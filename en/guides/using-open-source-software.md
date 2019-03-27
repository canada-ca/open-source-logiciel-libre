# Guide for Using Open Source Software (Draft)

## Purpose
This document provides guidance to departments on implementing the Treasury Board Directive on Management of Information Technology (Appendix C, Use of Open Standards and Solutions by Default). This appendix provides mandatory procedures for the assessment of digital initiatives by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB.

This guideline provides tips and tools for the selection and use of open source software, without modifications to the source code.

Its accompanying guidelines are Guideline on Open Source Software Modification and Contribution to Projects, and Guideline on Leading Open Source Software Projects.

## Introduction
The Government of Canada has been using Open Source Software as part of its technology ecosystem for years and is increasingly relying on them for successful service delivery. As part of its Digital Government commitments, the Government of Canada will release its own source code under Open Source Licences and will contribute source code to non-governmental projects. The Government is committed to doing so in a manner that is compatible with core administrative law principles such as transparency, accountability, legality and procedural fairness.

## Actively and Fairly Consider Open Source Software

### Selecting Open Source Software First
The mandatory procedures for enterprise architecture assessment require application architecture – for both new technology and upgrade/migration of existing solutions – to prioritize the use of open source software as well as open standards. Doing so maximizes the substitutability and interoperability of software components and opens the door to creating highly flexible solutions. It also helps mitigate the significant risks which arise from lock-in and similar issues.
Sometimes an open source solution meets most user needs but would require additional investment to develop missing functionality (see Guideline on Open Source Software Modification and Contribution to Projects). Open source software is free to modify, but it is not free of cost. The labour costs to install, configure, modify and maintain must be taken into account to estimate the total cost of ownership (TCO). This must be taken into account when comparing with other candidate solutions.

### Evaluating Open Source Software
The same factors used to evaluate the feature set and maturity of closed-source software, apply to open source software. These additional criteria are specific to the evaluation of open source software:

#### User Community
A strong user community involved in a project provides people to answer questions, test the software, report bugs, suggest improvements and drive forward overall interest in the software. The engagement of the user community can be assessed by the open source software project’s social media activity, mentions, likes and followers. 

#### Developer Community
Open source software is created and maintained by its developer community. This community corresponds to the manufacturer of proprietary software. A strong developer community with a history of releases and continued involvement is an indicator of longevity. 

Positive indicators:
* Project supported by a non-profit foundation 
* Developer community composed of leaders within the industry or knowledge domain.
* Quick pace of releases, and responses to requests to merge code from contributors.

#### Documentation
User documentation provides important information to help users install software and use its features. Technical documentation provides requirements and instructions for installation, development, deployment and configuration of the software.

#### Security Management
Although OSS code is auditable, this does not necessarily mean it is secure. The quality of the code and the typical response time for patching security-related flaws help indicate the security level of the software.
Note: The project should have a process to list all packages and maintain versions.

#### Open Core vs. Open Source
A solution that is built with open source software but requires the use of closed-source components should not be considered open source software for the purpose of this guide. The open core development model is where vendors open only portions of their software and then surround the remainder with closed-source offerings. The "free" open source software versions often referred to as "community" editions are recommended first. 

#### Evaluate Support Options
Use of open source software introduces a different model based on support services rather than purchasing software licences.

The two major support models for open source software are self-support, where the department or agency's internal IT team is responsible for maintenance, or support via professional services.

Support considerations include user support (i.e., the availability of assistance with installation and usage), and maintenance (i.e. patches, updates, optimization).

