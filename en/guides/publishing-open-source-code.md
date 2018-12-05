# Guides for Publishing Open Source Code

> Note: Source code should be released as early as possible in the project's lifecycle to avoid the overhead downstream.

## Approvals

Similar to open data or information covered by the Open Government Directive, the release of open source code under open source software (OSS) licences, requires appropriate department or agency approvals.
Currently this is assumed to be the Assistant Deputy Minister (ADM), or any other person named by the ADM, (because of the assignment of rights by an open source software licence) and the Information Management Senior Official (IMSO) of departments and agencies (like open information).

## Intellectual Property

### Copyright

The [Ownership of Copyright](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that where any work is, or has been, prepared or published by or under the direction or control of Her Majesty or any government department, the copyright in the work shall, subject to any agreement with the author, belong to Her Majesty.  This applies to source code.

However, Government of Canada employees have [Moral Rights](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-8) and as the author of a work has the right to the integrity of the work and the right to be associated with the work as its author by name or under a pseudonym and the right to remain anonymous.

#### Identify yourself as an employee of the Government of Canada

Use your full name and Government of Canada email address for your code contributions.

#### Appropriate Government of Canada Copyright Identification

Copyright (c) Her Majesty the Queen in Right of Canada, as represented by the Minister of (legal departmental name), (year of publication).

### Licencing

The [Ownership of Copyright, Assignments and Licences](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that the owner of the copyright in any work may assign the right and may grant any interest in the right by licence.
However no assignment or grant is valid unless it is in writing signed by the owner of the right in respect of which the assignment or grant is made, or by the owner’s duly authorized agent, currently assumed to be the ADM.

#### Choosing an open source software licence

* When the project is part of a larger Open Source ecosystem, use the license which is usually used in this ecosystem.
* Make sure that the outbound rights associated with the licence selected do not exceed inbound rights of any software components used in the source code; e.g.: it would not be possible to release a project under an MIT licence (permissive) if software components used within it were originally released under GPL3 (reciprocal).
* If multiple licences can be applied, choose a licence which matches the goal of the project and its interactions with other projects: this tends to revolve around the decision of whether to apply a permissive or reciprocal licence and the degree to which .

##### Permissive licences

Why choose a permissive licence?

* Maximizes the scope of downstream users and has a broad appeal to the entire private sector.
  * In essence, this means greater flexibility for end users, developers and companies to reuse the software as they see fit, including as part of commercial software.

Recommended permissive licences for Government of Canada open source code are:

* [MIT](https://opensource.org/licenses/MIT)
* [Apache 2.0](https://opensource.org/licenses/Apache-2.0)

If your project would like to use another permissive licence, please contact the Open Source Advisory Board.

##### Reciprocal licences

Why choose a reciprocal licence?

* Appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains free and open source software.
* It can also put a focus on benefiting other private-sector businesses that provide services and support.

Recommended reciprocal licences for Government of Canada open source code are:

* [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)
* [LGPL 3.0](https://www.gnu.org/licenses/lgpl-3.0.en.html)
* [AGPL 3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)

If your project would like to use another reciprocal licence, please contact the Open Source Advisory Board.

## Source code repositories

Recommended public source code repositories for Government of Canada open source code are:

* [GitLab](https://gitlab.com/)
* [GitHub](https://github.com/)
* [framagit](https://framagit.org/)
* [Bitbucket](https://bitbucket.org/)

The Government of Canada also has an internal source code repository available to all departments and agencies.

* [GCcode](#link)

## Mandatory files

Before publishing your source code, it must include:

* a LICENCE (see Licencing above) file containint a copy of the licence under under which the source code is released;
* a README.md file providing information about the project, how to use it and general documentation about the project.

It should also include:

* a CONTRIBUTING.md file explaining how to contribute to the project.

You can find examples of these files in the [Template repository](https://github.com/gctools-outilsgc/template-gabarit).

## Contributor License Agreement

Government of Canada projects dont use contributor agreements, but rely on the open source software licenses providing the necessary terms.
This means that contributions are made under the same license under which the project is released.

## Codes of Conduct

Although technical in nature, the open source software community is first and foremost about people. Treat other people with respect. Be kind, be open, respect the culture of the community you are interacting with and be aware of the diversity of people in that community. Be aware that, particularly in electronic communication, you might misunderstand or misinterpret what others are saying or meaning. The reverse is also true.

Follow any codes of conduct and set a high bar for your own behaviour. You are working in the open.

## Open Resource Exchange

Add a link to your source code repository on the [Open Source Code section on the Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-code.html).

Instructions for how to update the data can be found on [GitHub](https://github.com/canada-ca/ore-ero/tree/master/_data).
