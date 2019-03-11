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
1. [Decision Tree for Use of Open Source Software](#decision-tree-for-use-of-open-source-software)
1. [Other Notes](#other-notes)

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

See [Guide for Contributing to Open Source Software][guide-contribute-oss].

### Professional Services

It is possible to enter in contract with a company for professional services to provide maintenance, updates, warranty and liability for open source software.

Another scenario that may become recurrent would be choosing an open source software and using the community version and later down the road going for tender for professional support and maintenance.

When custom development requires the use of contracted developers, ensure that the proper rights to the source code are obtained to release as open source in accordance with the [Guide for Publishing Open Source Code][guide-publish-oss].

## Use Open Source Software Without Modification

**Using open source software without modification does not require that code be shared back.**

Configuration of software, even through configuration files, are not considered modifications.

This is also true for combinations of open source softwarfb72776bdc8f703a81e31d9297af0e9d2d589347e to build a solution or open source software used for development and deployment.
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

### Strong Reciprocal Implications

The AGPL reciprocal licence and others like the EUPL considers that software accessed through a network (like the Internet) is distribution and the modified source code must be made available to users.
See Guides for [Publishing Open Source Code][guide-publish-oss] and [Contributing to Open Source Software][guide-contribute-oss].

## Decision Tree for Use of Open Source Software

Whenever the Crown obtains software under an open source licence, departments should review the terms and conditions to validate if they can accept and comply with them given their particular business context.
* There is no negotiation expected with the community and, by default, limitation of liability and indemnification disclosure is common:
  * The software is usually provided 'as-is' meaning the community will not accept liability or provide no financial compensation to the Crown for service interruption, loss of data, or loss of confidentiality
  * Data ownership and processing may remain with the user
* A primary step for departments should be to assess if the licence is endorsed by the non-profit Open Source Initiative (OSI) group, as these are deemed to be the industry standards.
There is a transparent and public vetting process for all of their approved licences. (See Annex below for detailed breakdown of open source software licences)
* Then, depending on the capacity of the department to abide by the terms and conditions, the software can be obtained following the standard security evaluation processes.

In general, for acquisition purposes of open source software, the following decision tree should be used to help identify what licences terms and conditions the department is willing to approve:

<!-- markdownlint-disable MD006 -->
<!-- markdownlint-disable MD029 -->
1. Will you need to be making modifications to the source code of the application during its life cycle or will the software be used as a component of a custom development project?
  * a) No: It is used as a COTS; You can accept any OSI approved licence from section A) and B) of the Annex below.
  * b) Yes: See 2.
2. If you make modifications to the source code or if you are using the software as a part of a custom development, are there any reasons that would prevent the release of the modified source code? (Consider the update on the Directive on Management of IT: all custom source code must be released as open source)
  * a) No: You can accept any OSI approved licence from section A) and B) of the Annex below.
  * b) Yes: See 3.
3. Is the modified application going to be used as a web application?
  * a) No: See 4.
  * b) Yes: You can accept any OSI approved licence from section A) and B) of the Annex below except AGPL-like licences
4. Is the modified application going to be distributed externally, outside the GC, either the source code or the binary?
  * a) No: You can accept any OSI approved licence from section A) and B) of the Annex below.
  * b) Yes: You should accept only permissive licences from section A) and B) of the Annex below.

<!-- markdownlint-enable MD006 -->
<!-- markdownlint-enable MD029 -->

The decision tree above is only provided as a general guidance. Additional consultation with legal and engineering teams should be done for scenarios where the open source software is used as a component of custom development (e.g.: dynamic vs static linking, licence compatibility, etc.).

## Annex A

Recommendation of licences to accept in the GC. Original list comes from the [Open Source Initiative](https://opensource.org/licenses/category), tailored for the GC.

**A)** The main OSI approved licences that could be recommended for the crown are the following:
* Popular and widely-used or with strong communities
  * Apache License 2.0 (Apache-2.0)
  * 3-clause BSD license (BSD-3-Clause)
  * 2-clause BSD license (BSD-2-Clause)
  * GNU General Public License (GPL)
  * GNU Lesser General Public License (LGPL)
  * MIT license (MIT)
  * Mozilla Public License 2.0 (MPL-2.0)
  * Common Development and Distribution License version 1.0 (CDDL-1.0)
  * Eclipse Public License version 2.0
