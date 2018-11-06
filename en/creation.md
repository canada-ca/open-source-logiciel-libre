# Government of Canada Standard on Open Source Software Creation (DRAFT)

> Notice: The Standard format has been used to help drive the discussion around the requirements to open source code and support open source projects. The content of this document may reside elsewhere than in a Standard. As such, not all sections of a Standard will be kept at this time.

## Scope

These requirements apply to:

* All new [Source Code](#source-code) created or modified, whether developed internally by the Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.

A list of exclusions is attached in the [Exceptions](#exceptions) section.

## Objectives

* Set the standards and best practices for contributing to open source projects
* Encourage the publishing as open source of new source code created or modified, whether developed internally by Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.
* Support and be an active contributor to open source software used by the Government of Canada and/or where there is benefit to Canadians
* Improving the overall availability of re-usable technology within government and society
* Support and increase collaboration with other public administrations in Canada and around the world

## Expected results

* Increase the number of Government of Canada projects released as open source.
* Increase the number of Government of Canada contributions to third party open source software.

## Requirements

### Release all Government of Canada projects as open source code

* Source code must be released and hosted in a public [Source Code Repository](#source-code-repository)
* Source code must be registered in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/).
* Source code publicly released must use an [Open Source Initiative approved licence](open-source-initiative-approved-licence). Considerations as to how to determine appropriate licence provided in Annex. ([Whitepaper](https://github.com/canada-ca/Open_First_Whitepaper), decision tree)
  * The Crown Copyright must be clearly identified in the project documentation.
  * The licence must be clearly identified in the project repository.
* Changes to source code must be tracked using a [Version Control System](#version-control-system) and approved by a Government of Canada Project Maintainer.
* Source code acquired through contracting vehicules when hiring professional services must require the intellectual property to be acquired as Crown Copyright or contract must stipulate that the source code will be released under the project licence.
* The project documentation must clearly identify how the community can contribute.

## Exceptions

*To be defined*
Examples:

* Code being tested, experimented with and is disposable, not bringing value to Government or Canadians.
* Software deemed of National security value.
* Code related to unreleased policy or law.
* Code for a software that is going to be used to generate revenue for authorized department.
* Explaining and documenting why a project is not released if it has been deemed not having a benefit to Canadians.

## Definitions

### Approved Licence

You should publish your code under an [Open Source Initiative approved licence](https://opensource.org/licenses).

Where you distribute a project consisting entirely of your own code, or consisting of your own code along with permissively-licenced code and code which does not engage reciprocal obligations, you can choose the open source software licence yourself. The licence you choose should reflect your business requirements. All common open source software licences can be adopted for works by government, industry, or the education sector - you need to look at particular project aims.

Choosing an appropriate licence tends to revolve around the decision of whether to apply a reciprocal or permissive licence:

* Permissive licences maximize the scope of downstream users (with broad appeal to the entire private sector); while
* Reciprocal licences are appropriate in cases where it is important to receive back downstream changes, or where it is important to ensure that work built on an initial investment remains open and free. Reciprocal licences can also put a focus on benefiting other private-sector businesses that provide services and support.

[Choosealicence.com](https://choosealicense.com/) simplifies the process of selecting an open source software licence by presenting definitions of the most widely used licenses.

### Intellectual Property

Crown copyright act implications... All code produced by civil servants is automatically covered by Crown Copyright. (See questions to be clarified)

### Protected Information

The Treasury Board [Directive on Departmental Security Management (DDSM)](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=16579) defines protected information as one that "may qualify for an exemption or exclusion under the Access to Information Act or the Privacy Act because its disclosure would reasonably be expected to compromise the non-national interest."

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

The preferred approach is to use a [Distributed Version Control System (DVCS)](#distributed-version-control-system) in order to ...

#### Distributed Version Control System

A distributed version control system provides the flexibility of multiple collaborators and teams working ...

Examples of DVCS include, but are not limited to Git & Mercurial.

#### Centralized Version Control System

A centralized Version Control System may be used but...

CVS are considered deprecated.
