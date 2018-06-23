# Government of Canada Standard on Open Source Code Contribution (DRAFT)

## Questions to be clarified

* What current laws or policies support/hinder/need clarification to contribute open source code?
* Any law or policy regarding the source code being administrative documents that are communicable and reusable?

## Effective date

This standard takes effect on [Month Day, Year].

## Scope

All new [Source Code](#source-code) created or modified, whether developed internally by Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.

For the opening of existing source codes, additional actions will be needed, such as defining the scope, reviewing quality and security, and ensuring compliance specifically on intellectual property.

A list of exclusions is attached in the [Exceptions](#exceptions) section.

## Objectives

* Set the standards and best practices for contributing to open source projects
* Encourage the publishing as open source of new source code created or modified, whether developed internally by Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.
* Encourage the release of existing Government of Canada source code as open source software projects.
* Encourage contributions to open source software projects released by the Government of Canada
* Support and be an active contributor to open source software used by the Government of Canada and/or where there is benefit to Canadians

## Expected results

* Improving the overall availability of re-usable technology within government and society
* Support and increase collaboration with other public administrations in Canada and around the world
* Support an Open Government - Open by default approach
* Help ensure the viability and perreniality of a Government of Canada project into the future
* Benefit from other developers and communities collaborating on the software, including those outside of government

## Requirements

### Managers, functional specialists, and equivalents responsible for developing or overseeing development of source code are responsible for

#### Encouraging and supporting the release of Government of Canada projects as open source software where there is benefit to Canadians.

- Hosting the source code publicly in an open internet [Source Code Repository](#source-code-repository)
- Ensuring that the rights required to open the project source code are acquired through the contracting vehicules when hiring professional services. (IP+licence)
- Using an [Open Source Initiative approved licence](open-source-initiative-approved-licence)
- Keeping track of changes using a modern [Version Control System](#version-control-system).
- Offering users a mechanism to report bugs and issues, *and being responsive to these reports*
- Ensuring that documentation related to the project are available in both official languages: English and French
- Registering the project in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/)
- Explaining and documenting why a project is not released if it has been deemed not having a benefit to Canadians.

#### Encouraging and supporting internal contributions to third-party open source software projects used by the Government of Canada and/or where there is benefit to Canadians

- Contributing code, issues, testing, roadmap to open source software projects
- Supporting open source software initiatives and foundations to help ensure that critical code for modern technologies are monitored and supported

#### Ensuring that the source code does not contain [Protected Information](#protected-information)

- Keeping sensitive data such as credentials secure and separate from source code
- Not storing keys and other sensitive material in systems not approved for that purpose
- Doing code reviews to increase the likelihood of catching bugs, security vulnerabilities, and reduces the risk of committing sensitive data
- Implementing controls sufficient to prevent unauthorized or inadvertent changes

### The senior departmental official, designated by the deputy head, is responsible for

- Overseeing the implementation of this standard in their department by granting authorization to contribute to third-party open source software projects and to publish new projects as open source software, subject to legislation (Crown Copyright Act, etc.) and exception list.

### The departmental Chief Information Officer (CIO) or equivalent is responsible for

- Ensuring that all new or modified source code developped by or on behalf of the department meets the requirements or are modifiable to enable them to meet these requirements. *Needs revision*

## Monitoring and reporting requirements are as follows

### Deputy heads

Deputy heads are responsible for monitoring adherence to this standard within their departments, consistent with the provisions of the Treasury Board's Policy on Evaluation, and Policy on Internal Audit, and for ensuring that appropriate remedial action is taken to address any deficiencies within their departments.

### Senior departmental official

The senior departmental official, designated by the deputy head, is responsible for supporting their deputy head by overseeing the implementation and monitoring of this standard in their department, bringing to the deputy head's attention any significant difficulties, gaps in performance or compliance issues and developing proposals to address them, and reporting significant performance or compliance issues to the Chief Information Officer Branch of Treasury Board of Canada Secretariat.

### Government-wide

The Treasury Board of Canada Secretariat will monitor compliance with this standard in a variety of ways, including but not limited to, the following:

- assessments under the Management Accountability Framework;
- examinations of Treasury Board submissions, departmental performance reports, results of audits, evaluations and studies; and
- work performed in collaboration with departments.
- *Application Portfolion Management review process?*

Treasury Board of Canada Secretariat will review this standard and its effectiveness at the five-year mark from the effective date of the standard (or earlier if warranted).

## Consequences

In instances of non-compliance, deputy heads are responsible for taking corrective measures, within their organization with those responsible for implementing the requirements of this standard.

Consequences of non-compliance with this standard can include any measure allowed by the Financial Administration Act that the Treasury Board would determine as appropriate and acceptable in the circumstances.

## Roles and responsibilities of government organizations

### Treasury Board of Canada Secretariat (Chief Information Officer Branch), in consultation with other departments, is responsible for the following

- Developing standards, guidelines, and tools, and providing interpretive advice and guidance on these instruments;
- Communicating and engaging the government-wide Web community on the plans, progress, risks and challenges associated with implementing this standard and its supporting instruments in the federal government; and
- Poviding support to the CIO Council and other committees and working groups, as necessary, to address government-wide challenges and opportunities related to implementing this standard and its supporting instruments.
- Publishing and maintaining the list of exclusions from specific requirements.

## Exceptions

asdf

## Definitions

### Approved Licence

You should publish your code under an [Open Source Initiative approved licence](https://opensource.org/licenses).

When contributing to external open source software, the choice of the licence must comply with the existing licence of the project. Where a reciprocal licence obligation is in force, you need to license your code under the same licence. As well, even if you are not under a strict legal obligation to apply a particular licence, you may still wish to adopt the same licence as an existing software project or community in order to become involved with it.

Where you distribute a project consisting entirely of your own code, or consisting of your own code along with permissively-licenced code and code which does not engage reciprocal obligations, you can choose the open source software licence yourself. The licence you choose should reflect your business requirements. All common open source software licences can be adopted for works by government, industry, or the education sector - you need to look at particular project aims.

Choosing an appropriate licence tends to revolve around the decision of whether to apply a reciprocal or permissive licence:

- Permissive licences maximize the scope of downstream users (with broad appeal to the entire private sector); while
- Reciprocal licences are appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains open and free. Reciprocal licences can also put a focus on benefiting other private-sector businesses that provide services and support.

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

- Information obtained in confidence
- Information about federal-provincial affairs
- Information about international affairs and defence
- Information about law enforcement and investigations
- Information about the safety of individuals
- Information about the economic interests of Canada
- Personal information
- Third party information
- Advice about certain aspects of operations of government
- Information about testing procedures, tests, and audits
- Information that is subject to solicitor-client privilege
- Information that is subject to statutory prohibitions
- Certain types of information held by the Canadian Broadcasting Corporation and Atomic Energy of Canada Limited
- Confidences of the Queen’s Privy Council for Canada

It is highly unlikely that developers would intentionally include such information in their source code. As a result, the proposed categorization for the confidentiality of source code is considered unclassified unless the developer has included, inadvertently or otherwise, information that falls under the [exemptions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-3.html#h-10) and [exclusions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-10.html#h-29) of the [Access to Information Act](http://laws-lois.justice.gc.ca/eng/acts/A-1/) as listed above. Where feasible, this information should be removed from the source code to increase the ability for code to be shared.

Some security considerations to keep in mind when developing software:

### Source Code

Source code may include, but are not limited to, code written for software projects, modules, plugins, scripts, middleware, and APIs; it does not, however, include code that is truly exploratory or disposable in nature, such as that written by a developer experimenting with a new language or library.

### Source Code Repository

Examples of open Internet source code repiositories, include, but are not limited to:

- Gitlab
- Github
- Bitbucket
- Framagit
- SourceForge

### Version Control System

A version control system provides the ability to maintain a full history of changes applied to the codebase so that...

The preferred approach is to use a [Distributed Version Control System](#distributed-version-control-system) in order to ...

#### Distributed Version Control System

A distributed version control system provides the flexibility of multiple collaborators and teams working ...

Examples of dcvs include, but are not limited to:

- Git
- Mercurial
- Etc.

#### Centralized Version Control System

A centralized Version Control System may be used but...

CVS are considered deprecated.
