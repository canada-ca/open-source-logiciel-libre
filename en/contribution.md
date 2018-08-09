# Government of Canada Standard on Open Source Code Contribution (DRAFT)

> Notice: The Standard format has been used to help drive the discussion around the requirements to open source code and support open source projects. The content of this document may reside elsewhere than in a Standard. As such, not all sections of a Standard will be kept at this time.

## Questions to be clarified

* What are the key legal considerations we need to keep in mind with respect to open source code? For example:
  * What are the legal obligations obligations that would prevent the disclosure of open source code?
  * Is source code subject to ATIP requests?
    * Is source code considered a “document/record” for the law?
    * What are the exclusions that would apply?
  * Can contracted professional services be used to contribute to third-party projects?
  * When choosing a licence, what are the constraints and key considerations (patents?)?
  * Can we provide financial support for foundations and initiatives? (*Can we do this? Why not? Need formal clarification*)
* What are some of the key IP considerations when dealing with Open Source Code?
  * If vendors hold IP, how can we ensure that the GC can provide explainability of system functionality and how outcomes were reached? (i.e. automated decisions?)
  * What patents apply for software developed by the Government of Canada? For example, could it be considered an “Invention”, etc?
  * When contributing to a third-party, some projects require contributors to transfer intellectual property of their work. Can a GoC employee transfer IP of work done as part of their job to third-party project? Contributors Licencing Agreement (IP transfers)
  * Can employees of the Government of Canada  contribute code to projects that do not request intellectual property transfer.
* Specific use cases:
  * When forking a 3rd party open source project, how do I manage Intellectual Property (Copyrights) and Licences:
    * Exemple would be a project that has added a CC on their licence like MIT. Do I keep the CC there, add Crown Copyright for our version? Can I/Should I change the licence? If so, when am I allowed to do so? What are the constraints?

## Scope

These requirements apply to:

* All new [Source Code](#source-code) created or modified, whether developed internally by the Government of Canada employees or on behalf of the Government of Canada, whether through negotiated contracts or community contributions.
* All open source software used by the Government of Canada.

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

### A. Release all Government of Canada projects as open source code

* Source code must be released and hosted in a public [Source Code Repository](#source-code-repository) Examples of open Internet source code repositories, include, but are not limited to: Gitlab, Github, Bitbucket, Framagit, SourceForge
* Source code must be registered in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/).
* Source code publicly released must use an [Open Source Initiative approved licence](open-source-initiative-approved-licence). Considerations as to how to determine appropriate licence provided in Annex. ([Whitepaper](https://github.com/canada-ca/Open_First_Whitepaper)], decision tree)
* Changes to source code must be tracked using a [Version Control System](#version-control-system) and approved by a Government of Canada Project Maintainer.
* Source code acquired through contracting vehicules when hiring professional services must require the intellectual property to be acquired as Crown Copyright.

### B. Contribute to third-party open source software projects used by the Government of Canada and/or where there is benefit to the Government and Canadians

* Third-party open source software used by Government of Canada must be registered in the [Open Resource Exchange](https://canada-ca.github.io/ore-ero/open-source-software.html).
* Code contributions must be done in accordance to Crown Copyright Law constraints.
* Issues, bugs and feature requests should be identified to the third party project through their issue tracking system.

## Exceptions

*To be defined*
Examples:

* Code being tested and is disposable, not bringing value to Government or Canadians.
* Software deemed of National security value.
* Explaining and documenting why a project is not released if it has been deemed not having a benefit to Canadians.

## Definitions

### Approved Licence

You should publish your code under an [Open Source Initiative approved licence](https://opensource.org/licenses).

When contributing to external open source software, the choice of the licence must comply with the existing licence of the project. Where a reciprocal licence obligation is in force, you need to license your code under the same licence. As well, even if you are not under a strict legal obligation to apply a particular licence, you may still wish to adopt the same licence as an existing software project or community in order to become involved with it.

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
