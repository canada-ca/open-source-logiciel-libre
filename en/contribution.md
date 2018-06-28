# Government of Canada Standard on Open Source Code Contribution (DRAFT)

> Notice: The Standard format has been used to help drive the discussion around the requirements to open source code and support open source projects. The content of this document may reside elsewhere than in a Standard. As such, not all sections of a Standard will be kept at this time.

## Questions to be clarified

* What current laws or policies support/hinder/need clarification to contribute open source code?
* Any law or policy regarding the source code being administrative documents that are communicable and reusable?

## Scope

All new [Source Code](#source-code) created or modified, whether developed internally by the Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.

All open source software used by the Government of Canada.

> To discuss: Added the "[and/or used by] Government of Canada" to include in scope third-party projects that do not necessarily generate new code. Thoughts?

> To discuss: Would remove the "new" term from the sentence and manage "existing but not released as OSS" with Exceptions and clause explaining how we will be releasing it.

A list of exclusions is attached in the [Exceptions](#exceptions) section.

## Objectives

* Set the standards and best practices for contributing to open source projects
* Encourage the publishing as open source of new source code created or modified, whether developed internally by Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.
* Encourage the release of existing Government of Canada source code as open source software projects.
* Encourage contributions to open source software projects released by the Government of Canada
* Support and be an active contributor to open source software used by the Government of Canada and/or where there is benefit to Canadians
* Improving the overall availability of re-usable technology within government and society
* Support and increase collaboration with other public administrations in Canada and around the world
* Support an Open Government - Open by default approach

## Expected results

* Help ensure the viability and perreniality of a Government of Canada project into the future
* Benefit from other developers and communities collaborating on the software, including those outside of government

## Requirements

### Release Government of Canada projects as open source software where there is benefit to the Government and to Canadians

* Source code publicly released must be hosted in an open internet and public [Source Code Repository](#source-code-repository)
* Projects must be registered in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/).
* Projects publicly released must use an [Open Source Initiative approved licence](open-source-initiative-approved-licence) for its source code.
* Changes to source code must be tracked using a modern [Version Control System](#version-control-system).
* Source code acquired through contracting vehicules when hiring professional services must require the intellectual property to be acquired under Crown Copyright law.

### Contribute to third-party open source software projects used by the Government of Canada and/or where there is benefit to the Government and Canadians

* Open source software used by Government of Canada must be registered in the Open Resource Exchange (*or APM? already part of the process*) to help identify community of practice. *Thoughts: Could this hinder the use of OSS?) Objective would be to increase awareness of other experts in the GC as well as point of contact to help adoption.*
* Code contributions must be done in accordance to Crown Copyright Law constraints:
  * Employee of the Government of Canada must contribute code only to projects that do not request intellectual property transfer.
  * Contracted professional services can be used to contribute to third-party projects.
    * *Intellectual property can be maintained by the contracted party? (To clarify how this should be defined with Justice)*
  * Use compatible licence to the third-party project.
* Issues and bugs raised must be tracked internally as well as with the third party project issue tracking system. (To ensure that bugs are actually fixed, just like for proprietary software - Could just be an email with bug/issue #)
* Third party open source software testing must be done in compliance of internal security guidelines.
* Results of testing that would provide value to third party project and do not disclose protected information must be shared back.
* Feature requests must be tracked internally and using the third party project management platform.
* Financial support for foundations and initiatives must abide by X rules/laws. (*Can we do this? Why not? Need formal clarification*)

### Ensuring that publicly released source code meets quality and security requirements

* Source code must be peer reviewed.
* Source code must not contain:
  * [Protected Information](#protected-information)
* Government of Canada projects publicly released as open source must:
  * Have controls sufficient to prevent unauthorized or inadvertent changes (project repo settings, might fit under different section)
  * Offer users a mechanism to report bugs and issues.
  * Comply with official languages policies like all other information technology projects, including proprietary solutions projects:
    * Projects resources and budget must be allocated to support:
      * Bilingual graphical user interfaces
      * End-users documentation
    * Exclusions to this clause:
      * Source code
      * Configuration documentation
      * Contributions to third-party projects *(might already be covered due to not being a Government of Canada project but needs to be clear)*

## Exceptions

*To be defined*
Examples:

* Code being tested and is disposable, not bringing value to Government or Canadians.
* Software deemed of National security value.
* Other reasons need explaining and documenting why a project is not released if it has been deemed not having a benefit to Canadians.

## Definitions

### Approved Licence

You should publish your code under an [Open Source Initiative approved licence](https://opensource.org/licenses).

When contributing to external open source software, the choice of the licence must comply with the existing licence of the project. Where a reciprocal licence obligation is in force, you need to license your code under the same licence. As well, even if you are not under a strict legal obligation to apply a particular licence, you may still wish to adopt the same licence as an existing software project or community in order to become involved with it.

Where you distribute a project consisting entirely of your own code, or consisting of your own code along with permissively-licenced code and code which does not engage reciprocal obligations, you can choose the open source software licence yourself. The licence you choose should reflect your business requirements. All common open source software licences can be adopted for works by government, industry, or the education sector - you need to look at particular project aims.

Choosing an appropriate licence tends to revolve around the decision of whether to apply a reciprocal or permissive licence:

* Permissive licences maximize the scope of downstream users (with broad appeal to the entire private sector); while
* Reciprocal licences are appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains open and free. Reciprocal licences can also put a focus on benefiting other private-sector businesses that provide services and support.

The following chart details other key differences in this decision and list example licences:

|                                          | Permissive | Reciprocal |
| ---------------------------------------- | ---------- | ---------- |
| **Beneficiaries of the open source software release**         | Everyone: commercial software vendors, support services, etc. | Everyone, but only where they are willing to release their software as open source software, under the same licensing terms as were granted to them. |
| **Beneficiaries of downstream code changes** | The whole community, but only where the business (or other developer) chooses to contribute modifications back under the permissive licence. | The whole community in every case where a business, organization, or individual distributes the modifications, as the licence then mandates releasing the changes under the same open source software licence. |
| **Licence complexity**                       | Often very simple and understandable. | Relatively complex, requiring careful legal analysis (and some risk of misinterpretation). |
| **Interoperability**                         | Permissively-licenced code can be included in projects under reciprocal licences, other permissive licences, or closed-source licences. | Reciprocal-licenced code cannot generally be included in a project under any other single licence. |
| **Example licences**                         | MIT, Apache 2.0 | GPL 3.0, AGPL 3.0, LGPL 3.0 |

[Choosealicence.com](https://choosealicense.com/) simplifies the process of selecting an open source software licence by presenting definitions of the most widely used licenses.

### Intellectual Property

Crown copyright act implications... All code produced by civil servants is automatically covered by Crown Copyright?

Project requesting transfer of IP to project owners?

### Protected Information

The Treasury Board [Directive on Departmental Security Management (DDSM)](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=16579) defines protected information as one that "may qualify for an exemption or exclusion under the Access to Information Act or the Privacy Act because its disclosure would reasonably be expected to compromise the non-national interest."

In order for source code to potentially be deemed protected, it would have to contain any of the following information:

* Information obtained in confidence
* Information about federal-provincial affairs
* Information about international affairs and defence
* Information about law enforcement and investigations
* Information about the safety of individuals
* Information about the economic interests of Canada
* Personal information
* Third party information
* Advice about certain aspects of operations of government
* Information about testing procedures, tests, and audits
* Information that is subject to solicitor-client privilege
* Information that is subject to statutory prohibitions
* Certain types of information held by the Canadian Broadcasting Corporation and Atomic Energy of Canada Limited
* Confidences of the Queen’s Privy Council for Canada

It is highly unlikely that developers would intentionally include such information in their source code. As a result, the proposed categorization for the confidentiality of source code is considered unclassified unless the developer has included, inadvertently or otherwise, information that falls under the [exemptions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-3.html#h-10) and [exclusions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-10.html#h-29) of the [Access to Information Act](http://laws-lois.justice.gc.ca/eng/acts/A-1/) as listed above. Where feasible, this information should be removed from the source code to increase the ability for code to be shared.

Some security considerations to keep in mind when developing software:

* Tests: Unit testing, regression testing, integration testing, stress testing, etc.
* Testing procedures: Manual inspections, Thread modeling, Pen testing, Name of devices, IP addresses, MAC addresses, etc.
* Audits: Results of tests, logs, etc.

*Clarification required about elements of testing mentioned above as protected information.*

> moved from previous requiremnts

* Keeping sensitive data such as credentials secure and separate from source code
* Not storing keys and other sensitive material in systems not approved for that purpose
* Doing code reviews to increase the likelihood of catching bugs, security vulnerabilities, and reduces the risk of committing sensitive data
* For the opening of existing source codes, additional actions will be needed, such as defining the scope, reviewing quality and security, and ensuring compliance specifically on intellectual property.

### Source Code

Source code is code written in a human readable language for software projects, modules, plugins, scripts, middleware, and APIs; it does not, however, include code documentation.

### Source Code Repository

Examples of open Internet source code repositories, include, but are not limited to:

* Gitlab
* Github
* Bitbucket
* Framagit
* SourceForge

### Version Control System

A version control system provides the ability to maintain a full history of changes applied to the codebase so that...

The preferred approach is to use a [Distributed Version Control System](#distributed-version-control-system) in order to ...

#### Distributed Version Control System

A distributed version control system provides the flexibility of multiple collaborators and teams working ...

Examples of dcvs include, but are not limited to:

* Git
* Mercurial
* Etc.

#### Centralized Version Control System

A centralized Version Control System may be used but...

CVS are considered deprecated.
