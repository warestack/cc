# 3. Testing and deployment

Test your application locally, then demonstrate it in Docker on a GCP VM and on GKE. Keep the evidence needed for your [report and submission](04-report-marking-and-submission.md).

## Automated testing requirements

Write and run automated tests locally using **pytest**. All tests must run using one documented command, such as:

```bash
python -m pytest
```

The suite must not require cloud access, cloud credentials or a deployed service.

Include both:

- **Unit tests:** Direct tests of application rules, such as expiry, reaction transitions and ranking.
- **API integration tests:** Requests through FastAPI `TestClient`, checking authentication, validation, database effects, response bodies and status codes.

Use fixtures and an isolated test database. Tests must not modify your development database or depend on execution order.

Use a controllable clock for expiry tests. Do not make tests wait several minutes for posts to expire.

### Required scenario coverage

Implement automated coverage of the following Piazza scenario. Tests may use independent fixtures rather than one long sequence.

| ID   | Required behaviour                                           |
| ---- | ------------------------------------------------------------ |
| TC01 | Olga, Nick, Mary and Nestor register successfully            |
| TC02 | All four users log in and receive tokens                     |
| TC03 | Olga’s request without a token is rejected                   |
| TC04 | Olga creates a Tech post with an expiry timestamp            |
| TC05 | Nick creates another Tech post                               |
| TC06 | Mary creates another Tech post                               |
| TC07 | Tech browsing returns three posts with no initial reactions or comments |
| TC08 | Nick and Olga like Mary’s post                               |
| TC09 | Nestor likes Nick’s post and dislikes Mary’s post            |
| TC10 | Counts show Mary with two likes and one dislike, and Nick with one like |
| TC11 | Mary’s attempt to like her own post is rejected              |
| TC12 | Nick and Olga each add at least two comments to Mary’s post  |
| TC13 | Browsing returns the correct reaction counts and comments    |
| TC14 | Nestor creates a Health post                                 |
| TC15 | Health browsing returns the appropriate Health post          |
| TC16 | Mary comments on Nestor’s live Health post                   |
| TC17 | Mary’s attempted reaction after its expiry is rejected       |
| TC18 | The expired Health post remains readable with its existing comment |
| TC19 | Expired-post browsing for Sport returns an empty list when none exist |
| TC20 | Mary’s post is the most-active Tech post while the relevant Tech posts remain live |

Also test duplicate registration, incorrect login, invalid and expired tokens, invalid input, missing resources, repeated and switched reactions, empty comments, multiple-topic posts, ranking ties and empty ranking results.

Test expiry immediately before, exactly at and after the boundary. Include an automated check that stored data survives closing and reopening the application against the same temporary database file.

Map requirements to test names in a test matrix and save the pytest output. Summarise actual results in the report’s [required testing section](04-report-marking-and-submission.md#required-testing-section).

> **Clarification:** Use as many test functions as needed to cover all twenty scenarios. Keep Tech posts live for TC20 when advancing the clock past the Health post’s expiry. Check that expired posts reject both reactions and comments.

## Containerisation requirements

Package your application using Docker.

Your repository must contain:

- A Dockerfile.
- A `.dockerignore`.
- Dependency files with reproducible version information.
- Build and execution instructions.
- An example configuration containing placeholders rather than secrets.

Build the image, run it on the GCP VM used in the tutorials and verify the API through the VM’s address.

Publish the image to Docker Hub using an explicit version tag. Record the version tags and image digests used for the VM demonstration and both GKE versions in your report.

Use configuration to select the database location and JWT secret. The SQLite database must be stored outside the container’s disposable filesystem when demonstrating persistence.

> **Clarification:** Both VM and GKE demonstrations are required. Use a volume or bind mount for SQLite on the VM and a PersistentVolumeClaim on GKE. Exclude databases and real secrets from the image.

## Kubernetes deployment requirements

Deploy Piazza on **Google Kubernetes Engine** using:

- One API replica.
- A Kubernetes Deployment using the `Recreate` strategy.
- A LoadBalancer Service.
- A PersistentVolumeClaim mounted at the SQLite database location.
- Configuration and a Kubernetes Secret for the required settings.

Keep the JWT signing secret consistent across Pod replacement and application updates. Do not commit real secret values or secret manifests containing credentials.

Demonstrate:

1. The deployed API works through the Service address.
2. A post created through the deployed API is stored successfully.
3. Deleting the application Pod causes Kubernetes to create a replacement.
4. The replacement Pod can retrieve the previously stored post.
5. Updating to a second versioned image succeeds and preserves the data.
6. The cloud resources are cleaned up after evidence collection.

Use one replica because this assignment uses a file-based SQLite database. Explain the resulting limitations in availability, concurrent writes and horizontal scaling.

Capture evidence before cleanup. The application does not need to remain running during marking.

> **Clarification:** Replace only the Pod, keeping its Deployment and volume. For the update, deploy a visible change under a new image tag and verify the same stored post. Brief downtime with `Recreate` is acceptable.

## Assignment navigation

- [1. Assignment overview and development](README.md)
- [2. Piazza application requirements](02-application-requirements.md)
- [3. Testing and deployment](03-testing-and-deployment.md)
- [4. Report marking and submission](04-report-marking-and-submission.md)
