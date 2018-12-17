# Guides for Using Open Source Software

* Active and Fair Consideration
  * Cloud
  * Approvals
  * Evaluation
* Legal Compliance
* Types of use
  * Without modification
    * Combination of components and development
  * With modification

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the procedures for Application Architecture provide that, where possible, you must use open standards and open source software first as well as leverage and reuse existing solutions, components, and processes accross departments and agencies.

Using open source software means you can benefit from:

* solving common problems with readily available open source technology
* more time and resource for customised solutions to solve the rare or unique problems
* lower implementation and running costs

Be aware that open source software is not completely free, so take into account the total cost of migrating, including exit and transition costs.

## Active and Fair Consideration

Open source software must be selected on the basis of its additional inherent flexibility, when there is no significant functionnality difference with closed-source solutions.

If an open source software based solution meets most of the users needs but requires investment to develop remaining functionalities, this option must be considered by comparing the total cost of ownership (TCO) possible solutions.

See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

Using open source software provides an opertunity to share and reuse existing solutions, components, and processes with no additional, or minimal, licence costs.

### Cloud

Some open source software is available directly as software as a service (SaaS) on the cloud either for free or subsrciption based.
Most open source software can be deployed using platform as a service (PaaS) infrastructure as a service (IaaS).
Open source software is often what is running at the PaaS and IaaS layers of the cloud stack.

**note:** If you can find support for it or can self-support, open source software for user applications is considered SaaS.

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

#### Availibility of Support

Use of open source software introduces a different model  based on support services rather than obtaining software licences.

The two major support models for open source software are self support, where the department or agency's internal IT team is responsible for maintenance and interacting with the community, or professional support.

**notes:** Availability Support considerations include user support (i.e., the availability of assistance with installation and usage) and maintenance (i.e., fixing problems in the software).

Since a financial transaction may not have occured, it is important to have a proper process and tracking mechanism in place to manage the introduction of open source software...

##### Self-support

* Maintain and track thorough lists of open source software used and ensure updates are applied carefully.
* User and developer community should be levereged for general support questions as well as reporting bugs, creating feature requests and code contricutions.

See [Guides for Contributing to Open Source Software](contributing-to-open-source-software.md).

##### Professional Support

It is possible to enter in contract with a company for professional services to provide maintenance, updates, warranty and liability for open source software.

Another scenario that may become recurrent would be choosing an open source software and using the community version and later down the road going for tender for professional support and maintenance. *However, proper guidance needs to be confirmed with legal and procurement teams.*

Custom development with traditional request for proposal contracted developers should be done in a way so that the resulting source code may be released under an open source licences.

Finally, another option would be to leverage the [GCDevExchange](https://gcdevexchange-carrefourproggc.org/en) to have some custom code written for the government of Canada as open source through a bidding process. Code developed through this platform should be published as open source.

Whenever custom code is involved you should follow the guide for [Publishing Open Source Code](publishing-open-source-code.md).

#### Documentation

User documentation provides important information to help users install software and use its features. Technical documentation provides requirements and instructions for installation, development, deployment and configuration of the software.

#### Security Assesments

Although OSS code is auditable, this does not necessarily mean it is secure. The quality of the code and the typical response time for patching security-related flaws help indicate the security level of the software.

**note:** Should have a process to list all packages and maintain versions.

## Legal Compliance

The use of open source software must be done in compliance with the terms and conditions under which it is released. Unlike closed-source software, the licences are provided publicly with a set of rights and constraints.

Depending on the intended use, the licence under which an open source software was released may put some specific requirements on the user.

## Types of use

* [Without modification](#without-modification)
  * [Combination of components and development](#combination-of-components-and-development)
* [With modification](#with-modification)

### Without modification

This section covers the use of open source software without modifications.
The software could be used for scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops and devices, essentially like Commercial Off-The-Shelf (COTS) software, solutions and tools.
This includes configurations and combinations of multiple open source software and it's use in development.

|                                          | Standalone | Combination of components | Development |
| ---------------------------------------- | ---------- | ------------------------- | ----------- |
| **Examples** | Web browser, HTTP server, Database management system, Container platform, Operating system and utilities (Window manager, Text editor, Shell (console)..), .. | Application and plugins with database and web server | Custom development using open source software programming languages and dependencies |

The following applies to all types of use of open source software without modifications.

#### Licenses

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used as long as its use is compliant with its terms and conditions.
Using open source software without modifications internally (within the Governemnt of Canada) and for public facing applications is not considered distribution and does not require that code be shared back.

#### Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).

Instructions for how to updated the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

#### Combination of components and development

##### Licences

* Be careful when combining code with different licenses (dynamicly linked dependencies or directly including code).
* Certain licenses are incompatible when combined in the same program.
* Maintain updates and need to log all licences for notices and legal audits.

Your legal team should be contacted to help understand the nuances of the licences.

See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

### With modification

This section covers the use of open source software with modification weather its scripts, libraries, plugins, platforms, applications, services, databases and operating systems for servers, desktops or devices.

#### Don't Fork Open Source Software

It's simple to make a copy (fork) of open source software and start making changes to it.
But be aware this can make future updates and security patches hard to implement as well as trigger additional licence obligations.
The development team that made the changes will be responsible for maintaining those changes unless they are contributed to the original (upstream) version.

Use open source software without modifications and customizing it with modules, plugins or extensions, then share those back to the community.
See [Guides for Publishing Open Source Code](publishing-open-source-code.md).

To make changes in open source software, engage with the community and submit your changes upstream to ensure that your modificaitons are supported by future updates.
See [Guides for Contributing to Open Source Software](contributing-to-open-source-software.md).

#### Licences

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used as long as its use is compliant with its terms and conditions.

Using open source software with modifications internally (within the Governemnt of Canada) and for public facing applications is not generally considered distribution and does not require that code be shared back.
See notes on AGPL below.

##### AGPL like reciprocal implications

The AGPL reciprocal licence and others like the EUPL require that source code for applications accessed through a network (like the Internet) be made available.

See [Guides for Publishing Open Source Code](publishing-open-source-code.md).
