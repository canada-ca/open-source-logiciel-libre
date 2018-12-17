# Guides for Publishing Open Source Code

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the procedures for Application Architecture provide that, all source code must be released under an appropriate open source software license when appropriate, and when not, shared within the Government of Canada.

**note:** Custom developed code must be published or shared back with existing open source software communities.
This will make the resulting solutions available for reuse by everyone, including departments and agencies as well as Canadian businesses and citizens.

## Approvals

Similar to open data or information covered by the Open Government Directive, the release of open source code under open source software (OSS) licences, requires appropriate department or agency approvals.
Currently this is assumed to be the Assistant Deputy Minister (ADM), or any other person named by the ADM, (because of the assignment of rights by an open source software licence) and the Information Management Senior Official (IMSO) of departments and agencies (like open information).

## Release Early, Release Often, Work in the Open

Source code should be released as early as possible in the project's lifecycle to avoid the overhead of publishing source code late in the process.
The public source code repository should be the single source of truth where developers are working.

Publishing your code and data from the beginning of your technology project or programme will encourage:

* clearer documentation, making it easier for your team to maintain the code, track changes to it and for other people to use it
* cleaner and well-structured code that is easier to maintain
* processes that will allow you to continuously publish code as it is written
* clarity around data that needs to remain protected and how that's achieved
* suggestions about how the code can be improved or where security can be improved
* others to contribute ideas as the project is in progress

**note:** Prior art in releasing source code helps protecting against patents litigation.
The latest code version may not necessarly mean it's the version deployed in production.

## Intellectual Property

### Copyright

