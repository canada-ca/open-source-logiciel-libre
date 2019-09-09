# Open Source Standards

Treasury Board of Canada Secretariat’s **draft** standards to support the implementation of Treasury Board policy requirements related to open source use, contribution and creation and open standards.

The Government of Canada has been using Open Source Software as part of its technology ecosystem for years and is increasingly relying on them for its successful service delivery.
As part of its commitment to become a Digital Government, it has to also contribute back to external projects as well as release its own source code under Open Source Licences.
It is committed to doing so in a manner that is compatible with core administrative law principles such as transparency, accountability, legality and procedural fairness.

## The Importance of a Concept Case

Prior to any form of development or acquisition, it is important that a Concept Case be defined for any problem space. 

The Concept Case should clearly define the Business Requirement driving the project, this helps ensure that the GC follows current Trade Laws and has evidence in the event of a Trade Tribunal Complaint. 

### Evaluate Requirements
Technical and Functional requirements cannot be used as justification for the purpose of evaluation of Open Source Software to proprietary Software, only Business requirements.

The following are examples of elements that can be taken into consideration in the creation of business requirements, but it's important to remember that procurement rules may require that business requirements permit the bidding of both proprietary and Open Source Software.

#### The Use of International or Canadian Standards

The GC may set its requirements such that the underlying application conform to International or Canadian Standards, such as but not limited to the official languages requiring Software be available in both official languages.

#### Flexibility of the License

Open Source Software licenses can provide more flexibility then a proprietary license for the product of your concept case.

In the case that Software could be reused, the GC may set its requirement such that the Software being procured be used in subsequent projects in the GC. The licensor can grant such right of re-use as required, but by its nature all Open Source Software would be compliant with this request by default.

#### Ability to use for any Purpose

The GC may set its requirements such that Software be used for any purpose, having no restrictions in how it can be used, or allow others to use the Software.

#### The Ability to Evaluate the Code

The GC may set its requirements such that the source-code be available for audit by a third party to identify quality, functionality and security of the Software. 

#### The Alignment with Open Government

In addition the GC may set its requirements such that the source-code be provided to the public to enable greater transparency and align with [Open Government principles of the D9](https://www.canada.ca/en/government/system/digital-government/improving-digital-services/digital9charter.html). 

#### The Ability to Distribute the Software

The GC may set its requirements such that the Software be available for distribution to anyone of its choice to ensure that other crown institutions do not need to become customers of the original vendor in order to access and use services provided by another agency. For example the federal crown may wish to be able to provide the Software at no extra costs to provincial or municipal institutions.

### Defining Where Appropriate and Where Possible

The Directive on Management of Information Technology states under [C.2.3.8.1](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249&section=procedure&p=C) and [D2.2.1.4.2](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249&section=procedure&p=D) that 'where possible', use open standards and open software first. As well the [Digital Standards](https://www.canada.ca/en/government/system/digital-government/government-canada-digital-standards.html) state 'Leverage open standards and embrace leading practices, including the use of open source software where appropriate'.

Where Appropriate and Where Possible are defined as all items that are not exempt due to the following
- The Source Code is not owned exclusively by the Crown and is not already open-source.
- The Source Code is protected

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

It is highly unlikely that developers would intentionally include such information in their source code. As a result, source code is considered unclassified unless the developer has included, inadvertently or otherwise, information that falls under the [exemptions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-3.html#h-10) and [exclusions](http://laws-lois.justice.gc.ca/eng/acts/a-1/page-10.html#h-29) of the [Access to Information Act](http://laws-lois.justice.gc.ca/eng/acts/A-1/) as listed above.

Where feasible, this information should be removed from the source code to increase the ability for code to be shared.

## Procedures and Guidance for Open Source Software

- [Procurement of Open Source](guides/procurement-of-open-source.md)
- [Use of Open Source Software](guides/using-open-source-software.md)
- [Contribution to Open Source Software](guides/contributing-to-open-source-software.md)
- [Publication of Open Source Code](guides/publishing-open-source-code.md)

## Definitions

### Business Requirement

A Business Requirement is defined as a specific need that must be addressed in order to achieve an objective. These drive the element of 'why' for a project defining the nature and purpose at a high level.

### Functional Requirement

A Functional Requirement is defined as a more specific lower level needs in order to achieve an objective. These drive the element of 'what' for a project defining the specific details. 

### Technical Requirement

A Technical Requirement is defined as an architectural decision to support an objective. These drive the element of 'how' for a project defining the architecture of the software and how it should interface with other systems and software.

### Source Code
Computer program in its original programming language, human readable, before translation into object code usually by a compiler or an interpreter. It consists of algorithms, computer instructions and may include developer's comments.

### Open Source

Open Source is defined by the Government of Canada as any and all Software that meets the following basic requirements:

1. Free Redistribution
The license shall not restrict any party from selling or giving away the software as a component of an aggregate software distribution containing programs from several different sources. The license shall not require a royalty or other fee for such sale.

2. Source Code
The program must include source code, and must allow distribution in source code as well as compiled form. Where some form of a product is not distributed with source code, there must be a well-publicized means of obtaining the source code for no more than a reasonable reproduction cost, preferably downloading via the Internet without charge. The source code must be the preferred form in which a programmer would modify the program. Deliberately obfuscated source code is not allowed. Intermediate forms such as the output of a preprocessor or translator are not allowed.

3. Derived Works
The license must allow modifications and derived works, and must allow them to be distributed under the same terms as the license of the original software.

4. Integrity of The Author's Source Code
The license may restrict source-code from being distributed in modified form only if the license allows the distribution of "patch files" with the source code for the purpose of modifying the program at build time. The license must explicitly permit distribution of software built from modified source code. The license may require derived works to carry a different name or version number from the original software.

5. No Discrimination Against Persons or Groups
The license must not discriminate against any person or group of persons.

6. No Discrimination Against Fields of Endeavor
The license must not restrict anyone from making use of the program in a specific field of endeavor. For example, it may not restrict the program from being used in a business, or from being used for genetic research.

7. Distribution of License
The rights attached to the program must apply to all to whom the program is redistributed without the need for execution of an additional license by those parties.

8. License Must Not Be Specific to a Product
The rights attached to the program must not depend on the program's being part of a particular software distribution. If the program is extracted from that distribution and used or distributed within the terms of the program's license, all parties to whom the program is redistributed should have the same rights as those that are granted in conjunction with the original software distribution.

9. License Must Not Restrict Other Software
The license must not place restrictions on other software that is distributed along with the licensed software. For example, the license must not insist that all other programs distributed on the same medium must be open-source software.

10. License Must Be Technology-Neutral
No provision of the license may be predicated on any individual technology or style of interface.

### Proprietary Software
This refers to all Software not considered Open Source Software, copyrighted and traditionally governed by extensive terms and conditions.

### Crown Institution

A Crown Institution includes all Departments, Agencies, Provincial, Municipal, Crown Corporation or any other form of Government of Canada institution operating under the authority of the Crown.