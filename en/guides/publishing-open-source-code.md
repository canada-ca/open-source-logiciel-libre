# Guide for Publishing Open Source Code (Draft)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the [Procedures for Application Architecture](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8) provide that, all source code must be released under an appropriate open source software license, and when not, it must be shared within the Government of Canada.

> **All source code, whether developed in-house by GC or through procurement contracts, must be published under an appropriate open source software licence.**
> **When unable to publish source code publicly, it must be shared within the Government of Canada.**

The steps to publish GC source code are:

1. [Seek Approvals](#seek-approvals)
2. [Obtain Rights to Custom Code in Contracts](#obtain-rights-to-custom-code-in-contracts)
3. [Consider Security Implications](#consider-security-implications)
4. [Select Open Source Software Licence](#select-open-source-software-licence)
5. [Select Source Code Repository](#select-source-code-repository)
6. [Add Mandatory Files](#add-mandatory-files)
7. [Publishing a Legacy Application](#publishing-a-legacy-application)
8. [Work in the Open](#work-in-the-open)
9. [Other notes](#other-notes)

## Seek Approvals

### Team

The updates to the Directive on Management of IT clearly states that working in the open is the way forward. 
Aligned with the Open Government vision, teams should by default consider adapting their process to develop as open source from the inception of projects to reduce the overhead required to release their source code later down the road.

### Department

Similar to open data or information covered by the [Directive on Open Government](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28108), the publication of source code under an open source software licence, requires appropriate department or agency approvals.
Because of the required assignment of rights by an open source software licence, the Assistant Deputy Minister (ADM), or any other person named by the ADM is responsible for approving the releases of open source code.

**Note:** Delegation to the Information Management Senior Official (IMSO) of departments and agencies (like open information) should be considered.

## Obtain Rights to Custom Code in Contracts 

The ISED [Policy on Title to Intellectual Property Arising Under Crown Procurement Contracts](https://www.ic.gc.ca/eic/site/068.nsf/eng/00005.html) provides that the contractor is to own the rights to foreground intellectual property (IP) created as a result of a Crown procurement contract.
But when the Crown's intended use of the IP can be met through licence arrangements, it has the opportunity to seek the needed licence(s) whether broad or narrow.

The PSPC [Standard Acquisition Clauses and Conditions Manual](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual) provides clauses to request a [License to Material Subject to Copyright](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual/5/K/K3030C/2).
Use the clauses in contracts if the department or agency wants the copyright in the work to belong to the contractor but wishes to obtain a license to exercise all rights comprised in the copyright.

**Departments or agencies are able to release code developed as a result of a Crown procurement contract under an open source software licence.**
**The contract can also ask the the contracting body be responsible for publishing the source code under an acceptable open source software licence or contribute directly to existing open source software using that project's licence.**

## Consider Security Implications

### Classification of source code

The Treasury Board [Directive on Departmental Security Management](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=16579) defines protected information as one that "may qualify for an exemption or exclusion under the [Access to Information Act](http://laws-lois.justice.gc.ca/eng/acts/A-1/) because its disclosure would reasonably be expected to compromise the non-national interest".

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

It is highly unlikely that developers would intentionally include such information in their source code. As a result, source code is considered unclassified unless the developer has included, inadvertently or otherwise, information that falls under the [exemptions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-3.html#h-10) and [exclusions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-10.html#h-29) of the [Access to Information Act](http://laws-lois.justice.gc.ca/eng/acts/A-1/) as listed above. Where feasible, this information should be removed from the source code to increase the ability for code to be shared.

### Developing Software in the Open

- Keep sensitive data such as credentials secure and separate from source code.
- Avoid storing keys and other sensitive material in systems not approved for that purpose.
- Code reviews increase the likelihood of catching bugs, security vulnerabilities, and reduces the risk of committing sensitive data.
- Implement controls sufficient to prevent unauthorized or inadvertent changes such as code signing and repository user rights.

## Select Open Source Software Licence

When the project is part of a larger open source software community, like plugins, modules, extensions or derivative works of existing open source software, use the license which is usually used by the community.

Recommended permissive licences are:

|                                          | MIT | Apache 2.0 |
| ---------------------------------------- | --- | ---------- |
| **When to use** | Small, simple projects and scripts. | Larger software project use Apache 2.0 because it provides a grant of patents. |
| **Licence text** | https://opensource.org/licenses/MIT | http://www.apache.org/licenses/LICENSE-2.0.txt |

Recommended reciprocal licences are:

|                                          | GPL 3.0 | LGPL 3.0 | AGPL 3.0 |
| ---------------------------------------- | ------- | -------- | -------- |
| **When to use** | Software | Libraries | Web applications and services |
| **Licence text** | https://www.gnu.org/licenses/gpl-3.0.txt | https://www.gnu.org/licenses/lgpl-3.0.txt | https://www.gnu.org/licenses/agpl-3.0.txt |

To apply to source code, add the text of the chosen licence to a LICENSE.txt file in the root folder of the project. See [Add Mandatory Files](#add-mandatory-files).

If multiple licences can be applied, choose a licence which matches the goal of the project and its interactions with other projects. This tends to revolve around the decision of whether to apply a permissive or reciprocal licence.

The following chart details other key differences in this decision:

|                                          | Permissive | Reciprocal |
| ---------------------------------------- | ---------- | ---------- |
| **Beneficiaries of the OSS release** | Everyone: maximizes the scope of downstream users and has a broad appeal to the entire private sector... greater flexibility for end users, developers and companies to reuse the software as they see fit, including as part of commercial software. | Everyone: but only where they are willing to release their software under the same licensing terms that were granted to them. Appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains free and open source software... can also put a focus on benefiting other private-sector businesses that provide services and support. |
| **Beneficiaries of downstream code changes** | The whole community, but only where the business, organization, or individual developer chooses to contribute modifications back under the permissive licence. | The whole community in every case where a business, organization, or individual developer distributes the modifications or contribute modifications back under the reciprocal licence. |
| **Licence complexity** | Often short, simple and understandable (for example, MIT). | Relatively long and complex legal jargon (for example AGPL 3.0). |
| **Interoperability** | Permissively-licenced code can be included in projects under reciprocal licences, other permissive licences, or closed-source licences. | Reciprocal-licenced code cannot generally be included in a project under any other single licence. |

The differences amongst the GPL suite of reciprocal licences illustrate how the type of distribution and extent of integration interact to determine when a reciprocal obligation engages, as shown in the following table.

|            | **Derivative work of the original** | **Derivative work, but only links to original** | **Collection, including the unchanged original** |
| ---------- | ---------- | ---------- | ---------- |
| **Distribution of source code** | GPLv3: **Yes**<br/>LGPLv3: **Yes**<br/>AGPLv3: **Yes** | GPLv3: **Yes**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **No** |
| **Provision of access over a computer network** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **No** |

### Outbound Rights

Make sure that the outbound rights associated with the licence selected do not exceed inbound rights of any software components used in the source code; e.g.: it would not be possible to release a project under an MIT licence (permissive) if software components used within it were originally released under GPL3 (reciprocal).

### Appropriate Government of Canada Copyright Identification

**Use the following structure when applying the Government of Canada Copyright notice.**

> Copyright (c) Her Majesty the Queen in Right of Canada, as represented by the Minister of (legal departmental name), (year of publication).

Replace the **(legal departmental name)** and **(year of publication)** with the appropriate information.

## Select Source Code Repository

Recommended public source code repositories for Government of Canada open source code are:

- [GitLab](https://gitlab.com/)
- [GitHub](https://github.com/)
- [framagit](https://framagit.org/)
- [Bitbucket](https://bitbucket.org/)

The Government of Canada also has an internal source code repository available to all departments and agencies.

- [GCcode](https://gccode.ssc-spc.gc.ca/) (internal to Government of Canada only)

### Organizations

Departments and agencies are free to choose the platform that best suites their operational needs but their projects should, where possible, all be regrouped under a unique organization or group.

### Project and Repository Names

Projects names should be bilingual but repositories names can be unilingual or use acronyms.

## Add Mandatory Files

Before publishing, source code must include the following file to be considered as open source:

- a `LICENCE` (see [Select Open Source Software Licence](#select-open-source-software-licence)) file containing a copy of the licence under under which the source code is released;

By default, such a project would only be released under the Crown Copyright.

Additionally, the following are highly recommended as best practice:

- a `README.md` file providing bilingual information about the project, how to use it and general documentation.
- a `CONTRIBUTING.md` file explaining how to contribute to the project.
- a `SECURITY.md` file explaining security policy as well as procedures for reporting security vulnerabilities.

Examples of these files are available in the [Template Repository](https://github.com/canada-ca/template-gabarit).

## Publishing a Legacy Application

Publishing a legacy application can seem like a lot of work but it is feasible and actually a good investment if the application will continue to be used in the future.
Documentation could be improved during the release project to help increase community contributions.

Additionally, releasing a legacy application may lead to reuse and increase in development contributions from interested parties.
It may revive the active development of the application, providing it with enhanced features and bug fixes.

Vulnerability risks already exist and releasing it as open source doesn't change their state.
One way of limiting those risks is to not provide the configurations of the production version.

On the other end, if it's a web application and the worry is to expose specific vulnerabilities, it should be mitigated no matter if it's released as open source or not as those exposed services could already be exploited.

Scanning tools with advanced functionalities and security tests should be considered to help the development teams speed up the review and clean up process.

## Work in the Open

### Release Early, Release Often

Source code should be released as early as possible in the project's life cycle to avoid the overhead of publishing source code late in the process.
The public source code repository should be the single source of truth where developers are working.
The latest code version may not necessarily mean it's the version deployed in production.

### Identify as an employee of the Government of Canada

Employees should use their full name and Government of Canada email address for all code contributions to public repositories while acting within the scope of their duties or employment.

### Community

Building a welcoming community can influence your project's future and reputation.
Provide a positive experience for contributors and make it easy so they keep coming back.
Respond to questions, bugs and merge requests.

Include a `README.md` and `CONTRIBUTING.md` file with your source code.
See [Add Mandatory files](#add-mandatory-files).

#### Contributor License Agreement

Government of Canada projects don't require contributor license agreements, but rely on the open source software licenses providing the necessary terms.
Contributions are made under the same license under which the project is released and that authors retain their copyright for their contributions.

#### Open Resource Exchange

Add a link to your source code repository on the [Open Source Code section of the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-code.html).

Instructions for how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

## Other notes

### Copyright

The [Ownership of Copyright](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that where any work is, or has been, prepared or published by or under the direction or control of Her Majesty or any government department, the copyright in the work shall, subject to any agreement with the author, belong to Her Majesty.
This applies to source code developed by Government of Canada employees.

However, Government of Canada employees have [Moral Rights](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-8) and as the author of a work has the right to the integrity of the work and the right to be associated with the work as its author by name or under a pseudonym and the right to remain anonymous.

### Official languages

Source code is exempt (including inline comments) of the provisions of the [Policy on Official Languages](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=26160).

Documentation (not in source code files) should however be bilingual?

Depends whether an open source project is considered under Language of work (6.3) or Communications with the public (6.2)
