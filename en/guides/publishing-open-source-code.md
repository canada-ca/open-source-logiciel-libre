# Guides for Publishing Open Source Code

* [Release Early, Release Often, Work in the Open](#release-early-release-often-work-in-the-open)
* [Working in the Open](working-in-the-open)
* [Mandatory files](#mandatory-files)
* [Intellectual Property](#intellectual-property)
  * [Licencing](#licencing)
* [Source code repositories](#source-code-repositories)
  * [Two Factor Authentication](#two-factor-authentication)
  * [Organizations](#organizations)
* [Open Resource Exchange](#open-resource-exchange)
* [Official languages](#official-languages)
  * [Project and Repository Names](#project-and-repository-names)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C provides mandatory procedures for enterprise architecture assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the procedures for Application Architecture provide that, all source code must be released under an appropriate open source software license when appropriate, and when not, shared within the Government of Canada.

**note:** Custom developed code must be published or shared back with existing open source software communities.
This will make the resulting solutions available for reuse by everyone, including departments and agencies as well as Canadian businesses and citizens.

## Release Early, Release Often, Work in the Open

Source code should be released as early as possible in the project's life cycle to avoid the overhead of publishing source code late in the process.
The public source code repository should be the single source of truth where developers are working.

Publishing your code and data from the beginning of your technology project or programme will encourage:

* clearer documentation, making it easier for your team to maintain the code, track changes to it and for other people to use it
* cleaner and well-structured code that is easier to maintain
* processes that will allow you to continuously publish code as it is written
* clarity around data that needs to remain protected and how that's achieved
* suggestions about how the code can be improved or where security can be improved
* others to contribute ideas as the project is in progress

**note:** Prior art in releasing source code helps protecting against patents litigation.
The latest code version may not necessarily mean it's the version deployed in production.

## Working in the Open

Building a welcoming community can influence your project's future and reputation.
Provide a positive experience for contributors and make it easy so they keep coming back.

* README.md and CONTRIBUTING.md file
* Respond to questions, bugs and merge requests for code.

## Intellectual Property

### Licencing

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

### Security Considerations

* Use 2 factor authentication (2FA) to secure accounts.
* Signed and hashed commits

**notes** need to work with Cyber

## Open Resource Exchange

Add a link to your source code repository on the [Open Source Code section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-code.html).

Instructions for how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).

## Official languages

Source code is exempt (including inline comments) of the provisions of the [Policy on Official Languages](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=26160).

Documentation (not in source code files) should however be bilingual?

Depends whether an open source project is considered under Language of work (6.3) or Communications with the public (6.2)

### Project and Repository Names

Projects names should be bilingual but repositories names can be unilingual or use acronyms.
