# Guide for Contributing to Open Source Software (Draft)

The [Directive on Management of Information Technology](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249), Appendix C, provides Mandatory Procedures for Enterprise Architecture Assessment. These will be used by the GC Enterprise and departmental Architecture Review Boards in an assessment framework for digital initiatives to ensure that all sub-organizations of the GC adhere to a single, consistent digital direction.

This strategy aligns with the [Digital Standards](https://www.canada.ca/en/government/publicservice/modernizing/government-canada-digital-standards.html) and requirement C.2.3.8 of the [Mandatory Procedures for Enterprise Architecture Assessment](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=15249#claC.2.3.8) which provide that all custom source code must be released under an appropriate open source software licences.

As such it is recommended for departments to contribute back to the community all source code modifications made to 3rd party open source software, whether done in-house by GC employees or through procurement contracts.

## There Are Many Ways to Contribute

Open source communities are driven by a wide range of contributions.
Code that fixes bugs or implements valued features is of course very important, but non-code contributions such as writing or editing documentation, or submitting feature requests and bug reports, are also highly valued.
Even simply supporting the contributions of others, or expressing interest in another's feature request, can be a valued contribution.

The steps for GC to contribute code to open source software communities are:

1. [Verify Open Source Software Licence](#verify-open-source-software-licence)
2. [Verify Contributing Process and Policies](#verify-contributing-process-and-policies)
3. [Additional Approvals](#additional-approvals)
4. [Contribute to the project](#contribute-to-the-project)
5. [Contribute through professional services](#contribute-through-professional-services)
6. [Publish contributions regardless of upstream acceptance](#publish-contributions-regardless-of-upstream-acceptance)

## Verify Open Source Software Licence

The GC can contribute to all software licensed under an [Open Source Initiative approved license](https://opensource.org/licenses) or a [Free Software Foundation free software licence](https://www.gnu.org/licenses/license-list.html).

If a licence for software developed in the open is under another licence, seek legal counsel to clarify if contributions are recommended.

## Verify Contributing Process and Policies

Certain projects may have specific policies for code contribution (Contributor Licence Agreement, Developer's Certificate of Origin) as well as processes (templates, platform, etc.).
Before going forward with submitting a contribution, employees should properly understand the project contribution processes and policies.
Employees should then ensure that the delegated approvals meet those requirements.

### Contributors Licence Agreement

Contributors Licence Agreements (CLA) are contracts that some project owners require external contributors to sign before accepting their contributions. Those contracts could state various clauses, including the following examples:

- The external contributor confirms that the original work (the contribution) is their own work and can thus legally share it with the project.
- The copyright of the contribution needs to be transferred to the project owners.
- Patent rights are granted to the project owners for the purpose of this project.
- Etc.

Since these may be complex and have many various clauses, it is highly recommended to seek legal counsel before agreeing to these additional contractual obligations.

In general, it is not a problem to contribute to a project that has a CLA in place but additional analysis is best practice. Some projects are moving away from these complex contracts to remove the barrier they create around external contributions in favour of Developer's Certificate of Origin.

### Developer's Certificate of Origin

A Developer's Certificate of Origin (DCO) is considered to be a way of stating to the project maintainers that by submitting this contribution, the contributor confirms he or she has the right to do so.

It usually consist of adding a "Signed by: contributor@email.com" in the commit of the code.

Unlike for a CLA, if you do have the right to submit a contribution, a DCO should not cause a problem as you should have already acquired the proper approvals to contribute to the project.
See [Additional Approvals](#additional-approvals)

## Additional Approvals

If for some reason the departmental delegated approvals are not meeting the third-party contribution's requirements, employees should contact their supervisor to see how they can obtain the additional approvals required.
Departments should define specific criteria for approval of open-source contributions, and describe them clearly to employees.

### Time

Some departments may institute guidelines or policy stating that employees must get their manager's approval to spend public time contributing to open source software.
This should not be intended to curtail open-source contribution, but only to allow for the prioritization of operational needs; the default policy should be to encourage contributing back to open-source projects used by the GC.

### Department

Similar to open data or information covered by the [Directive on Open Government](https://www.tbs-sct.gc.ca/pol/doc-eng.aspx?id=28108), the publication of source code under an open source software licence, requires appropriate department or agency approvals.

That person may vary according to your department and delegation should be encouraged to the lowest level possible to encourage contribution to 3rd party OSS projects.

## Contribute to the project

### Identify as an employee of the Government of Canada

In order to contribute, it may be required that you set up an account with the site or platform where the project you want to contribute to is hosted.
This should clearly identify you as an employee of the Government of Canada since you would be contributing back as such.
If there is an option to have your organization listed on the project, it would be beneficial to do so as well.

Currently, it is recommended that employees use their full name and Government of Canada email address for all code contributions to public repositories while acting within the scope of their duties or employment as this is the primary way of identifying your work.
Some services allow you to list multiple email addresses, others may require you to set up a new account for official contributions.

**Note**: this provision is related to the [Public Servant Invention Act](https://laws-lois.justice.gc.ca/eng/acts/P-32/FullText.html#h-3), section 3.
Additional clarification as to the means of identifying as an employee of the GC without requiring the email address in commits will need to be sought to ease the process and your organization may already have its own guidance around this topic.

### Submit changes

To make changes in open source software, engage with the community and submit your changes upstream, which means to the original project, to ensure that your modifications are supported by future updates.
This way, your changes will help improve the software for everyone that uses it but you will also ensure that you stay in line with the original project and don't have to maintain a separate version of the source code.

Contributing to a 3rd party should be done in accordance to the project governance model, if such a model is present.

## Contribute through professional services

If your department would like to leverage professional services to contribute to third party projects, see [Obtain Rights to Custom Code in Contracts](publishing-open-source-code.md#obtain-rights-to-custom-code-in-contracts)

## Publish contributions regardless of upstream acceptance

Whether or not a given set of changes is accepted upstream as a contribution, the changes should still be published in accordance with the [Guide for Publishing Open Source Code](https://github.com/canada-ca/open-source-logiciel-libre/blob/master/en/guides/publishing-open-source-code.md).

Publication allows upstream, the original project, to pick up the changes at some later date, and allows 3rd parties to pick up the changes independently of when or whether upstream does so.

Changes not accepted by upstream should still be noted in upstream forums where possible and appropriate, so that 3rd parties who might be interested in those changes have a means of discovering them.
