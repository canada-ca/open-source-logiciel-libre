# Guides for Using Open Source Software

* [Without modification](without-modification)
* [With modification](#with-modification)

Proposed structure in table:

* Without modification
  * Standalone Software
  * Combination of components configured and integrated only (no custom code)
  * Custom development with dependencies such as libraries and frameworks
    * Automatically need to consider rules/guides on publishing
* With modification
  * Automatically need to consider rules/guides on publishing

## Without modification

This section covers the use of open source software without modifications. The software could be used for scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops and devices, essentially like "Commercial Off-The-Shelf" (COTS) software, solutions and tools.
This includes configurations and combinations of multiple open source software and it's use in development.

### Approvals

Approvals reside with each government department or agency's information management and technology group.

### Licenses

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used as long as its use is compliant with its terms and conditions. Consult with your legal team if you are not sure.

Use in web service may require release of source code; proper analysis of obligations are required. (e.g. AGPL-like implications)

### Evaluation

The same factors applicable to an evaluation of the feature set and maturity of closed-source software also apply to OSS. A few additional criteria should be assessed when evaluating OSS:

* **Community** A strong user community involved in a project provides people to answer questions, test the software, report bugs, suggest improvements and drive forward overall interest in the software.
  * How? By looking at the number of contributors, of stars, bookmarks or likes on a project, the issues log, length of time between replies, last comments (a few days, a year, etc.), etc.
* **Release Activity** A strong developer community with a history of releases and continued involvement tends to demonstrate that fixes and improvements to the software will continue into the future.
  * How? Looking at pace of releases, number of commits, pull requests, actual releases and updates.
* **Longevity** This is measured in both in terms of the age of the product and the number of versions released, indicates a project's stability and chance of survival.
  * How? Looking at how long the project has been running, number of core contributors and their continous invovlment. Any support from foundations and companies, etc.
* **Support** Availability Support considerations include user support (i.e., the availability of assistance with installation and usage) and maintenance (i.e., fixing problems in the software). Support for OSS can be provided by the community and/or paid support services businesses.
  * How?
* **Documentation** User documentation provides important information to help users install software and use its features. Technical documentation provides requirements and instructions for installation, development, deployment and configuration of the software.
* **Security** Although OSS code is auditable, this does not necessarily mean it is secure. The quality of the code and the typical response time for patching security-related flaws help indicate the security level of the software. **Should have a process to list all packages and maintain versions, just like any other software.**
* **Functionality** Specific functionality needs depend on the business case for the software and need to be assessed on a case-by-case basis.
* **Integration** Where a software package will interact with other pieces of software, or with particular data formats, compatibility and the ability to integrate the software and data together becomes a paramount consideration.

### Using in Development Projects

Things specific to using OSS in development project. Either by having dynamicly linked dependencies or directly including code.

#### Licences

Be careful when combining code with different licenses. Certain licenses are incompatible when combined in the same program.

note: Maintain updates and need to log all licences for notices

### Maintenance and Support

#### Self-support

Maintain and track thorough lists of open source software used and ensure updates are applied carefully.

Community support for issues and questions.

#### Professional Support

Choosing an open source software and using the community version, then going for tender for professional support and Maintenance: implications and process to be expanded.

Possible to enter in contract with company for professional service to provide maintenance, updates, warranty and liability, just like any other software.

### Open Resource Exchange

Add open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).

Instructions for how to updated the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

## With modification

This section covers the use of open source software with modification weather its scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops or devices.

### Licences

Need to use components with compatible licences
