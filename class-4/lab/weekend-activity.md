### Week 4: Weekend Activity

#### Your Backend Architecture and API Journey

Plan how the components of your final Piazza application will work together. You do not need a finished application or cloud deployment for this activity.

#### Part A: Draw a Simple Architecture Diagram

Create one readable diagram of your planned backend. Use diagrams.net, PowerPoint, Mermaid or a clear hand-drawn sketch. Include:

- A client such as Postman or the API documentation page.
- FastAPI routes and Pydantic request/response validation.
- Registration/login, password hashing and JWT verification.
- Application rules, such as deciding whether a post is still live.
- SQLAlchemy models and sessions, and the SQLite database file.

Use arrows with short labels to show requests, database queries and responses. Show the signing secret as configuration, without its value. Add a small **planned deployment** outline: Docker container inside one GKE Pod, a LoadBalancer Service for access, and a persistent volume for SQLite. These parts will be taught by Week 7; label them as planned rather than claiming they already run.

> **Clarification:** Pydantic, authentication and SQLAlchemy are components within your backend, not separate cloud servers. SQLite is a file, not a separate database service. You do not need a frontend.

#### Part B: Explain the User Journey

Write **200–300 words** following one user who logs in and retrieves posts through the API. Explain:

1. How the user registers, and why a password hash is stored.
2. How login returns an expiring JWT and the client sends it with a later request.
3. How the backend checks the token, validates query parameters and applies application rules.
4. How SQLAlchemy reads SQLite and the API returns a JSON response to the client.
5. What the user receives if the token is invalid or expired.

Refer to the labels in your diagram. Describe your own planned design and distinguish implemented components from planned ones.

#### Part C: Share in Teams

Post your diagram as an image or PDF and your 200–300-word explanation in the **module Teams chat**. Use the title **Week 4 — My backend architecture**. Include one design question you would like feedback on, and respond constructively to one classmate's diagram.

Share the design, not assessed source code, credentials, tokens or personal data. This activity is for feedback and adds no assignment marks. You may develop your diagram for the report later, updating it to match what you actually build.

#### Checklist

- All core backend components appear, with labelled arrows.
- The explanation follows a complete login-to-data journey.
- Cloud components are labelled as planned where appropriate.
- The explanation is 200–300 words and the diagram is readable.
- The post contains no secrets or assessed solution code.

There is no single model diagram: your design may differ. Use the checklist to review it and bring questions to the lab.

Return to [Week 4](../README.md).
