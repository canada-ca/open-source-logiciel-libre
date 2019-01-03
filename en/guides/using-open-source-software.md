# Guides for Using Open Source Software

* [Active and Fair Consideration](#active-and-fair-consideration)
  * [Cloud](#cloud)
  * [Approvals](#approvals)
  * [Evaluation](#Evaluation)
* [Types of Use](#types-of-use)
  * [Without Modification](#without-modification)
    * [Combination of Components and Development](#combination-of-components-and-development)
  * [With Modification](#with-modification)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the procedures for Application Architecture provide that, where possible, you must use open standards and open source software first as well as leverage and reuse existing solutions, components, and processes across departments and agencies.

Using open source software means you can benefit from:

* solving common problems with readily available open source technology
* more time and resource for customised solutions to solve the rare or unique problems
* lower implementation and running costs

Be aware that open source software is not completely free, so take into account the total cost of migrating, including exit and transition costs.

## Active and Fair Consideration

See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

Using open source software provides an opportunity to share and reuse existing solutions, components, and processes with no additional, or minimal, licence costs.

### Approvals

Approvals reside with each government department or agency's information management and technology group.

### Evaluation

The same factors applicable to an evaluation of the feature set and maturity of closed-source software also apply to OSS [link]. A few additional criteria should be assessed when evaluating OSS:

#### User Community

A strong user community involved in a project provides people to answer questions, test the software, report bugs, suggest improvements and drive forward overall interest in the software.
Look at the software's public code repository and check the project popularity by looking at the number of likes and followers.
Check how active the project responds to users by looking at issues and the time between replies.

#### Developer Community

A strong developer community with a history of releases and continued involvement tends to demonstrate that fixes and improvements to the software will continue into the future.
Look at who are the core developers and who is supporting the project and community, such as a non-profit Foundation.
Look at when the project got started, the pace of releases and responses to requests to merge code from contributors.

#### Availability of Support

Use of open source software introduces a different model  based on support services rather than obtaining software licences.

The two major support models for open source software are self support, where the department or agency's internal IT team is responsible for maintenance and interacting with the community, or professional support.

**notes:** Availability Support considerations include user support (i.e., the availability of assistance with installation and usage) and maintenance (i.e., fixing problems in the software).

Since a financial transaction may not have occurred, it is important to have a proper process and tracking mechanism in place to manage the introduction of open source software...

#### Documentation

User documentation provides important information to help users install software and use its features. Technical documentation provides requirements and instructions for installation, development, deployment and configuration of the software.

#### Security Assessments

Although OSS code is auditable, this does not necessarily mean it is secure. The quality of the code and the typical response time for patching security-related flaws help indicate the security level of the software.

**note:** Should have a process to list all packages and maintain versions.

## Types of Use

Depending on the intended use, the licence under which an open source software was released may put some specific requirements on the user.

* [Without Modification](#without-modification)
  * [Combination of Components and Development](#combination-of-components-and-development)
* [With Modification](#with-modification)

### Without Modification

This section covers the use of open source software without modifications.
The software could be used for scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops and devices, essentially like Commercial Off-The-Shelf (COTS) software, solutions and tools.
This includes configurations and combinations of multiple open source software and it's use in development.

|                                          | Standalone | Combination of components | Development |
| ---------------------------------------- | ---------- | ------------------------- | ----------- |
| **Examples** | Web browser, HTTP server, Database management system, Container platform, Operating system and utilities (Window manager, Text editor, Shell (console)..), .. | Application and plugins with database and web server | Custom development using open source software programming languages and dependencies |

The following applies to all types of use of open source software without modifications.

#### Combination of Components and Development

* Be careful when combining code with different licenses (dynamically linked dependencies or directly including code).
* Certain licenses are incompatible when combined in the same program.
* Maintain updates and need to log all licences for notices and legal audits.

Your legal team should be contacted to help understand the nuances of the licences.

See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

**note:** notice?

#### Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).

Instructions for how to updated the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

### With Modification

This section covers the use of open source software with modification weather its scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops or devices.

#### Don't Fork Open Source Software

It's simple to make a copy (fork) of open source software and start making changes to it.
But be aware this can make future updates and security patches hard to implement as well as trigger additional licence obligations.
The development team that made the changes will be responsible for maintaining those changes unless they are contributed to the original (upstream) version.

Use open source software without modifications and customizing it with modules, plugins or extensions, then share those back to the community.
See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

To make changes in open source software, engage with the community and submit your changes upstream to ensure that your modifications are supported by future updates.
See [Guides for Contributing to Open Source Software](contributing-to-open-source-software.md).

**note:** don't just copy parts of code from OSS...