* International licenses
  * Licence Libre du Québec – Permissive (LiLiQ-P) version 1.1 (LiLiQ-P-1.1)
  * Licence Libre du Québec – Réciprocité (LiLiQ-R) version 1.1 (LiLiQ-R-1.1)
  * Licence Libre du Québec – Réciprocité forte (LiLiQ-R+) version 1.1 (LiLiQ-Rplus-1.1)
* Other approved licences that may be accepted:
  * Boost Software License (BSL-1.0)
  * CeCILL License 2.1 (CECILL-2.1)
  * Common Public Attribution License 1.0 (CPAL-1.0)
  * European Union Public License (EUPL-1.2)
  * GNU Affero General Public License v3 (AGPL-3.0)
  * ISC License (ISC)
  * Microsoft Public License (MS-PL)
  * Microsoft Reciprocal License (MS-RL)
  * MirOS Licence (MirOS)
  * Non-Profit Open Software License 3.0 (NPOSL-3.0)
  * NTP License (NTP)
  * Reciprocal Public License 1.5 (RPL-1.5)
  * Simple Public License 2.0 (SimPL-2.0)
  * Open Group Test Suite License (OGTSL)

**B)** Non-reusable licences must only be accepted if they are applied to the software for which they have been written (e.g. the Python License can’t be accepted for the use of software other than Python):
* Apple Public Source License (APSL-2.0)
* Computer Associates Trusted Open Source License 1.1 (CATOSL-1.1)
* eCos License version 2.0
* EU DataGrid Software License (EUDatagrid)
* Entessa Public License (Entessa)
* Frameworx License (Frameworx-1.0)
* IBM Public License (IPL-1.0)
* LaTeX Project Public License (LPPL-1.3c)
* Motosoto License (Motosoto)
* Multics License (Multics)
* Naumen Public License (Naumen)
* Nethack General Public License (NGPL)
* Nokia Open Source License (Nokia)
* OCLC Research Public License 2.0 (OCLC-2.0)
* PHP License (PHP-3.0)
* Python License (Python-2.0)
* CNRI Python license (CNRI-Python) (CNRI portion of Python License)
* RealNetworks Public Source License V1.0 (RPSL-1.0)
* Ricoh Source Code Public License (RSCPL)
* Sleepycat License (Sleepycat)
* Sun Public License (SPL-1.0)
* Sybase Open Watcom Public License 1.0 (Watcom-1.0)
* Vovida Software License v. 1.0 (VSL-1.0)
* W3C License (W3C)
* wxWindows Library License (WXwindows)
* Zope Public License (ZPL-2.0)

**C)** Amongst the OSI approved licences, some categories should however not be considered:
* Licenses that have been voluntarily retired
  * CUA Office Public License Version 1.0 (CUA-OPL-1.0)
  * Intel Open Source License (Intel)
  * Jabber Open Source License
  * MITRE Collaborative Virtual Workspace License (CVW)
  * Sun Industry Standards Source License (SISSL)
* Special purpose licenses
  * BSD+Patent (BSD-2-Clause-Patent)
  * Educational Community License, Version 2.0 (ECL-2.0)
  * IPA Font License (IPA)
  * NASA Open Source Agreement 1.3 (NASA-1.3)
  * OSET Public License version 2.1 (OSET-PL-2.1)
  * SIL Open Font License 1.1 (OFL-1.1)
  * Upstream Compatibility License v1.0
* Superseded licences
  * Boost Software License (BSL-1.0)
  * CeCILL License 2.1 (CECILL-2.1)
  * Common Public Attribution License 1.0 (CPAL-1.0)
  * European Union Public License (EUPL-1.2)
  * GNU Affero General Public License v3 (AGPL-3.0)
  * ISC License (ISC)
  * Microsoft Public License (MS-PL)
  * Microsoft Reciprocal License (MS-RL)
  * MirOS Licence (MirOS)
  * Non-Profit Open Software License 3.0 (NPOSL-3.0)
  * NTP License (NTP)
  * Reciprocal Public License 1.5 (RPL-1.5)
  * Simple Public License 2.0 (SimPL-2.0)
  * Open Group Test Suite License (OGTSL)

## Other Notes

### Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).

Instructions on how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

<!-- References -->
[guide-contribute-oss]: contributing-to-open-source-software.md
[guide-publish-oss]: publishing-open-source-code.md