# Standard on using open source software (Draft)

[Back to Table of Contents](../../README.md#english-content)

## Authorities

This directive is issued under the authority of section 7 of the [Financial Administration Act](https://laws-lois.justice.gc.ca/eng/acts/f-11/) and pursuant to sections 3 and 6.4.9 of the [Policy on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=12755).

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

Ensuring that open source software be actively and fairly considered for all new technologies, upgrades or migrations, including cloud solutions. See Appendix A.

Ensuring that the use of open source software is compliant with its licence terms and conditions. See Appendix B.

**notes:** Ensuring that solutions are properly supported - Appendix C: Support Models. Ensuring that software is properly obtained - Appendix D: Procurement

**The senior departmental official, designated by the deputy head, is responsible for**

Overseeing the implementation of this standard in their department and carrying out the activities referred to in Monitoring and Reporting Requirements.

Encouraging personnel to collaborate departmentally and interdepartmentally, to share expertise, and to prioritize reusable components and tools.

**The Chief Information Officer (CIO) of departments and agencies, or any other person named by the CIO, is responsible for the following**

Ensuring that the open source software requirements of this directive are integrated in any new plans for procuring, developing, or modernizing departmental information applications, systems, or solutions in support of the delivery of programs and services.

Encouraging personnel to collaborate departmentally and interdepartmentally, to share expertise, and to prioritize reusable components and tools.

**Centres of Expertise are responsible for**

Serving as the primary point of contact between Treasury Board of Canada Secretariat's Chief Information Officer Branch and their department for questions and communications related to interpretation and implementation of the standards, guidelines and tools.

Participating in the interdepartmental Centres of Expertise forum, chaired by the Treasury Board of Canada Secretariat's Chief Information Officer Branch, to stay current with evolving standards, guidelines and tools.

## Monitoring and Reporting Requirements

### Senior departmental official

The senior departmental official, designated by the deputy head, is responsible for supporting their deputy head by overseeing the implementation and monitoring of this standard in their department, bringing to the deputy head's attention any significant difficulties, gaps in performance or compliance issues and developing proposals to address them, and reporting significant performance or compliance issues to the Chief Information Officer Branch of Treasury Board of Canada Secretariat.

### Government-wide

The Treasury Board of Canada Secretariat will monitor compliance with this standard in a variety of ways, including but not limited to, the following:

* assessments under the Management Accountability Framework;
* examinations of Treasury Board submissions, departmental performance reports, results of audits, evaluations and studies; and work performed in collaboration with departments; and

The Treasury Board of Canada Secretariat will review this standard and its effectiveness at the five-year mark from the effective date of the standard (or earlier if warranted).

## Appendix A - Active and Fair Consideration

Open source software must be selected on the basis of its additional inherent flexibility, when there is no significant functionality or cost difference with closed-source solutions.

If an open source software based solution meets most of the users needs but requires investment to develop remaining functionalities, this option must be considered by comparing the total cost ownership (TCO), including exit and transition costs.

### Cloud

Some open source software is available directly as software as a service (SaaS) on the cloud either for free or subscription based, which in some instances may create dependence and lock-in when you can't easily migrate your solution to another service provider.

Open source software can also be deployed using platform as a service (PaaS) or infrastructure as a service (IaaS).
This must be considered same as SaaS when responsibility for hosting, setup, configuration, maintenance and support can be done by a service provider.

This latter option provides additional flexibility in the selection of the service provider at inception of the solution and also guarantees that the solution developed can live beyond the initial service provider, in line with the Digital Standards.

## Appendix B - Legal Compliance

Depending on the intended use, the licence under which an open source software was released may put some specific requirements on the user of the code.

* [Without Modification](#without-modification)
  * [Combination of Components and Development](#combination-of-components-and-development)
* [With Modification](#with-modification)

### Without Modification

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used without modifications as long as its use is compliant with its terms and conditions.
Using open source software without modifications for internal (within the Government of Canada) and for public facing applications does not require that code be shared back.

**note:** notices for use?

### With Modification

All open source software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) can be used with modifications as long as its use is compliant with its terms and conditions.

Using open source software, even with modifications for internal (within the Government of Canada) and for public facing applications is not generally considered distribution and does not require that code be shared back.

#### Strong reciprocal implications

The AGPL reciprocal licence and others like the EUPL considers that software accessed through a network (like the Internet) is distribution and the modified source code must be made available to users.

**note:** see publishing

## Appendix C - Support Models

### Internal

Using a self-support model requires that the responsible teams:

* Maintain and track thorough lists of open source software used and ensure updates are applied carefully.
* User and developer community should be leveraged for general support questions as well as reporting bugs, creating feature requests and code contributions.

See [Standard for Contributing to Open Source Software](contributing-to-open-source-software.md).

### Professional Services

It is possible to enter in contract with a company for professional services to provide maintenance, updates, warranty and liability for open source software.

Another scenario that may become recurrent would be choosing an open source software and using the community version and later down the road going for tender for professional support and maintenance. *However, proper guidance needs to be confirmed with legal and procurement teams.*

If custom development with traditional request for proposal contracted developers is required, you should follow the [Standard for Publishing Open Source Code](publishing-open-source-code.md).

Finally, another option would be to leverage the [GCDevExchange](https://gcdevexchange-carrefourproggc.org/en) to have some custom code written for the government of Canada as open source through a bidding process. Code developed through this platform should be published as open source.

## Appendix D - Procurement

### Open Source First

Community editions of open source software support the Digital Standards and are thus recommended first.

In order to have professional support, the procurement should be around the  services around the solution rather than the product itself.

### Open Core

A solution that is built with open source software but that you can't access all of its source code is not deemed open source for the purpose of this Standard.

### Custom Code

See [Standard for Publishing Open Source Code](publishing-open-source-code.md).
