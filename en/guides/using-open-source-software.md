# Guide for Using Open Source Software (Draft)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the [Procedures for Application Architecture](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8) provide that, where possible, open source software be used first.

> **Open source software must be selected first on the basis of its additional inherent flexibility and interoperability benefits, when there is no significant functionality or cost difference with closed-source solutions.**

The steps for GC to use open source software are:

1. [Actively and Fairly Consider Open Source Software](#actively-and-fairly-consider-open-source-software)
1. [Verify Open Source Software Licence](#verify-open-source-software-licence)
1. [Evaluate Support Options](#evaluate-support-options)
1. [Use Open Source Software Without Modification](#use-open-source-software-without-modification)
1. [Use Open Source Software With Modifications](#use-open-source-software-with-modifications)
1. [Other Notes](#other-notes)

## Actively and Fairly Consider Open Source Software

Be aware that open source software is not completely free, so take into account the total cost ownership (TCO) of migrating, including exit and transition costs.

### Be Aware of Open Core

A solution that is built with open source software but requires the use of closed-source components should not be considered open source software for the purpose of this guide.
The open core development model is where vendors open only portions of their software and then surround the remainder with closed-source offerings.
The "free" open source software versions often referred to as "community" editions are recommended first.
See [Verify Open Source Software Licence](#verify-open-source-software-licence).

### Selecting Open Source Software First

The mandatory procedures for enterprise architecture assessment state that security and privacy must be implemented across all architectural layer and start with the business architecture to align to the GC business capability model and identify capabilities that can be shared and reused.
The Business Process Management Notation (BPMN) open standard is identified and must be used to model business processes.
Systems must be accessible, multilingual, measurable, accountable and designed for users first.

Then the information architecture, to ensure data is collected, managed and stored in a manner that maximizes use and availability, aligns to existing standards and enable accessibility and interoperability while being properly categorized to determine appropriate safeguards required.

**Application architecture is where open standard and open source software a to be prioritized in the selection process** allowing for substitutability and interoperability while avoiding lock-in.
If an open source software based solution meets most of the users needs but requires investment to develop remaining functionalities, this option must also be considered by comparing the TCO.
See Guide for [Contributing to Open Source Software](contributing-to-open-source-software.md).

Finally, the technology architecture is where the use of cloud services must be considered first, especially Software as a Service (SaaS) first and public cloud first but always thinking of cloud mobility and developing an exit strategy to avoid lock-in.

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

Although OSS code is auditable, this does not necessarily mean it is secure. The quality of the code and the typical response time for patching security-related flaws help indicate the security level of the software.

**note:** Should have a process to list all packages and maintain versions.

## Verify Open Source Software Licence

All software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) or a [Free Software Foundation free software licence](https://www.gnu.org/licenses/license-list.html) is considered open source software and can be used by GC.

## Evaluate Support Options

Use of open source software introduces a different model  based on support services rather than obtaining software licences.

The two major support models for open source software are self support, where the department or agency's internal IT team is responsible for maintenance and interacting with the community, or professional support.

**notes:** Availability Support considerations include user support (i.e., the availability of assistance with installation and usage) and maintenance (i.e., fixing problems in the software).

Since a financial transaction may not have occurred, it is important to have a proper process and tracking mechanism in place to manage the introduction of open source software...

### Internal

Using a self-support model requires that the responsible teams:

* Maintain and track thorough lists of open source software used and ensure updates are applied carefully.
* User and developer community should be leveraged for general support questions as well as reporting bugs, creating feature requests and code contributions.

See [Guide for Contributing to Open Source Software](contributing-to-open-source-software.md).

### Professional Services

It is possible to enter in contract with a company for professional services to provide maintenance, updates, warranty and liability for open source software.

Another scenario that may become recurrent would be choosing an open source software and using the community version and later down the road going for tender for professional support and maintenance.

When custom development requires the use of contracted developers, ensure that the proper rights to the source code are obtained to release as open source in accordance to the [Guide for Publishing Open Source Code](publishing-open-source-code.md).

## Use Open Source Software Without Modification

**Using open source software without modification does not require that code be shared back.**

Configuration of software, even through configuration files, are not considered modifications.

This is also true for combinations of open source software to build a solution or open source software used for development and deployment.
See examples below:

| Standalone | Combination of components | Development and deployment |
| ---------- | ------------------------- | -------------------------- |
| Web browser, Productivity suite, Operating system and utilities (Window manager, Desktop environment, Text editor, Console..), .. | Application and plugins with database and web server | Custom development using open source software programming languages and dependencies, HTTP server, Database management system, Container platform |

For development or when writing source code, see [Guide for Publishing Open Source Code](publishing-open-source-code.md).

## Use Open Source Software With Modifications

**Using open source software with modifications is not generally considered distribution and does not require that code be shared back.**

Modifications made to open source software should still be shared with the community to help ensure sustainability of the solution.
See [Guide for Contributing to Open Source Software](contributing-to-open-source-software.md).

For cases where sharing modifications is mandatory, see [Strong Reciprocal Implications](#strong-reciprocal-implications).

### Don't Fork Open Source Software

**Where possible, use open source software without modification.**

Use configuration and customize the software with modules, plugins or extensions and make those available to the community.
See [Guide for Publishing Open Source Code](publishing-open-source-code.md).

It's easy to copy (fork) open source software and start making changes to the source code.
If a fork is created, be aware it can make future updates and security patches hard to implement.
The development team that made the changes will be responsible for maintaining those changes indefinitely unless they are contributed to the upstream version.

To make changes to open source software, engage with the community and submit changes upstream to ensure that they are supported by future updates.
See [Guide for Contributing to Open Source Software](contributing-to-open-source-software.md).

### Strong Reciprocal Implications

The AGPL reciprocal licence and others like the EUPL considers that software accessed through a network (like the Internet) is distribution and the modified source code must be made available to users.
See Guides for [Publishing Open Source Code](publishing-open-source-code.md) and [Contributing to Open Source Software](contributing-to-open-source-software.md).

## Other Notes

### Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).

Instructions for how to updated the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).