### Use Approved and Compatible Licences
All software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) or a [Free Software Foundation free software licence](https://www.gnu.org/licenses/license-list.html) free software licence is considered open source software and can be used.


## Maintaining Open Source Software

Use the Community Version
It is recommended that the community version be used without modifications. Installation, maintenance and support can be done by departmental staff or contracted out.

Using a self-support model requires that the responsible teams:
*	Maintain and track lists of open source software used and ensure updates are applied in a timely manner.
*	User and developer community should be leveraged for general support questions as well as reporting bugs, creating feature requests.

Using professional services for maintenance and customization requires that the proper rights to the source code are obtained to release the modifications as open source in accordance with the Guide to Leading Open Source Projects.

## Decision Tree for the Use of Open Source Software

Whenever the Crown obtains software under an open source licence, departments should review the terms and conditions to validate if they can comply to its terms.
* It is not possible to negotiate the terms and conditions with the development community, therefore, by default, clauses to address  limitation of liability and indemnification disclosure are common:
  * The software is usually provided 'as-is' meaning the community will not accept liability or provide financial compensation to the Crown for service interruption, loss of data, or loss of confidentiality
  * Data ownership and processing may remain with the user
* As a first step, departments should assess if the licence is endorsed by the non-profit Open Source Initiative (OSI) group, as these are deemed to be the industry standards.
There is a transparent and public vetting process for all of their approved licences. (See Annex below for detailed breakdown of open source software licences)
* Then, depending on the capacity of the department to abide by the terms and conditions, the software can be obtained following the standard security evaluation processes.

In general, for acquisition of open source software, the following decision tree should be used to help identify what licences terms and conditions the department is willing to approve:

<!-- markdownlint-disable MD006 -->
<!-- markdownlint-disable MD029 -->
1. Will modifications to the source code be required during its life cycle or will the software be used as a component of a custom development project?
  * a) No: It is used as-is, like any other commercial product; the department can accept any OSI approved licence from section A) and B) of the Annex below.
  * b) Yes: See 2.
2. If source code modifications are required or if the software is a part of a custom development, are there any reasons that would prevent the release of the modified source code? (Consider the update on the Directive on Management of IT: all custom source code must be released as open source)
  * a) No: Any OSI approved licence can be accepted, from section A) and B) of the Annex below.
  * b) Yes: See 3.
3. Is the modified source code for a web application?
  * a) No: See 4.
  * b) Yes: Refer to the Guideline on Open Source Software Modification and Contribution to Projects.
4. Is the modified application going to be distributed externally, outside the GC, either the source code or the binary?
  * Refer to the Guideline on Open Source Software Modification and Contribution to Projects.

<!-- markdownlint-enable MD006 -->
<!-- markdownlint-enable MD029 -->

The decision tree above is only provided as a general guidance. Additional consultation with legal and engineering teams should be done for scenarios where the open source software is used as a component of custom development (e.g.: dynamic vs static linking, licence compatibility, etc.).

## Key Terms and Definitions

## Annex A: Acceptable Open Source Licences

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
  * Apache Software License 1.1 (Apache-1.1)
  * Artistic license 1.0 (Artistic-1.0)
  * Common Public License 1.0 (CPL-1.0)
  * Eclipse Public License 1.0 (EPL-1.0)
  * Educational Community License, Version 1.0 (ECL-1.0)
  * Eiffel Forum License V1.0 (EFL-1.0)
  * Lucent Public License ("Plan9"), version 1.0  * (LPL-1.0)
  * Mozilla Public License 1.0 (MPL-1.0)
  * Mozilla Public License 1.1 (MPL-1.1)
  * Open Software License 1.0 (OSL-1.0)
  * Open Software License 2.1 (OSL-2.1)
  * Reciprocal Public License, version 1.1 (RPL-1.1)
  
## Annex B: Recommended Open Source Foundations 
The following foundations have a good track record for managing open source projects and delivering great products.

* Apache Software Foundation
* Document Foundation
* Eclipse Foundation
* Evergreen Community
* iTop Community
* MariaDB Foundation
* Moodle Community
* Mozilla Foundation
* Python Software Foundation
* Redmine Community
* The Elgg Foundation
* The R Foundation
* Wikimedia Foundation
* WordPress Foundation

## Other Notes

### Open Resource Exchange

Add all open source software your department or agency is using to the [Open Source Software section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/en/open-source-software.html).

Instructions on how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/blob/master/_data/README.md).


## References

<!-- References -->
[guide-contribute-oss]: contributing-to-open-source-software.md
[guide-publish-oss]: publishing-open-source-code.md