The [Ownership of Copyright](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that where any work is, or has been, prepared or published by or under the direction or control of Her Majesty or any government department, the copyright in the work shall, subject to any agreement with the author, belong to Her Majesty.  This applies to source code developed by Government of Canada employees.

However, Government of Canada employees have [Moral Rights](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-8) and as the author of a work has the right to the integrity of the work and the right to be associated with the work as its author by name or under a pseudonym and the right to remain anonymous.

#### Identify yourself as an employee of the Government of Canada

Use full name and Government of Canada email address for all contributions to public communities and repositories.

#### Crown Procurement Contracts

The ISED [Policy on Title to Intellectual Property Arising Under Crown Procurement Contracts](https://www.ic.gc.ca/eic/site/068.nsf/eng/00005.html) provides that the contractor is to own the rights to foreground intellectual property (IP) created as a result of a Crown procurement contract.
But when the Crown's intended use of the IP can be met through licence arrangements, it has the opportunity to seek the needed licence(s) whether broad or narrow.

The PSPC [Standard Acquisition Clauses and Conditions Manual](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual) provides clauses to request a [License to Material Subject to Copyright](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual/5/K/K3030C/2).
Use the clause in contracts if the department or agency wants the copyright in the work to belong to the contractor but wishes to obtain a license to exercise all rights comprised in the copyright.
This would allow the department or agency to release code developped as a result of a Crown procurement contract under an open source software licence.

**note:** Draft clause for OSS permissive licence.
May also request use of TBS exceptions to acquire IP.

#### Appropriate Government of Canada Copyright Identification

Copyright (c) Her Majesty the Queen in Right of Canada, as represented by the Minister of (legal departmental name), (year of publication).

#### Contributor License Agreement

Government of Canada projects dont use contributor license agreements, but rely on the open source software licenses providing the necessary terms.
This means that contributions are made under the same license under which the project is released and that authors retain their copyright for their contributions.

### Licencing

The [Ownership of Copyright, Assignments and Licences](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that the owner of the copyright in any work may assign the right and may grant any interest in the right by licence.
However no assignment or grant is valid unless it is in writing signed by the owner of the right in respect of which the assignment or grant is made, or by the owner’s duly authorized agent, currently assumed to be the ADM. Delegation should be considered to encourage the release of source code under an open source licence as easily as possible.

You need to include a licence with your code before publishing it by adding a LICENCE file with your code.

#### Choosing and using open source software licences

* When the project is part of a larger Open Source ecosystem, use the license which is usually used in this ecosystem.
* Make sure that the outbound rights associated with the licence selected do not exceed inbound rights of any software components used in the source code; e.g.: it would not be possible to release a project under an MIT licence (permissive) if software components used within it were originally released under GPL3 (reciprocal).
* If multiple licences can be applied, choose a licence which matches the goal of the project and its interactions with other projects. This tends to revolve around the decision of whether to apply a permissive or reciprocal licence.

The following chart details other key differences in this decision:

|                                          | Permissive | Reciprocal |
| ---------------------------------------- | ---------- | ---------- |
| **Beneficiaries of the OSS release** | Everyone: maximizes the scope of downstream users and has a broad appeal to the entire private sector... greater flexibility for end users, developers and companies to reuse the software as they see fit, including as part of commercial software. | Everyone: but only where they are willing to release their software under the same licensing terms that were granted to them. Appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains free and open source software... can also put a focus on benefiting other private-sector businesses that provide services and support. |
| **Beneficiaries of downstream code changes** | The whole community, but only where the business, organization, or individual developer chooses to contribute modifications back under the permissive licence. | The whole community in every case where a business, organization, or individual developer distributes the modifications or contribute modifications back under the reciprocal licence. |
| **Licence complexity** | Often short, simple and understandable (for example, MIT). | Relatively long and complex legal jargon (for example AGPL 3.0). |
| **Interoperability** | Permissively-licenced code can be included in projects under reciprocal licences, other permissive licences, or closed-source licences. | Reciprocal-licenced code cannot generally be included in a project under any other single licence. |

##### Permissive licences

Recommended permissive licences for Government of Canada open source code are:

|                                          | MIT | Apache 2.0 |
| ---------------------------------------- | --- | ---------- |
| **When to use** | Small, simple projects and scripts. | For larger software project use Apache 2.0 because it provides a grant of patents. |
| **How to apply to your code** |  |  |
| **Licence text** | https://opensource.org/licenses/MIT | http://www.apache.org/licenses/LICENSE-2.0.txt |

##### Reciprocal licences

Recommended reciprocal licences for Government of Canada open source code are:

|                                          | GPL 3.0 | LGPL 3.0 | AGPL 3.0 |
| ---------------------------------------- | ------- | -------- | -------- |
| **When to use** |  |  |
| **Licence text** | https://www.gnu.org/licenses/gpl-3.0.txt | https://www.gnu.org/licenses/lgpl-3.0.txt | https://www.gnu.org/licenses/agpl-3.0.txt |

The differences amongst the GPL suite illustrate how the type of distribution and extent of integration interact to determine when a reciprocal obligation engages, as shown in the following table.

|            | **Derivative work of the original** | **Derivative work, but only links to original** | **Collection, including the unchanged original** |
| ---------- | ---------- | ---------- | ---------- |
| **Distribution of source code** | GPLv3: **Yes**<br/>LGPLv3: **Yes**<br/>AGPLv3: **Yes** | GPLv3: **Yes**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **No** |
| **Provision of access over a computer network** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **Yes** | GPLv3: **No**<br/>LGPLv3: **No**<br/>AGPLv3: **No** |

## Source code repositories

Recommended public source code repositories for Government of Canada open source code are:

* [GitLab](https://gitlab.com/)
* [GitHub](https://github.com/)
* [framagit](https://framagit.org/)
* [Bitbucket](https://bitbucket.org/)

The Government of Canada also has an internal source code repository available to all departments and agencies.

* [GCcode](https://gccode.ssc-spc.gc.ca/) (internal to Government of Canada only)

### Two Factor Authentication

Use 2 factor authentication (2FA) to secure accounts.

### Organizations

Departments are free to choose the platform that best suites their operational needs but their projects should all be regrouped under a unique organization.

Organizations should be registered in the Open Resource Exchange.

### Repository vs Projects Names

Projects names should be bilingual but repositories names can be unilingual or use acronyms.

## Mandatory files

Before publishing your source code, it must include:

* a LICENCE (see Licencing above) file containint a copy of the licence under under which the source code is released;
* a README.md file providing bilingual information about the project, how to use it and general documentation.

It should also include:

* a CONTRIBUTING.md file explaining how to contribute to the project.
* a SECURITY.md file explaining security policy as well as security vulnerabilities reporting procedures.

You can find some examples of these files in the [Template repository](https://github.com/gctools-outilsgc/template-gabarit).

## Open Resource Exchange

Add a link to your source code repository on the [Open Source Code section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-code.html).

Instructions for how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

## Official languages

Source code is exempt (including inline comments) of the provisions of the [Policy on Official Languages](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=26160).

Documentation (not in source code files) should however be bilingual?

Depends whether an open source project is considered under Language of work (6.3) or Communications with the public (6.2)
