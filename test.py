import os
import sys
import re
import ctypes
import hashlib
import mimetypes
from datetime import datetime

def is_admin():
    """Check if the script is running with admin privileges"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Re-run the script with admin privileges"""
    try:
        if not is_admin():
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                " ".join([sys.argv[0]] + sys.argv[1:]),
                None,
                1
            )
            sys.exit()
        return True
    except Exception as e:
        print(f"Error obtaining admin privileges: {e}")
        return False

def get_file_info(file_path):
    """Get detailed information about a file."""
    try:
        stats = os.stat(file_path)
        file_size = stats.st_size
        mod_time = datetime.fromtimestamp(stats.st_mtime)
        mime_type, _ = mimetypes.guess_type(file_path)

        # Calculate file hash
        md5_hash = hashlib.md5()
        with open(file_path, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                md5_hash.update(chunk)

        return {
            'size': file_size,
            'modified': mod_time,
            'mime_type': mime_type or 'unknown',
            'md5': md5_hash.hexdigest()
        }
    except Exception as e:
        return f"Error getting file info: {str(e)}"

def get_ignored_items():
    """Prompt user for directories or files to ignore."""
    ignored_items = input("Enter names of files or directories to ignore, separated by commas: ").strip()
    return set(ignored_items.split(','))

def generate_project_structure(directory, ignored_items, indent_level=0):
    """Generate a detailed project structure with file information."""
    structure = ""
    excluded_dirs = {'venv', '__pycache__', '.git', 'node_modules'}.union(ignored_items)

    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            if any(excluded in root for excluded in excluded_dirs):
                continue

            level = root.replace(directory, '').count(os.sep)
            indent = '│   ' * (level - indent_level)
            structure += f"{indent}├── {os.path.basename(root)}/\n"

            sub_indent = '│   ' * (level + 1 - indent_level)
            for file in files:
                if file in ignored_items:
                    continue
                file_path = os.path.join(root, file)
                file_info = get_file_info(file_path)
                if isinstance(file_info, dict):
                    structure += (f"{sub_indent}├── {file} "
                                f"({file_info['mime_type']}, "
                                f"{file_info['size']/1024:.1f}KB)\n")
                else:
                    structure += f"{sub_indent}├── {file} (error reading file)\n"

        return structure
    except Exception as e:
        return f"Error generating project structure: {str(e)}"

def extract_code_elements(content, file_ext):
    """Extract relevant elements based on file type."""
    elements = {}

    try:
        if file_ext == '.py':
            # Python-specific extraction
            class_regex = r'class\s+([a-zA-Z_]\w*)\s*(?:\([^)]*\))?:'
            method_regex = r'def\s+([a-zA-Z_]\w*)\s*\([^)]*\):'

            class_matches = re.finditer(class_regex, content)
            method_matches = re.finditer(method_regex, content)

            # Extract classes with their content
            elements['classes'] = []
            for match in class_matches:
                class_start = match.start()
                class_name = match.group(1)
                lines = content[class_start:].split('\n')
                class_content = [lines[0]]
                for line in lines[1:]:
                    if line and not line.startswith(' ') and not line.startswith('\t'):
                        break
                    class_content.append(line)
                elements['classes'].append((class_name, '\n'.join(class_content)))

            # Extract methods with their content
            elements['methods'] = []
            for match in method_matches:
                method_start = match.start()
                method_name = match.group(1)
                lines = content[method_start:].split('\n')
                method_content = [lines[0]]
                for line in lines[1:]:
                    if line and not line.startswith(' ') and not line.startswith('\t'):
                        break
                    method_content.append(line)
                elements['methods'].append((method_name, '\n'.join(method_content)))

        elif file_ext in ['.js', '.ts']:
            # JavaScript/TypeScript extraction
            class_regex = r'class\s+([a-zA-Z_]\w*)\s*{[^}]*}'
            function_regex = r'function\s+([a-zA-Z_]\w*)\s*\([^{]*{[^}]*}'

            elements['classes'] = [(m.group(1), m.group(0))
                                 for m in re.finditer(class_regex, content)]
            elements['functions'] = [(m.group(1), m.group(0))
                                   for m in re.finditer(function_regex, content)]

    except Exception as e:
        print(f"Error extracting code elements: {str(e)}")
        elements['error'] = str(e)

    return elements

def format_extracted_elements(elements, file_ext):
    """Format extracted elements into readable text."""
    formatted = ""

    try:
        if 'error' in elements:
            return f"\nError analyzing code: {elements['error']}\n"

        if file_ext == '.py':
            if elements.get('classes'):
                formatted += "\nClasses:\n" + "="*80 + "\n"
                for class_name, class_content in elements['classes']:
                    formatted += f"\nClass: {class_name}\n" + "-"*40 + "\n"
                    formatted += f"{class_content}\n"

            if elements.get('methods'):
                formatted += "\nMethods:\n" + "="*80 + "\n"
                for method_name, method_content in elements['methods']:
                    formatted += f"\nMethod: {method_name}\n" + "-"*40 + "\n"
                    formatted += f"{method_content}\n"

        elif file_ext in ['.js', '.ts']:
            if elements.get('classes'):
                formatted += "\nClasses:\n" + "="*80 + "\n"
                for class_name, class_content in elements['classes']:
                    formatted += f"\nClass: {class_name}\n" + "-"*40 + "\n"
                    formatted += f"{class_content}\n"

            if elements.get('functions'):
                formatted += "\nFunctions:\n" + "="*80 + "\n"
                for func_name, func_content in elements['functions']:
                    formatted += f"\nFunction: {func_name}\n" + "-"*40 + "\n"
                    formatted += f"{func_content}\n"

    except Exception as e:
        formatted += f"\nError formatting elements: {str(e)}\n"

    return formatted

def should_include_content(file_ext):
    """Determine if file content should be included based on extension."""
    code_extensions = {
        '.py', '.js', '.ts', '.java', '.kt', '.css', '.html', '.xml',
        '.json', '.yml', '.yaml', '.md', '.txt', '.rb', '.sh'
    }
    return file_ext.lower() in code_extensions

def read_files_recursively(directory, ignored_items):
    """Read and analyze all files recursively."""
    content = ""
    excluded_dirs = {'venv', '__pycache__', '.git', 'node_modules'}.union(ignored_items)
    excluded_extensions = {'.pyc', '.pyo', '.pyd', '.dll', '.exe'}
    binary_extensions = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg'}

    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            if any(excluded in root for excluded in excluded_dirs):
                continue

            for file in files:
                if file in ignored_items:
                    continue
                try:
                    file_path = os.path.join(root, file)
                    _, file_ext = os.path.splitext(file)

                    if file_ext.lower() in excluded_extensions:
                        continue

                    print(f"Processing file: {file_path}")
                    content += f"\nFile: {file_path}\n" + "="*80 + "\n"

                    # Get file information
                    file_info = get_file_info(file_path)
                    if isinstance(file_info, dict):
                        content += f"Size: {file_info['size']/1024:.1f}KB\n"
                        content += f"Modified: {file_info['modified']}\n"
                        content += f"Type: {file_info['mime_type']}\n"
                        content += f"MD5: {file_info['md5']}\n\n"

                    # Skip binary file content
                    if file_ext.lower() in binary_extensions:
                        content += "Binary file - content analysis skipped\n"
                        continue

                    # Include file content for code and text files
                    if should_include_content(file_ext):
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                file_content = f.read()
                                elements = extract_code_elements(file_content, file_ext.lower())
                                formatted_elements = format_extracted_elements(elements, file_ext.lower())
                                content += "File Content:\n" + "-"*40 + "\n"
                                content += file_content + "\n\n"
                                content += "Extracted Elements:\n" + "-"*40 + "\n"
                                content += formatted_elements
                        except UnicodeDecodeError:
                            with open(file_path, 'r', encoding='ISO-8859-1') as f:
                                content += "File content: Binary or non-text file\n"
                except Exception as e:
                    content += f"Error processing file {file}: {str(e)}\n"

                content += "\n" + "="*80 + "\n"

        return content
    except Exception as e:
        return f"Error reading files: {str(e)}"

def save_content_to_txt(directory, output_file, ignored_items):
    """Save project analysis to a file."""
    print("Starting project analysis...")

    try:
        output_dir = os.path.dirname(output_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        project_structure = generate_project_structure(directory, ignored_items)
        file_content = read_files_recursively(directory, ignored_items)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Project Structure:\n")
            f.write("=" * 80 + "\n\n")
            f.write(project_structure)
            f.write("\n\nDetailed File Analysis:\n")
            f.write("=" * 80 + "\n")
            f.write(file_content)

        print(f"Analysis completed successfully. Output saved to: {output_file}")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

def main():
    """Main function to run the script."""
    try:
        if not is_admin():
            print("Script requires admin privileges. Requesting elevation...")
            success = run_as_admin()
            if not success:
                print("Failed to obtain admin privileges. Please run as administrator.")
                sys.exit(1)

        project_directory = input("Enter the project directory path: ").strip()
        output_directory = input("Enter the output directory path: ").strip()

        # Get items to ignore
        ignored_items = get_ignored_items()

        if not os.path.exists(project_directory):
            print("Error: Project directory does not exist.")
            sys.exit(1)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = os.path.join(output_directory, f"project_analysis_{timestamp}.txt")

        print(f"\nAnalyzing project: {project_directory}")
        print(f"Output will be saved to: {output_file}\n")

        save_content_to_txt(project_directory, output_file, ignored_items)

    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
