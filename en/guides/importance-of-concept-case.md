# The Importance of a Concept Case

Prior to any form of development or acquisition, it is important that a Concept Case be defined for any problem space. 

The Concept Case should clearly define the Business Requirement driving the project, this helps ensure that the GC follows current Trade Laws and has evidence in the event of a Trade Tribunal Complaint. 

## Evaluate Requirements
Technical and Functional requirements cannot be used as justification for the purpose of evaluation of Open Source Software to proprietary Software, only Business requirements.

The following are examples of elements that can be taken into consideration in the creation of business requirements, but it's important to remember that procurement rules may require that business requirements permit the bidding of both proprietary and Open Source Software.

### The Use of International or Canadian Standards

The GC may set its requirements such that the underlying application conform to International or Canadian Standards, such as but not limited to the official languages requiring Software be available in both official languages.

### Flexibility of the License

Open Source Software licenses can provide more flexibility then a proprietary license for the product of your concept case.

In the case that Software could be reused, the GC may set its requirement such that the Software being procured be used in subsequent projects in the GC. The licensor can grant such right of re-use as required, but by its nature all Open Source Software would be compliant with this request by default.

### Ability to use for any Purpose

The GC may set its requirements such that Software be used for any purpose, having no restrictions in how it can be used, or allow others to use the Software.

### The Ability to Evaluate the Code

The GC may set its requirements such that the source-code be available for audit by a third party to identify quality, functionality and security of the Software. 

### The Alignment with Open Government

In addition the GC may set its requirements such that the source-code be provided to the public to enable greater transparency and align with [Open Government principles of the D9](https://www.canada.ca/en/government/system/digital-government/improving-digital-services/digital9charter.html). 

### The Ability to Distribute the Software

The GC may set its requirements such that the Software be available for distribution to anyone of its choice to ensure that other crown institutions do not need to become customers of the original vendor in order to access and use services provided by another agency. For example the federal crown may wish to be able to provide the Software at no extra costs to provincial or municipal institutions.

## Defining Where Appropriate and Where Possible

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