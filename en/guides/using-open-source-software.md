# Guide for Using Open Source Software (Draft)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the [Procedures for Application Architecture](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8) provide that, where possible, open source software be used first.

> **Open source software must be selected first on the basis of its additional inherent flexibility and interoperability benefits, when there is no significant functionality or cost difference with closed-source solutions.**

The steps for GC to use open source software are:

1. [Actively and Fairly Consider Open Source Software](#actively-and-fairly-consider-open-source-software)
2. [Verify Open Source Software Licence](#verify-open-source-software-licence)
3. [Evaluate Support Options](#evaluate-support-options)
4. [Use Open Source Software Without Modification](#use-open-source-software-without-modification)
5. [Use Open Source Software With Modifications](#use-open-source-software-with-modifications)
6. [Register to Open Resource Exchange](#register-to-open-resource-exchange)

## Actively and Fairly Consider Open Source Software

Be aware that open source software is not completely free, so take into account the total cost of ownership (TCO) of migrating, including exit and transition costs.

### Be Aware of Open Core

A solution that is built with open source software but requires the use of closed-source components should not be considered open source software for the purpose of this guide.
The open core development model is where vendors open only portions of their software and then surround the remainder with closed-source offerings.
The "free" open source software versions often referred to as "community" editions are recommended first.
See [Verify Open Source Software Licence](#verify-open-source-software-licence).

### Selecting Open Source Software First

The mandatory procedures for enterprise architecture assessment require application architecture – for both new technology and upgrade/migration of existing solutions – to prioritize the use of open source software as well as open standards.
Doing so maximizes the substitutability and interoperability of software components and opens the door to creating highly flexible solutions.
It also helps mitigate the significant risks which arise from lock-in and similar issues.

Sometimes an open source solution meets most user needs but would require additional investment to develop missing functionality (see [Guide for Contributing to Open Source Software][guide-contribute-oss]).
In these cases, this investment must be considered by weighing the total cost of ownership against those of other candidate solutions.

### Evaluation

The same factors applicable to an evaluation of the feature set and maturity of closed-source software also apply to open source software.
Additional criteria should be assessed when evaluating open source software:

#### User Community

A strong user community involved in a project provides people to answer questions, test the software, report bugs, suggest improvements and drive forward overall interest in the software.
Look at the software's public code repository and check the project popularity by looking at the number of likes and followers.
Check how active the project responds to users by looking at issues and the time between replies.

#### Developer Community

A strong developer community with a history of releases and continued involvement tends to demonstrate that fixes and improvements to the software will continue into the future.
Look at who are the core developers and who is supporting the project and community, such as a non-profit Foundation.
Look at when the project got started, the pace of releases and responses to requests to merge code from contributors.

#### Documentation

User documentation provides important information to help users install software and use its features. Technical documentation provides requirements and instructions for installation, development, deployment and configuration of the software.

#### Security Assessments

Although OSS code is auditable, this does not necessarily mean it is secure.
The quality of the code and the typical response time for patching security-related flaws help indicate the security maturity level of the software.

As per any software, you should maintain best practices and have a process in place to list all packages in use as well as their version in order to patch them promptly­.

## Verify Open Source Software Licence

Whenever the Crown obtains software under an open source licence, departments should review the terms and conditions to validate if they can accept and comply with them given their particular business context.

The software is usually provided 'as-is' meaning the community will not accept liability or provide no financial compensation to the Crown for service interruption, loss of data, or loss of confidentiality. Data ownership and processing may remain with the user.

All software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses/alphabetical) or a [Free Software Foundation free software licence](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses) is considered open source software and can be used by GC [without modifications](#use-open-source-software-without-modification).
However if the software needs to be modified, the following considerations should be applied to help identify what licences terms and conditions the department is willing to approve.

<!-- markdownlint-disable MD006 -->
<!-- markdownlint-disable MD029 -->
1. Will you need to be making modifications to the source code of the application during its life cycle or will the software be used as a component of a custom development project?
   * No: It is used as a COTS; You can accept any OSI approved licence or FSF free software licence. See [Use Open Source Software Without Modification](#use-open-source-software-without-modification).
   * Yes: See 2.
2. Are there any reasons that would prevent the release of the modified source code?
   * No: You can accept any OSI approved licence or FSF free software licence. See [Use Open Source Software With Modifications](#use-open-source-software-with-modifications).
   * Yes: See 3.
3. Is the modified application going to be used as a web application?
   * Yes: You can accept any OSI approved licence or FSF free software licence **except** strong reciprocal licences. See [Strong Reciprocal Licences](#strong-reciprocal-licences).
   * No: See 4.
4. Is the modified application going to be distributed externally, outside the GC, either the source code or the binary?
   * No: You can accept any OSI approved licence or FSF free software licence.
   * Yes: You can accept any OSI approved licence or FSF free software licence **except** [Reciprocal Licences](#reciprocal-licences). Use only [Permissive Licences](#permissive-licences).
<!-- markdownlint-enable MD006 -->
<!-- markdownlint-enable MD029 -->

Additional consultation with legal and engineering teams should be done for scenarios where the open source software is used as a component of custom development (e.g.: dynamic vs static linking, licence compatibility, etc.).

### Popular and Widely Used Licences

The following is are lists of licences categorized by permissive and reciprocal. For full list refer to Open Source Initiative (OSI) and Free Software Foundation (FSF) Websites.

### Permissive Licences

* Apache License
* BSD license
* ISC License
* MIT license
* X11 license

### Reciprocal Licences

* Eclipse Public License (EPL)
* European Union Public License (EUPL)
* GNU General Public Licenses (GPL, LGPL and AGPL)
* Mozilla Public License (MPL)
* Open Software License (OSL)

## Evaluate Support Options

Use of open source software introduces a different model based on support services rather than obtaining software licences.

The two major support models for open source software are self support, where the department or agency's internal IT team is responsible for maintenance and interacting with the community, or professional support.

### Internal

Using a self-support model requires that the responsible teams:

* Have a proper process in place to manage the evaluation and the introduction of open source software in the organization.
* Maintain and track thorough lists of open source software used how and by whom.
* Ensure updates are applied in a timely fashion.

User and developer community should be leveraged for general support questions as well as reporting bugs, creating feature requests and code contributions.

When using software components for development purposes, powerful tools and services can be leveraged by IT teams to automate, facilitate and speed up the identification of these components, including open source software.
These tools can provide scanning capabilities for known security vulnerabilities as well as legal compliance.

See [Guide for Contributing to Open Source Software][guide-contribute-oss].

### Professional Services

It is possible to enter in contract with a company for professional services to provide maintenance, updates, warranty and liability for open source software.

Another scenario that may become recurrent would be choosing an open source software and using the community version and later down the road going for tender for professional support and maintenance.

When custom development requires the use of contracted developers, ensure that the proper rights to the source code are obtained to release as open source in accordance with the [Guide for Publishing Open Source Code][guide-publish-oss].

## Use Open Source Software Without Modification

**Using open source software without modification does not require that code be shared back.**

Configuration of software, even through configuration files, are not considered modifications.

This is also true for combinations of open source software to build a solution or open source software used for development and deployment.
See examples below:

| Standalone | Combination of components | Development and deployment |
| ---------- | ------------------------- | -------------------------- |
| Web browser, Productivity suite, Operating system and utilities (Window manager, Desktop environment, Text editor, Console..), .. | Application and plugins with database and web server | Custom development using open source software programming languages and dependencies, HTTP server, Database management system, Container platform |

For development or when writing source code, see [Guide for Publishing Open Source Code][guide-publish-oss].

## Use Open Source Software With Modifications

**Using open source software with modifications is not generally considered distribution and does not require that code be shared back.**

Modifications made to open source software should still be shared with the community to help ensure sustainability of the solution.
See [Guide for Contributing to Open Source Software][guide-contribute-oss].

For cases where sharing modifications is mandatory, see [Strong Reciprocal Implications](#strong-reciprocal-implications).

### Don't Fork Open Source Software

**Where possible, use open source software without modification.**

Use configuration and customize the software with modules, plugins or extensions and make those available to the community.
See [Guide for Publishing Open Source Code][guide-publish-oss].

It's easy to copy (fork) open source software and start making changes to the source code.
If a fork is created, be aware it can make future updates and security patches hard to implement.
The development team that made the changes will be responsible for maintaining those changes indefinitely unless they are contributed to the upstream version.

To make changes to open source software, engage with the community and submit changes upstream to ensure that they are supported by future updates.
See [Guide for Contributing to Open Source Software][guide-contribute-oss].

Note: this is easily confused with the process of forking projects on GitHub which is critical in submtting changes (Pull Requests) back to the original project. 

### Strong Reciprocal Implications

Strong reciprocal licences consider that software accessed through a network (like the Internet) is distribution and the modified source code must be made available to users.
See Guides for [Publishing Open Source Code][guide-publish-oss] and [Contributing to Open Source Software][guide-contribute-oss].

#### Strong Reciprocal Licences

The [Open Source Initiative approved licenses](https://opensource.org/licenses/alphabetical) and the [Free Software Foundation free software licences](https://www.gnu.org/licenses/license-list.html#SoftwareLicenses) contain the following strong reciprocal licences.

* GNU Affero General Public License (AGPL)
* European Union Public License (EUPL)
* Open Software License (OSL)

## Register to Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/en/open-source-software.html).

Instructions on how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/blob/master/_data/README.md).

<!-- References -->
[guide-contribute-oss]: contributing-to-open-source-software.md
[guide-publish-oss]: publishing-open-source-code.md
