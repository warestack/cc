# 2. Piazza application requirements

Implement the Piazza API and business rules below. Use the [testing and deployment requirements](03-testing-and-deployment.md) to verify and deploy your work.

## Registration and authentication

Provide registration and login endpoints.

- Each user must have a unique email address and a password.
- Store password hashes, never plaintext passwords.
- Successful login must return an expiring JWT access token.
- Require a valid bearer token for all Piazza business endpoints.
- Reject missing, invalid and expired tokens.
- Do not expose password hashes or secrets in API responses.

Registration, login, health checks and API documentation may be publicly accessible. A separate OAuth2 authorisation server is not required.

> **Clarification:** All authenticated users may read all Piazza posts, including expired posts. Determine the author of a new post, reaction or comment from the verified token, not a user identifier supplied in the request.

## Posts and topics

Authenticated users must be able to create posts and retrieve them individually or by topic.

Each post must contain:

- A unique identifier.
- Its author.
- A title and message body.
- One or more topics.
- A creation timestamp.
- An expiry timestamp.
- Its current status: `Live` or `Expired`.
- Like and dislike counts.
- Associated comments.

Use these topic names consistently:

**Politics, Health, Sport and Tech.**

Validate incoming data. Titles, message bodies and comments must contain non-whitespace text. Posts must have at least one valid topic and an expiry time later than their creation time.

A post assigned to multiple topics must appear when browsing any of those topics.

> **Clarification:** Generate post identifiers and creation timestamps on the server. Use integer post identifiers for the ranking tie-break. A new post starts with zero likes, zero dislikes and no comments. Persist users, posts, reactions and comments in SQLite.

## Reactions and comments

For reactions and comments on live posts:

- A user may have only one reaction per post.
- Repeating the same reaction must not increase the count.
- Switching from like to dislike, or vice versa, replaces the previous reaction.
- Authors cannot like or dislike their own posts.
- Authors may comment on their own live posts.
- Users may add multiple comments.
- Each comment must record its author, content and creation timestamp.

## Expiry and history

Use UTC timestamps consistently.

A post is expired when:

```
current time >= expiry time
```

Expired posts must remain readable, including their existing reactions and comments. They must reject new reactions and comments.

Topic browsing must support filtering by `Live` or `Expired`. If no status filter is supplied, return both.

You may calculate status when processing a request; no background task is required.

> **Clarification:** Accept expiry timestamps with an explicit timezone and compare them in UTC. Reject timestamps without a timezone with `422`. Expiry blocks comments as well as reactions, including a repeated reaction that would otherwise leave counts unchanged.

## Most-active post

Provide an endpoint returning the most-active **live** post in a topic.

Calculate activity as:

```
number of likes + number of dislikes
```

Comments do not contribute to this score.

Resolve ties by:

1. The newest creation timestamp.
2. The lowest post identifier if timestamps are also equal.

Return an empty list when no live posts exist in the requested topic.

> **Clarification:** A live post with zero reactions can still be the most-active post.

## API contract

Implement the following interface. Document request fields, response fields and examples through FastAPI’s generated documentation and your README.

| Method | Endpoint                      | Purpose                                             | Successful response                       |
| ------ | ----------------------------- | --------------------------------------------------- | ----------------------------------------- |
| POST   | `/auth/register`              | Register a user                                     | `201`, public user details                |
| POST   | `/auth/login`                 | Authenticate a user                                 | `200`, access token and token type        |
| POST   | `/posts`                      | Create a post                                       | `201`, created post                       |
| GET    | `/posts`                      | Browse posts; optional `topic` and `status` filters | `200`, list of posts                      |
| GET    | `/posts/{post_id}`            | Retrieve one post                                   | `200`, post details                       |
| PUT    | `/posts/{post_id}/reaction`   | Set or replace the current user’s reaction          | `200`, updated reaction counts            |
| POST   | `/posts/{post_id}/comments`   | Add a comment                                       | `201`, created comment                    |
| GET    | `/topics/{topic}/most-active` | Retrieve the most-active live post                  | `200`, a list containing zero or one post |
| GET    | `/health`                     | Check application health                            | `200`, health status                      |

Registration and login accept JSON. For example:

```json
{
  "email": "olga@example.com",
  "password": "example-test-password"
}
```

A post-creation request must accept:

```json
{
  "title": "Cloud computing discussion",
  "body": "What are the advantages of containers?",
  "topics": ["Tech"],
  "expires_at": "2027-06-01T12:00:00Z"
}
```

The date above is an example. In your tests, use an expiry time after the test clock’s current time.

A reaction request contains `{"value": "like"}` or `{"value": "dislike"}`. A comment request contains `{"body": "A comment"}`.

Use these error codes consistently:

| Code  | Meaning                                                      |
| ----- | ------------------------------------------------------------ |
| `401` | Missing, invalid or expired authentication, or incorrect login credentials |
| `403` | An author attempts to react to their own live post           |
| `404` | The requested resource does not exist                        |
| `409` | Duplicate registration, or an attempted interaction with an expired post |
| `422` | Invalid request data, topic, status filter or reaction value |

For authenticated interaction requests, check that the post exists and remains live before applying the self-reaction rule.

> **Clarification:** For example, `/posts?topic=Tech&status=Live` returns live Tech posts. With neither filter, return all posts; when no posts match, return `200` with `[]`. Use the topic and status spellings shown in this brief. Post editing, deletion and reaction removal are not required.

## Assignment navigation

- [1. Assignment overview and development](README.md)
- [2. Piazza application requirements](02-application-requirements.md)
- [3. Testing and deployment](03-testing-and-deployment.md)
- [4. Report marking and submission](04-report-marking-and-submission.md)
