# GC Standard on Open Source Code Contribution (DRAFT)

## Questions to be clarified

* What current laws or policies supports/hinders/needs clarification to contribute open source code?
* Any law or policy regarding the source code being administrative documents that are communicable and reusable?

## Effective date

This standard takes effect on July 1, 2018.

## Scope

All new source code created or modified, whether developed internally by GC employees or through negotiated contracts on behalf of the GC

## Objectives

* Set the standards and best practices for opening source code
* Publish as open source all new source code created or modified, whether developed internally by GC employees or through negotiated contracts on behalf of the GC
* Support and be an active contributor (code, issues, testing, roadmap, ..) to OSS used by the GC and/or where there is benefit to Canadians
* Encourage contributions to OSS released by the GC, whether it be code, commentary, bug reports, feature requests, or overall strategic direction

## Expected results

* Benefit from other developers and communities collaborating on the software, including those outside of government
* Help ensure the viability and perreniality of a project into the future
* Support an Open Government - Open by default approach
* Improving the overall availability of re-usable technology in society and within government
* Support and increase collaboration with other public administrations in Canada and around the world

## Requirements

### Managers, functional specialists, and equivalents responsible for developing or overseeing development of source code are responsible for

- Ensuring that the source code does not contain [Protected Information](#protected-information), by:
  - Keeping sensitive data such as credentials secure and separate from source code
  - Not storing keys and other sensitive material in systems not approved for that purpose
  - Doing code reviews to increase the likelihood of catching bugs, security vulnerabilities, and reduces the risk of committing sensitive data
  - Implementing controls sufficient to prevent unauthorized or inadvertent changes
- Hosting the source code publicly in an open internet [Source Code Repository](#source-code-repository)
- Keeping track of changes using a version control system
- Using an [Open Source Initiative approved licence](open-source-initiative-approved-licence)
- Offering users a mechanism to report bugs and issues, and being responsive to these reports
- Ensuring that documentation related to the project are available in both official languages: English and French
- Registered the project in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/)

### The senior departmental official, designated by the deputy head, is responsible for

- Overseeing the implementation of this standard in their department by granting authorization to contribute to third-party OSS projects and to publish new projects as OSS.

### The departmental Chief Information Officer (CIO) or equivalent is responsible for

- Ensuring that all new source developped by or on behalf of the department meets the requirements or are modifiable to enable them to meet these requirements.

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

Treasury Board of Canada Secretariat will review this standard and its effectiveness at the five-year mark from the effective date of the standard (or earlier if warranted).

## Consequences

In instances of non-compliance, deputy heads are responsible for taking corrective measures, within their organization with those responsible for implementing the requirements of this standard.

Consequences of non-compliance with this standard can include any measure allowed by the Financial Administration Act that the Treasury Board would determine as appropriate and acceptable in the circumstances.

Potential corrective actions, including consequences, are included in Appendix C and align with the Framework for the Management of Compliance.

## Roles and responsibilities of government organizations

### Treasury Board of Canada Secretariat (Chief Information Officer Branch), in consultation with other departments, is responsible for the following

- Developing standards, guidelines, and tools, and providing interpretive advice and guidance on these instruments;
- Communicating and engaging the government-wide Web community on the plans, progress, risks and challenges associated with implementing this standard and its supporting instruments in the federal government; and
- Poviding support to the CIO Council and other committees and working groups, as necessary, to address government-wide challenges and opportunities related to implementing this standard and its supporting instruments.
- Publishing and maintaining the list of exclusions from specific requirements.

## Definitions

### Approved Licence

You should publish your code under an [Open Source Initiative approved licence](https://opensource.org/licenses).

You will not always have a choice as to which licence you apply. Where a reciprocal licence obligation is in force, you need to license your code under the same licence - see the section on [Managing Licence Obligations](9_Annex_Legal.md#managing-licence-obligations). As well, even if you are not under a strict legal obligation to apply a particular licence, you may still wish to adopt the same licence as an existing software project or community in order to become involved with it.

Where you distribute a project consisting entirely of your own code, or consisting of your own code along with permissively-licenced code and code which does not engage reciprocal obligations, you can choose the OSS licence yourself. The licence you choose should reflect your business requirements. All common OSS licences can be adopted for works by government, industry, or the education sector - you need to look at particular project aims.

Choosing an appropriate licence tends to revolve around the decision of whether to apply a reciprocal or permissive licence:

- Permissive licences maximize the scope of downstream users (with broad appeal to the entire private sector); while
- Reciprocal licences are appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains open and free. Reciprocal licences can also put a focus on benefiting other private-sector businesses that provide services and support.

The following chart details other key differences in this decision and list example licences:

|                                          | Permissive | Reciprocal |
| ---------------------------------------- | ---------- | ---------- |
| **Beneficiaries of the OSS release**         | Everyone: commercial software vendors, support services, etc. | Everyone, but only where they are willing to release their software as OSS, under the same licensing terms as were granted to them. |
| **Beneficiaries of downstream code changes** | The whole community, but only where the business (or other developer) chooses to contribute modifications back under the permissive licence. | The whole community in every case where a business, organization, or individual distributes the modifications, as the licence then mandates releasing the changes under the same OSS licence. |
| **Licence complexity**                       | Often very simple and understandable. | Relatively complex, requiring careful legal analysis (and some risk of misinterpretation). |
| **Interoperability**                         | Permissively-licenced code can be included in projects under reciprocal licences, other permissive licences, or closed-source licences. | Reciprocal-licenced code cannot generally be included in a project under any other single licence. |
| **Example licences**                         | MIT, Apache 2.0 | GPL 3.0, AGPL 3.0, LGPL 3.0 |

[Choosealicence.com](https://choosealicense.com/) simplifies the process of selecting an OSS licence by presenting definitions of the most widely used licenses.

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

### Source Code Repository

Examples of open Internet source code repiositories, include, but are not limited to:

- Gitlab
- Github
- Bitbucket
- Framagit
- SourceForge
