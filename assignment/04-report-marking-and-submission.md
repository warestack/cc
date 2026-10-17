# 4. Report marking and submission

Use the report structure, marking criteria and submission checklist below.

- [Report structure](#technical-report-structure)
- [Marking criteria](#marking-criteria)
- [Submission checklist](#submission-checklist)

## Technical report structure

The technical report accounts for **20% of the assignment mark** under F1–F4.

Write approximately **1,500–2,000 words**. References, API tables, the development milestone table and evidence appendices are excluded from this target.

Use the following structure:

| Section                   | Suggested words | Content                                                      |
| ------------------------- | --------------- | ------------------------------------------------------------ |
| Overview and architecture | 200             | Purpose, architecture diagram and relationship to teaching material |
| Implementation            | 350             | Data model, authentication, validation and Piazza rules      |
| Automated testing         | 350             | Summary of unit/API tests, results, isolation, representative cases and limitations |
| Containerisation          | 200             | Image design, registry reference and VM execution            |
| Kubernetes deployment     | 400             | Deployment, storage, Pod replacement, update and cleanup     |
| Critical evaluation       | 250             | Limitations, technical trade-offs and justified improvements |
| **Suggested total**       | **1,750**       |                                                              |

### Required testing section

Include a clearly labelled **Automated testing** section in the main report. Summarise:

- What your unit tests and API integration tests check, including their relationship to TC01–TC20 and the additional required cases.
- How to run the suite, the assessed commit SHA and the date of the reported test run.
- The number of tests passed, failed and skipped, separately for unit tests and API tests. Explain failures, skips and untested requirements.
- How you isolate the database and control time, plus one representative successful case and one rejected or boundary case.

Use a compact results table, interpret the results and reference the full matrix and pytest output. Do not paste the test suite into the report.

> **Clarification:** C1–C3 assess the executable tests; F4 assesses their written summary and interpretation. Both are required.

### Report details and evidence

Begin with:

- Student identifier.
- Repository URL.
- Full submitted commit SHA.
- Docker Hub image reference and digest.

Include numbered evidence with captions explaining what it demonstrates. Link evidence to the relevant marking criteria.

Appendices should contain:

- API summary.
- Requirement-to-test matrix.
- GitHub milestone table and timing/push evidence, as specified in the [development requirements](README.md#github-development-requirements).
- Evidence index.

Keep full command sequences in the README. Explain decisions and results in the report, referencing adapted code, teaching material and external sources.

> **Clarification:** Word counts are guidance. Keep explanations in the main report and supporting evidence in appendices. For deployment claims, show the command or request, result and interpretation; a running Pod alone does not prove API functionality or persistence.

## Marking criteria

Each mark is one percentage point of the assignment total.

| ID | Criterion | Marks |
| --- | --- | ---: |
| A1 | Appropriate data models, relationships and constraints | 3 |
| A2 | Post creation, retrieval and topic/status filtering | 4 |
| A3 | Reactions and comments | 4 |
| A4 | Expiry and most-active behaviour | 4 |
|  | **Piazza functionality subtotal** | 15 |
| B1 | Registration, password hashing and duplicate handling | 3 |
| B2 | Expiring JWTs and protection of business endpoints | 4 |
| B3 | Input validation and consistent error responses | 3 |
|  | **Authentication and validation subtotal** | 10 |
| C1 | Unit tests of application rules | 4 |
| C2 | API integration tests of successful and unsuccessful requests | 4 |
| C3 | Isolated fixtures, repeatable execution and interpretable results | 2 |
|  | **Automated testing subtotal** | 10 |
| D1 | Appropriate Dockerfile and build context | 2 |
| D2 | Basic repository README with reproducible build/run instructions and versioned registry image | 2 |
| D3 | Working container on the GCP VM | 1 |
|  | **Containerisation subtotal** | 5 |
| E1 | Working GKE Deployment and LoadBalancer Service | 3 |
| E2 | Persistent storage and successful Pod-replacement verification | 4 |
| E3 | Versioned application update and cleanup evidence | 3 |
|  | **Kubernetes subtotal** | 10 |
| F1 | Traceable technical evidence and reproduction references | 5 |
| F2 | Critical evaluation of design choices and limitations | 4 |
| F3 | Clear report structure, architecture diagram and references | 5 |
| F4 | Clear and accurate testing summary with results, representative cases and limitations | 6 |
|  | **Technical report subtotal** | 20 |
| G1 | Five meaningful milestone commits | 10 |
| G2 | At least five qualifying commits spanning 15 full days | 10 |
| G3 | Descriptive commit messages explaining the changes made | 5 |
| G4 | Preserved, traceable history and evidence of regular pushes throughout development | 5 |
|  | **GitHub development subtotal** | 30 |
|  | **TOTAL** | 100 |

### Performance descriptors

The percentages below apply to the marks available for each individual criterion, except G1 and G2, which use the explicit rules stated below.

| Criterion | 0–49%                                  | 50–59%                                  | 60–69%                                        | 70–100%                                                      |
| --------- | -------------------------------------- | --------------------------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| A1        | Missing or inconsistent model          | Core entities persist                   | Clear relationships and constraints           | Well-justified model with robust integrity                   |
| A2        | Major operations fail                  | Main post operations work               | Filtering and retrieval work reliably         | Complete, consistent behaviour including edge cases          |
| A3        | Interactions missing or incorrect      | Basic reactions/comments work           | Duplicate, switching and ownership rules work | All interaction rules implemented robustly                   |
| A4        | Expiry/ranking substantially incorrect | Main expiry and ranking work            | Boundaries and filtering handled              | Exact boundary, ties and empty cases handled consistently    |
| B1        | Registration insecure or incomplete    | Registration and hashing work           | Duplicates and failures handled clearly       | Reliable registration without credential exposure            |
| B2        | Protection absent or bypassable        | Main endpoints protected                | Invalid/expired tokens rejected consistently  | All required routes and token failures handled robustly      |
| B3        | Little validation                      | Main fields validated                   | Required error codes used consistently        | Thorough validation with clear, predictable responses        |
| C1        | Few meaningful unit assertions         | Core rules directly tested              | Positive and negative rule cases tested       | Boundary and transition tests detect plausible defects       |
| C2        | Manual evidence or superficial tests   | Main API flows tested                   | Authentication and failure flows tested       | Comprehensive state and response assertions across requirements |
| C3        | Tests unreliable or contaminate data   | Suite runs with basic isolation         | Fixtures and setup are repeatable             | Deterministic clock, cleanup and restart checks are clearly evidenced |
| D1        | Image fails or context is unsuitable   | Working basic Dockerfile                | Sensible layers and exclusions                | Clear, reproducible packaging with appropriate configuration |
| D2 | README missing or build/run unclear | Basic README instructions and tagged image provided | README supports a reproducible fresh build/run | Concise, complete README with precise configuration and image identity |
| D3        | No working VM evidence                 | Container starts on VM                  | API requests succeed through VM address       | Clear evidence of the assessed image and expected behaviour  |
| E1        | Deployment unavailable                 | Pod and Service operate                 | External API access demonstrated              | Correct manifests, configuration and reproducible deployment |
| E2        | Data lost or persistence unproven      | Volume mounted and data stored          | Data survives Pod replacement                 | Clear before/after verification tied to stored records       |
| E3        | Update/cleanup absent                  | Some update or cleanup evidence         | Update preserves data; cleanup shown          | Both stages clearly verified with version and resource evidence |
| F1        | Claims difficult to verify             | Main evidence identifiable              | Evidence maps clearly to requirements         | Concise, complete traceability to the assessed revision      |
| F2        | Descriptive or unsupported             | Main limitations recognised             | Trade-offs explained using evidence           | Critical, technically justified evaluation and improvements  |
| F3        | Unclear or poorly referenced           | Readable structure and basic references | Clear diagram and appropriate attribution     | Precise, coherent report with complete attribution           |
| F4 | Testing summary absent, unclear or unsupported | Main test types and results summarised | Results, representative cases and limitations explained with evidence | Accurate, concise interpretation linking results, isolation and boundary cases to the assessed revision |
| G3 | Mostly vague or missing descriptions | Messages identify the main changes | Messages consistently describe coherent changes | Precise, informative messages make development decisions and fixes easy to follow |
| G4 | History unavailable, one final upload or progress largely unverifiable | History retained with some dated push evidence | Milestone links and dated pushes demonstrate staged development | Complete milestone traceability and dated pushes clearly demonstrate sustained development |

Higher marks within a band reflect greater completeness, correctness and quality of evidence.

### GitHub marking rules

- **G1 (10 marks):** Award 2 marks for each of the five milestones evidenced by a distinct meaningful commit. At least five qualifying commits are needed for all 10 marks. One commit cannot count for multiple milestones.
- **G2 (10 marks):** Award 10 marks only where at least five qualifying commits span at least 15 full days within the assignment period and before submission. Otherwise award 0 for G2. This does not impose an automatic cap on the assignment or remove marks earned under other criteria.

Partial credit is available. A deployment failure does not automatically remove marks for functioning application code or tests. Implementation and testing are assessed separately. The same omission will not be deducted twice within one criterion.

Test quantity and coverage percentages alone do not earn marks. Screenshots do not replace executable automated tests. Additional features cannot raise the total above 100%.

> **Clarification:** Technical marks assess what works; report marks assess explanation and evidence. Missing the 15-day requirement loses G2’s 10 marks, not all 30 GitHub marks.

## Submission checklist

Submit **one PDF report through Moodle** and complete the separate AI Declaration. Keep code and supporting files in GitHub; do not upload a source-code archive.

> **Clarification:** Markers assess the recorded commit SHA. Later changes are outside the submission.

Before submission, confirm that:

- Your report links to a repository accessible to markers.
- The final assessed commit has been pushed and its SHA is recorded.
- The repository preserves at least five meaningful commits covering all five milestones, with the first and last qualifying commits at least 15 full days apart.
- The report appendix includes qualifying commit links, the elapsed-period calculation and dated push evidence.
- Source code, tests, dependencies, Docker assets and Kubernetes manifests are included.
- A basic root-level README.md explains the application, prerequisites, setup, configuration, testing, container execution and deployment.
- The report includes a testing section summarising unit/API tests, pass/fail/skip counts, representative cases and limitations.
- The report provides evidence for VM execution, GKE deployment, persistence, update and cleanup.
- Secrets, real credentials and unnecessary personal data are excluded.
- Reused material and permitted AI assistance are acknowledged.
- The official Moodle AI Declaration is completed.

Your repository and report must describe the work you actually completed. Explain any incomplete features, failed tests or deployment limitations accurately.

## Assignment navigation

- [1. Assignment overview and development](README.md)
- [2. Piazza application requirements](02-application-requirements.md)
- [3. Testing and deployment](03-testing-and-deployment.md)
- [4. Report marking and submission](04-report-marking-and-submission.md)
