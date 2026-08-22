# Tech Note 09-18: Using Amazon Elastic Compute Cloud for 4D Benchmarking and Testing

**Author:** Thomas Maul, 4D Germany
**Published:** May 7, 2009 | **Product/Version:** 4D v11.4 | **Platform:** Mac & Win
**Page:** https://kb.4d.com/assetid=75737
**Download:** https://kb.4d.com/DLTN/TN/2009/Windows/TN_2009_18-21_(MAY)/09-18_Cloud_Bench.zip

## Proposition
This note shows how to use Amazon EC2 to rent multiple virtual machines on demand, cheaply simulating many concurrent 4D Server clients via POST KEY-based keyboard emulation, so developers can prove multi-user performance to customers without owning dozens of physical test machines.

## Key Points
- **Cost model (2009):** EC2 instances rented from $0.125–$1.20/hour with no setup fee; ~20 small "client" instances plus one large "server" instance could run a 45-minute load test for under $5.
- **Define a stress test plan first** with the customer — identify which parts of the application see heavy concurrent load and at what realistic per-user speed, rather than testing arbitrary metrics.
- **POST KEY-driven emulation:** a low-cost way to script realistic keyboard-based user interaction without expensive dedicated UI-testing software.
- **Step-by-step EC2 setup:** security groups, choosing an Amazon Machine Image, launching/connecting to instances, preparing and bundling a reusable client image, and separately preparing a server instance.
- **Cleanup step emphasized** to avoid ongoing EC2 charges after testing completes.

## Featured Technology
- Amazon Elastic Compute Cloud (EC2)
- Elasticfox (AWS EC2 management extension)
- Amazon Machine Images (AMI) for client/server test instances
- POST KEY (automated keyboard-driven user emulation)
- 4D Server multi-user stress/load testing

## Best Practices Highlighted
1. Agree on a concrete, realistic stress-test plan with the customer before any technical setup, rather than chasing arbitrary raw throughput numbers.
2. Bundle a prepared client AMI once so it can be relaunched repeatedly for future tests without redoing setup.
3. Always clean up rented EC2 resources promptly after testing to avoid unnecessary ongoing costs.

## Context / Positioning
Published when cloud computing itself was still a novel concept for many developers, this note was an early, practical bridge between 4D consulting practice and the emerging elastic-cloud paradigm, aimed at consultants needing to credibly demonstrate scalability to prospects.

## Historical Commentary
**Status:** Partially Superseded

This note pioneered using Amazon EC2 to rent multiple virtual machines for cost-effective multi-user 4D Server load testing, driven by POST KEY-based keyboard emulation, at a time when cloud computing itself was a novel concept for most developers. The core idea of using elastic cloud compute for on-demand load/stress testing is not just still relevant but has become entirely mainstream practice.

However, the specific tooling shown (the EC2 "Classic"-era workflow, the Elasticfox browser extension, and manual AMI bundling steps) is long obsolete, superseded by AWS's modern EC2 console/CLI/API, VPC-based networking, and by purpose-built load-testing and CI/CD-integrated performance tools that didn't exist in 2009.
