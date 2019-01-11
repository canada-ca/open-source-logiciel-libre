# Standard on publishing open source code (Draft)

[Back to Table of Contents](../../README.md#english-content)

* Authorities
* Objectives and expected results
  * The expected results of this Standard are as follows
* Requirements
  * Exceptions to publications

* Appendix A - Intellectual Property
  * Approvals
  * Copyright
    * Identify as an employee of the Government of Canada
    * Crown Procurement Contracts
  * Appropriate Government of Canada Copyright Identification
  * Contributor License Agreement
  * Licencing
    * Licences

* Appendix B - Source Code Repository
  * Organizations
  * Mandatory Files

## Authorities

This Standard is issued under the authority of section 7 of the [Financial Administration Act](https://laws-lois.justice.gc.ca/eng/acts/f-11/) and pursuant to sections 3 and 6.4.9 of the [Policy on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=12755) and the section C.2.3.8 of the [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8).

This Standard supports the [Policy on Information Management](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=12742) and the [Directive on Open Government](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28108).

## Objectives and expected results

The objective of this directive is to maximize the release of source code, whether developed in-house by departments and agencies or through negotiated contracts, to support transparency, accountability, citizen engagement, and socio-economic benefits through reuse, subject to applicable restrictions associated with privacy, confidentiality, and security.

### The expected results of this directive are as follows

* Canadians are able to find, reuse and contribute to GC software projects and source code to support meaningful engagement with their government.
* Support and increase collaboration between departments, agencies and other public administrations in Canada and around the world, including society as a whole.
* Improve the overall availability and quality of re-usable technology within government and society.

## Requirements

**Managers, functional specialists, and equivalents responsible for enterprise architecure and software procurement and development are responsible for**

Ensuring that Government of Canada source code, whether developed in-house by departments and agencies or through negotiated contracts, is released under an appropriate open source software licence.
See Appendix A.

Ensuring that the Government of Canada source code is released using an open and accessible version control system via a public source code repository.
See Appendix B.

**The senior departmental official, designated by the deputy head, is responsible for**

Overseeing the implementation of this standard in their department and carrying out the activities referred to in Monitoring and Reporting Requirements.

Encouraging personnel to collaborate departmentally and interdepartmentally, to share expertise, and to prioritize reusable components and tools.

**The Chief Information Officer (CIO) of departments and agencies, or any other person named by the CIO, is responsible for the following**

Ensuring that the open source software requirements of this directive are integrated in any new plans for procuring, developing, or modernizing departmental information applications, systems, or solutions in support of the delivery of programs and services.

Encouraging personnel to collaborate departmentally and interdepartmentally, to share expertise, and to prioritize reusable components and tools.

**Centres of Expertise are responsible for**

Serving as the primary point of contact between Treasury Board of Canada Secretariat's Chief Information Officer Branch and their department for questions and communications related to interpretation and implementation of the standards, guidelines and tools.

Participating in the interdepartmental Centres of Expertise forum, chaired by the Treasury Board of Canada Secretariat's Chief Information Officer Branch, to stay current with evolving standards, guidelines and tools.

### Exceptions to publications

* Code that is being tested, experimented with and is disposable.
* Code deemed of National security value.
* Code related to unreleased policy or law.

Such exceptions will require:

* Explaining and documenting why a project is not released as open source.
* Making the source code internally available to the Government as a whole where possible.

## Appendix A - Intellectual Property

### Approvals

Similar to open data or information covered by the [Directive on Open Government](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28108), the release of open source code under open source software licences, requires appropriate department or agency approvals.
Because of the required assignment of rights by an open source software licence, the Assistant Deputy Minister (ADM), or any other person named by the ADM is responsible for approving the releases of open source code. 
Delegation to the Information Management Senior Official (IMSO) of departments and agencies (like open information) should be considered.

**notes** needs to be confirmed + delegation of authority

### Copyright

The [Ownership of Copyright](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that where any work is, or has been, prepared or published by or under the direction or control of Her Majesty or any government department, the copyright in the work shall, subject to any agreement with the author, belong to Her Majesty.
This applies to source code developed by Government of Canada employees.

However, Government of Canada employees have [Moral Rights](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-8) and as the author of a work has the right to the integrity of the work and the right to be associated with the work as its author by name or under a pseudonym and the right to remain anonymous.

#### Identify as an employee of the Government of Canada

Employees must use their full name and Government of Canada email address for all code contributions to public repositories while acting within the scope of their duties or employment.

#### Crown Procurement Contracts

The ISED [Policy on Title to Intellectual Property Arising Under Crown Procurement Contracts](https://www.ic.gc.ca/eic/site/068.nsf/eng/00005.html) provides that the contractor is to own the rights to foreground intellectual property (IP) created as a result of a Crown procurement contract.
But when the Crown's intended use of the IP can be met through licence arrangements, it has the opportunity to seek the needed licence(s) whether broad or narrow.

The PSPC [Standard Acquisition Clauses and Conditions Manual](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual) provides clauses to request a [License to Material Subject to Copyright](https://buyandsell.gc.ca/policy-and-guidelines/standard-acquisition-clauses-and-conditions-manual/5/K/K3030C/2).
Use the clause in contracts if the department or agency wants the copyright in the work to belong to the contractor but wishes to obtain a license to exercise all rights comprised in the copyright.
This would allow the department or agency to release code developed as a result of a Crown procurement contract under an open source software licence.

**note:** Draft clause for OSS permissive licence.
May also request use of TBS exceptions to acquire IP.

#### Appropriate Government of Canada Copyright Identification

Use the following structure when applying the Government of Canada Copyright notice:

> Copyright (c) Her Majesty the Queen in Right of Canada, as represented by the Minister of (legal departmental name), (year of publication).

Replace the **legal departmental name** and **year of publication** by the appropriate information.

#### Contributor License Agreement

Government of Canada projects don't use contributor license agreements, but rely on the open source software licenses providing the necessary terms.
This means that contributions are made under the same license under which the project is released and that authors retain their copyright for their contributions.

**notes** to be confirmed, might be need to clarify that contributors keep their IP but that they guarantee that the code is not copied from somewhere else.

### Licencing

The [Ownership of Copyright, Assignments and Licences](https://laws-lois.justice.gc.ca/eng/acts/c-42/page-4.html#h-7) provides that the owner of the copyright in any work may assign the right and may grant any interest in the right by licence.
However no assignment or grant is valid unless it is in writing signed by the owner of the right in respect of which the assignment or grant is made, or by the owner’s duly authorized agent.

Open source code must include a licence before publishing to a public source code repository.

#### Licences

Include a licence by adding a LICENSE file as part of open source code.

Recommended permissive licences are:

* MIT for small, simple projects and scripts;
* Apache 2.0 for larger software project.

Recommended reciprocal licences are:

* GPL 3.0 for software
* LGPL 3.0 for libraries
* AGPL 3.0 for web applications and services

## Appendix B - Source Code Repository

Recommended public source code repositories for Government of Canada open source code are:

* [GitLab](https://gitlab.com/)
* [GitHub](https://github.com/)
* [framagit](https://framagit.org/)
* [Bitbucket](https://bitbucket.org/)

The Government of Canada also has an internal source code repository available to all departments and agencies.

* [GCcode](https://gccode.ssc-spc.gc.ca/) (internal to Government of Canada only)

### Organizations

Departments and agencies are free to choose the platform that best suites their operational needs but their projects should, where possible, all be regrouped under a unique organization or group.

### Mandatory Files

Before publishing open source code, it must include:

* a LICENCE (see Licencing above) file containing a copy of the licence under under which the source code is released;
* a README.md file providing bilingual information about the project, how to use it and general documentation.

It should also include:

* a CONTRIBUTING.md file explaining how to contribute to the project.
* a SECURITY.md file explaining security policy as well as security vulnerabilities reporting procedures.

Examples of these files are available in the [Template repository](https://github.com/canada-ca/template-gabarit).
