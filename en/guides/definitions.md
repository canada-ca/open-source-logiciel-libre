# Definitions

## Defining Where Appropriate and Where Possible

The Directive on Management of Information Technology states under [C.2.3.8.1](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249&section=procedure&p=C) and [D2.2.1.4.2](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249&section=procedure&p=D) that 'where possible', use open standards and open software first. As well the [Digital Standards state](https://www.canada.ca/en/government/system/digital-government/government-canada-digital-standards.html) 'Leverage open standards and embrace leading practices, including the use of open source software where appropriate'.

Where Appropriate and Where Possible are defined as all items that are not exempt due to the following:

- The Source Code is not owned exclusively by the Crown and is not already open-source.
- The Source Code is protected

In order for source code to potentially be deemed protected, it would have to contain any of the following information:

- Information that is deemed Classified
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

It is highly unlikely that developers would intentionally include such information in their source code. As a result, source code is considered unclassified unless the developer has included, inadvertently or otherwise, information that falls under the items listed above.

Where feasible, this information should be removed from the source code to increase the ability for code to be shared.

## Terms

### Open Source Software (OSS)

Open Source Software is generally, software for which the underlying programming code is available to users to read, change and build new versions of the software incorporating changes. In particular, GC considers that OSS is any Software that meets all the following basic requirements:

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

### Business Owner

The business owner is the executive who is responsible for the business or program area for which the digital project has been established. The business owner is responsible for defining the required capabilities, intended business outcomes and benefits of a project or programme at its outset and for the achievement of the business outcomes and benefits following implementation of the digital project.

### Business Requirement

A Business Requirement is defined as a specific need that must be addressed in order to achieve an objective. These drive the element of 'why' for a project defining the nature and purpose at a high level. In the Context of OSS, this means fulfilling Canada’s requirement to have the rights to use the software being acquired for a particular purpose, such as redistributing or carrying out modifications to software.

### Concept Case

A Concept Case means the creation of a case for a digital project (formerly known as IT-enabled projects) or initiative in accordance with Appendix C of Canada’s Policy on the Planning and Management of Investments, with the value of the digital project in Appendix C.2.2 calculated to include all project investments for software, servicing and professional services associated with a digital project.  A concept case is an examination of a business problem or opportunity for which a digital project may be established and includes a description of the conceptual future state and intended outcome(s) that are expected to result from the investment.  As such, it must take into account all elements of the digital project costed over its life cycle.

### Functional Requirement

A Functional Requirement is defined as a more specific working level need in order to achieve an objective. These drive the element of 'what' for a project defining the specific details and describe a particular function of software or part of it to attain an expected result.

### Technical Requirement

A Technical Requirement is defined as an architectural decision to support an objective. These drive the element of 'how' for a project defining the architecture of the software and how it should interface with other systems and software.

### Source Code

Computer program in its original programming language, human readable, before translation into object code usually by a compiler or an interpreter. It consists of algorithms, computer instructions and may include developer's comments.

### Proprietary Software

This refers to all Software that is not Open Source Software as defined above, which is copyrighted and not subject to Open Source Software License terms.

### Crown Institution

A Crown Institution includes all Departments, Agencies, Provincial, Municipal, Crown Corporation or any other form of Government of Canada institution operating under the authority of the Crown.
