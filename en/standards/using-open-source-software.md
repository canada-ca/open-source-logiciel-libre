# Standard on using open source software (Draft)

[Back to Table of Contents](../../README.md#english-content)

* Authorities
* Objectives and expected results
  * The expected results of this directive are as follows
* Requirements

* Appendix A - Active and Fair Consideration
  * Approvals
  * Open Source Software First
    * Open Core
  * Cloud

* Appendix B - Legal Compliance
  * Without Modification
  * With Modification
    * Strong reciprocal implications

## Authorities

This Standard is issued under the authority of section 7 of the [Financial Administration Act](https://laws-lois.justice.gc.ca/eng/acts/f-11/) and pursuant to sections 3 and 6.4.9 of the [Policy on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=12755) and the section C.2.3.8 of the [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8).

## Objectives and expected results

The objective of this directive is to maximize the use of open source software as key components of its technology ecosystem to improve interoperability between systems, seek independence from software, technologies and vendors as well as substitutability of solutions and service providers.

### The expected results of this directive are as follows

* Enable greater flexibility in the management of information and communication technologies (ICT).
* Increase the reuse of existing open source software and technology by departments and agencies.
* Support and increase collaboration between departments, agencies and other public administrations in Canada and around the world, including society as a whole.
* Canadians are able to reuse and contribute to open source software used by the GC to support meaningful engagement with their government and communities.
* Improve the overall availability of re-usable technology within government and society.
* Support Canadian economic growth by removing barriers to entry in providing technological services and solutions.

## Requirements

**Managers, functional specialists, and equivalents responsible for enterprise architecure and software procurement and development are responsible for**

Ensuring that open source software be actively and fairly considered for all new technologies, upgrades or migrations, including cloud solutions.
See Appendix A.

Ensuring that the use of open source software is compliant with its licence's terms and conditions.
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

## Appendix A - Active and Fair Consideration

### Approvals

Approvals reside with each government department or agency's information management and technology group.

### Open Source Software First

Open source software must be selected first on the basis of its additional inherent flexibility, when there is no significant functionality or total cost ownership (TCO) difference with closed-source solutions.

If an open source software based solution meets most of the users needs but requires investment to develop remaining functionalities, this option must also be considered by comparing the TCO, including exit and transition costs.
All source code developed must be published or contributed back to the open source software community.
See [Standard for Publishing Open Source Code](publishing-open-source-code.md) and [Standard for Contributing to Open Source Software](contributing-to-open-source-software.md).

#### Open Core

A solution that is built with open source software but that requires the use of closed-source components should not be considered open source software for the purpose of this Standard.
The open core development model is where vendors open only portions of their software and then surround the remainder with closed-source offerings.
The free open source software versions often referred to as "community" editions are recommended first.

### Cloud

Some open source software is available directly as software as a service (SaaS) on the cloud either for free or subscription based.
This may create lock-in if the software and support can't easily be migrated to other service providers.

Open source software can be deployed using platform as a service (PaaS) or infrastructure as a service (IaaS).
This must be considered same as SaaS when responsibility for hosting, setup, configuration, maintenance and support can be done by a service provider or internally.
This provides additional flexibility in the selection of cloud provider (public or private) and the support service provider.

## Appendix B - Legal Compliance

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used as long as its use is compliant with its terms and conditions.

Depending on the intended use, the licence under which an open source software was released may put some specific requirements on the user of the code.

* [Without Modification](#without-modification)
* [With Modification](#with-modification)

### Without Modification

Using open source software without modification for internal (within the Government of Canada) and for public facing applications is not considered distribution and does not require that code be shared back.

This is also true for combination of open source software to build a solution or open source software used for development and production (ex.: container, database, programming language, ..).
When writing source code, see [Standard for Publishing Open Source Code](publishing-open-source-code.md).

### With Modification

Using open source software, even with modifications for internal (within the Government of Canada) and for public facing applications is not generally considered distribution and does not require that code be shared back.
See Strong Reciprocal Implications.

#### Don't Fork Open Source Software

Where possible, use open source software without modification. Use configuration and customize the software with modules, plugins or extensions and make those available to the community.
See [Standard for Publishing Open Source Code](publishing-open-source-code.md).

It's easy to copy (fork) open source software and start making changes to the source code.
If a fork is created, be aware it can make future updates and security patches hard to implement as well as trigger additional licence obligations.
The development team that made the changes will be responsible for maintaining those changes unless they are contributed to the upstream version.

To make changes in open source software, engage with the community and submit changes upstream to ensure that they are supported by future updates.
See [Standard for Contributing to Open Source Software](contributing-to-open-source-software.md).

#### Strong Reciprocal Implications

The AGPL reciprocal licence and others like the EUPL considers that software accessed through a network (like the Internet) is distribution and the modified source code must be made available to users.
See [Standard for Publishing Open Source Code](publishing-open-source-code.md).
