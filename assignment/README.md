# 1. Advanced Cloud Computing Coursework

Develop, test and deploy Piazza with FastAPI

- **Assessment type:** Individual postgraduate coursework
- **Total marks:** 100
- **Report length:** Approximately 1,500–2,000 words
- **Deadline:** As published on Moodle
- **Submission:** One PDF report containing a link to your GitHub repository, plus the required Moodle AI Declaration.

Read all four files in order. Together they form the assignment brief; navigation links appear at the end of each file.

## Assignment overview

Piazza is a discussion platform where registered users publish posts by topic, react and comment. Expired posts remain readable but accept no further interactions. Build its backend with FastAPI, authentication and persistent storage; test it with pytest, package it with Docker and deploy it on Google Kubernetes Engine. Explain your work and provide evidence in a technical report.

Follow the technologies and approaches introduced in the [Cloud Computing teaching repository](https://github.com/warestack/cc):

- Python and FastAPI.
- Pydantic for validation.
- SQLAlchemy and SQLite for data storage.
- JWT bearer authentication.
- pytest and FastAPI `TestClient`.
- Docker and Docker Hub.
- Google Cloud and Kubernetes.

GitHub Actions, Cassandra and ZeroMQ are outside this assignment. A frontend and CI/CD pipeline are not required and receive no additional marks.

## Individual work and permitted AI use

This is an individual assessment. All submitted work must reflect your own understanding, and you must be able to explain it. You may adapt teaching and appropriately licensed examples with clear attribution. Do not submit another student’s work or an externally obtained complete solution.

### AI restrictions for this assessment

AI use is optional and limited to conceptual explanations, debugging guidance on your own code, feedback on your approach, and spelling or grammar checks. Make all implementation decisions yourself. Do not use AI to generate or rewrite assessed code, tests, Dockerfiles, Kubernetes manifests or report text, including through editor assistants. Never fabricate results, screenshots, references, development history or deployment evidence.

Complete the official Moodle AI Declaration even if you have not used AI. Where permitted AI assistance is used, acknowledge the tool, date, purpose and affected parts of your work, and retain records of prompts and outputs privately. The report acknowledgement does not replace the Moodle declaration. Follow [Birkbeck’s AI guidance for assessment integrity](https://www.bbk.ac.uk/professional-services/registry-services/student-policies-2026-27/generative-artificial-intelligence).

## GitHub development requirements

Create your repository at the start of the assignment. Use either:

- A repository in the Birkbeck GitHub organisation designated on Moodle, accessible to the markers; or
- A public repository in your personal GitHub account.

Both options receive the same marks. Keep your own coursework repository accessible until marking and moderation are complete.

Your GitHub work is worth **30 marks**. See [G1–G4](04-report-marking-and-submission.md#github-marking-rules) for the breakdown.

Make **at least five meaningful commits spanning at least 15 full days (360 hours)**. Measure the interval between your first and last meaningful commits using their Git author timestamps in UTC. All meaningful commits must fall within the assignment period and be included in the submitted revision.

Make at least one meaningful commit for each milestone:

| Milestone                  | Expected repository progress                               |
| -------------------------- | ---------------------------------------------------------- |
| 1. Initial setup           | Project structure, dependencies and initial README         |
| 2. Application development | Data models, authentication and Piazza functionality       |
| 3. Automated testing       | Unit tests, API tests and fixes arising from testing       |
| 4. Containerisation        | Docker configuration and container execution instructions  |
| 5. Kubernetes deployment   | Manifests, deployment instructions and evidence references |

Commit coherent changes and push at each milestone. Use descriptive messages such as `Reject reactions on expired posts`. Five commits are the minimum; extra commits earn no automatic bonus.

Each commit should show useful progress. Empty commits, minor edits made only to increase the count and other people’s commits do not count. Push as you work, keep your history and do not alter commit dates. Uploading everything at the end is insufficient.

In the report appendix, provide a milestone table with completion dates, commit messages and direct links to at least five meaningful commits. Show the first and last timestamps, calculate the elapsed period and include dated GitHub push evidence. See [G1–G4](04-report-marking-and-submission.md#github-marking-rules) for how marks are awarded.

> **Clarification:** Commits record local changes; pushes upload them to GitHub. Commit timestamps do not prove when you pushed. For the 15-day rule, 1 November at 12:00 UTC to 16 November at 12:00 UTC qualifies; commits on 15 calendar dates alone may not.

### Development log

Create `development-log.md` in the root of your repository. Update, commit and push it as you work, with at least one entry for each of the five milestones.

Each entry should briefly record the date, work completed, a key decision or problem, related commit links, and any sources or permitted assistance used. For permitted AI assistance, identify the tool and purpose; keep prompts and outputs private.

The log supports your existing development evidence and carries no additional marks. It does not replace the report milestone table or Moodle declaration.

## Basic repository README

Add a short `README.md` in the main folder of your repository with:

- A short description of Piazza and the main technologies used.
- Prerequisites and commands to install dependencies.
- Required configuration variables, using placeholders rather than real secrets, and the SQLite database location.
- Commands to run the application locally and access its API documentation.
- The command to run all tests with pytest.
- Docker build/run instructions, the versioned Docker Hub image reference, and Kubernetes deployment and cleanup instructions. You may link to longer instructions elsewhere in your repository.

> **Clarification:** The README explains how to run your project. Keep the analysis and screenshots in the report.

## Assignment navigation

- [1. Assignment overview and development](README.md)
- [2. Piazza application requirements](02-application-requirements.md)
- [3. Testing and deployment](03-testing-and-deployment.md)
- [4. Report marking and submission](04-report-marking-and-submission.md)
