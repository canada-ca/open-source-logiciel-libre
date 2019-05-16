# Guide for Contributing to Open Source Software (Draft)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C, provides mandatory procedures for enterprise architecture assessment. These will be used by the GC Enterprise and departmental Architecture Review Boards in an assessment framework for digital initiatives to ensure that all sub-organizations of the GC adhere to a single, consistent digital direction.  This strategy aligns with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and the [Procedures for Application Architecture](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8) in that all source code must be released under appropriate open source software licences:

> **All source code modifications made to open source software, whether in-house by GC or through procurement contracts, must be shared back with the open source software community.**
> **The GC must be an active contributor to open source software it's using or where there is benefit to Canadians, by sharing code, but also by creating bug reports and feature requests as well as helping with testing and influencing the development roadmap.**

## There Are Many Ways to Contribute

Open source communities are driven by a wide range of contributions.
Code that fixes bugs or implements valued features is of course very important, but non-code contributions such as writing or editing documentation, or submitting feature requests and bug reports, are also highly valued.
Even simply supporting the contributions of others, or expressing interest in another's feature request, can be a valued contribution.

### Steps required for GC employees to contribute to open source:

1. [Verify Open Source Software Licence](#verify-open-source-software-licence)
1. [Verify Contributing Process and Policies](#verify-contributing-process-and-policies)
1. [Seek Approvals](#seek-approvals)
1. [Contribute](#contribute)
1. [Other Notes](#other-notes)

## Verify Open Source Software Licence

The GC can contribute to all software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) or a [Free Software Foundation free software licence](https://www.gnu.org/licenses/license-list.html).

If a licence for software developed in the open is under another licence, seek legal counsel to clarify if contributions are recommended.

## Verify Contributing Process and Policies

Certain projects may have specific policies for code contribution (Contributor Licence Agreement, Developer's Certificate of Origin) as well as processes (templates, platform, etc.).
Before going forward with submitting a contribution, employees should properly understand the project contribution processes and policies.
Employees should then ensure that the delegated approvals meet those requirements.

## Additional Approvals

If for some reason the departmental delegated approvals are not meeting the third-party contribution's requirements, employees should contact their supervisor to see how they can obtain the additional approvals required.
Departments should define specific criteria for approval of open-source contributions, and describe them clearly to employees.

### Time

Some departments may institute guidelines or policy stating that employees must get their manager's approval to spend public time contributing to open source software.
This should not be intended to curtail open-source contribution, but only to allow for the prioritization of operational needs; the default policy should be to encourage contributing back to open-source projects used by the GC.

### Department

Similar to open data or information covered by the [Directive on Open Government](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28108), the publication of source code under an open source software licence, requires appropriate department or agency approvals.
Because of the required assignment of rights by an open source software licence, the Assistant Deputy Minister (ADM), or any other person named by the ADM is responsible for approving the releases of open source code.

As mentioned previously, delegation should be encouraged to be done to the lowest level possible to encourage contribution to 3rd party OSS projects.

## Contribute to the project

### Identify as an employee of the Government of Canada

Set up an account with the site where the project you want to contribute to is hosted. 
This should clearly identify you as an employee of the Government of Canada. 
If there is an option to have your [organization listed](https://openconcept.ca/blog/mike/your-organization-using-drupal-get-drupalorg-account), it would be beneficial to do so as well.

Currently, employees should use their full name and Government of Canada email address for all code contributions to public repositories while acting within the scope of their duties or employment as this is the primary way of identifying your work.
Some services allow you to list multiple email addresses, others may require you to set up a new account for official contributions.

**Note**: this provision is related to the [Public Servant Invention Act](https://laws-lois.justice.gc.ca/eng/acts/P-32/FullText.html#h-3), section 3. 
Additional clarification as to the means of identifying as an employee of the GC without necessarily requiring the email address in commits will need to be sought to ease the process.

### Submit changes

To make changes in open source software, engage with the community and submit your changes upstream to ensure that your modifications are supported by future updates.

Contributing to a 3rd party should be done in accordance to the project governance model, if such a model is present.

## Contribute through professional services

If professional services are used to contribute to third party projects, see [Guide for publishing Open Source Code](publishing-open-source-code.md#obtain-rights-to-custom-code-in-contracts)

## Publish contributions regardless of upstream acceptance

Whether or not a given set of changes is accepted upstream as a contribution, the changes should still be published in accordance with the [publication policy](https://github.com/canada-ca/open-source-logiciel-libre/blob/master/en/guides/publishing-open-source-code.md).
Publication allows upstream to pick up the changes at some later date, and allows 3rd parties to pick up the changes independently of when or whether upstream does so.
Changes not accepted by upstream should still be noted in upstream forums where possible and appropriate, so that 3rd parties who might be interested in those changes have a means of discovering them.

## Other Notes

* Licence delegation authority (IP+licence)
  * Recommended that delegation of authority to contribute on a 3rd party OSS project be granted de facto given key requirements:
    * No CLA is required (would need the organisation to sign it, not the individual - to be confirmed)
    * IP still belongs to the Crown
* Security
  * Contributing employee follows Policy on Acceptable Network and Device Use, just like any other external services.
    * 2FA is recommended
* Basic commits guidelines (use your name, prof email address., message, etc.)
* Grants and contributions for open source projects and foundations
