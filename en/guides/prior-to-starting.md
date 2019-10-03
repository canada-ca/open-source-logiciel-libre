# Guide for Open Source Software Acquisition

The Directive on Management of Information Technology, Appendix C provides Mandatory Procedures for Enterprise Architecture Assessment that will be used by departmental Architecture Review Boards (ARB) and the Government of Canada Enterprise ARB as an assessment framework to review digital initiatives to ensure the GC acts as a single enterprise and to ensure departmental alignment with the GC digital direction.

These align with the Digital Standards and requirement C.2.3.8 of the Mandatory Procedures for Architecture Assessment which provide that, where possible, open source software be used first.

Law and policy applicable to the GC may require that the acquisition of software, software servicing or professional services relating to software be competed through an invitation to suppliers calling for the tender of the goods or services. However, where software can be acquired for free and alone, without any compulsory fees for manuals, media or services, and the Business Requirement substantiates the acquisition of OSS instead of Proprietary Software, the acquisition of such software through download or otherwise without a call for tenders may be possible.

In the event that Open Source Software has already been procured, or is not bound by Trade Contract Laws move to the ‘Using Open Source Software’ section.

The steps for the GC to tender or procure open source software are:

1. [Considerations](#considerations)
2. [Evaluations](#evaluations)
3. [Acquisition Principles](#acquisition-principles)


## Considerations

The first consideration is that open source software tends to have narrowly focused functionally. There is an expectation users will integrate and manage multiple products together to create a solution. A large open source solution commonly requires one or more core products and 3rd-party plugins. The work of integration, support, and management tends to fall more on the user than with commercial software. This may not be a concern if in-house expertise is valued as part of the solution.

Second, access to support needs to be considered. The quality of open source updates, documentation, and forums will differ by product from excellent to non-existent. However most open source products do not provide a contractual means by which a specific question can be answered or update obtained in a timely manner. This tends to be a greater issue early in a solution’s lifecycle therefore significant lab testing can help offset concerns in this area. Some companies offer commercial support for open source software however this rarely covers all parts of an integrated solution.

The final major consideration is the benefits of open source software. The most obvious relate to acquisition and deployment. While open source software will have an attached license, they generally allow free acquisition and deployment without restriction. Open source software tends to provide ease of integration through open APIs, data exchange tools, and open storage formats. Also, open source software allows full access to the source code for ease of inspection and modification. For these reasons open source software tends to allow flexibly to scale and change the solution to meet future needs and reduce product lock-in.

## Evaluations

When evaluating open source software the availability of information presents a barrier. Unlike commercial software, most open source projects do not have a sales and marketing team creating easy to consume information. This poses a challenge and may require searching the internet for secondary sources, reading technical documentation, and lab testing.

In general, open source functionally should be evaluated in the same manner as other software. Beyond functionality, the key questions are: can the solution be managed, is support available, and do the benefits lead to best value? While these questions apply to commercial software, they have increased relevance for open source and can be harder to answer. 

The questions below provide a roadmap to answering these larger questions for open source software.

### Design
 - What open source product(s) are needed to meet the requirements?
 - Integrating a large number open source products may meet requirements but cause other problems. Can the same requirements be met with a less complex solution?
 - Many open source products assume an industry standard environment. Can the requirements be changed to match industry standards and allow open source products to work with less integration or modification?
 - Can integration be accomplished with open APIs or a well defined plug-in architecture?
 - Is data stored in an easy to manipulate (import/export/inspection/migration) format?
 - Are the APIs and storage formats used by other products and do they use open standards?
   
### Procurement
 - What are the license restrictions?
 
### Community 
 - Are the products normally used in the proposed manner?
 - How large is the user base and is it growing or shrinking?
 - Are there other users, similar to you, using similar solutions?
 - Who is the developer and are they likely to continue with the
   project? E.g single developer, research group, small company, tech
   giant, consortiums, …
 - Is one group the only significant contributor?
 - Is one group clearly limiting features? For example, is there one
   company that is the primary contributor and also offers a commercial
   “enterprise” version? 
    - If so, are they doing so in a logical manner
   and what would the long term impact be?
 - Does the project have rules for contributing that are supportive of
   community contributions?
 - Are proposed enhancements from 3rd-partys (pull requests) left
   unresolved?
   
### Development 
 - Does the project follow a documented release management process?
 - Are all parts of the solution released and tested together?
 - Can the product(s) be tested in a lab environment?
 - Do we already have in-house expertise or can it be developed? 
 - What will the cost be?

### Support 
 - Does a recent Long Term Support (LTS) release exist? 
	 - Is so, what is the planned support duration?
 - Has the project been forked? 
	 - If so, are the forks taking away from the main project or contributing to it?
 - Are bugs public? 
	 - Is so, are bugs left unresolved for long periods?
 - Are security related bugs resolved quickly with easy to deploy patches?
 - Is documentation complete and up to date?
 - Are there bugs related to documentation and are they resolved in a timely manner?
 - Are their secondary sources of documentation, tutorials, etc.?
 - Is there a dedicated and active community support forum? 
	 - What is the tone of the forum? 
	 - Are forums limited in any way such that you may be forced to buy support or an enterprise version?
 - Is commercial support available? 
	 - Is so, is it available from more then one source? 
	 - Is commercial support available from someone other than the primary contributor?

## Acquisition Principles

If open source software has not already been acquired by Canada, since it may be that the law requires the acquisition to be competed, the GC must substantiate, through its Concept Case and the formation of its Business Requirement, a *bona fide* operational reason to acquire Open Source Software instead of Proprietary Software, when OSS is chosen.

Therefore, prior to acquisition, your institution’s legal services unit should be consulted to review the software Business Requirements and to properly specify in any tender notice the contract terms that would apply to your acquisition.

This open source software policy guidance does not remove or nullify any other Government of Canada policy guidance, such as the Directive on the Management of Procurement and its associated Guidance. Where Canada acquires software on open source software terms, the Contracting Authority must first seek the appropriate exemptions from Treasury Board or other appropriate authorities if a resulting contract will contain terms that are not in accordance with such existing Government of Canada policies.
