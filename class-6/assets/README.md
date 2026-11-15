# Week 6 screenshots

## Lab verification

These screenshots show the lab running on a disposable Ubuntu Compute Engine VM. The Docker Hub demonstration used a temporary private repository.

| Screenshot | What to look for |
| --- | --- |
| `ubuntu-container.png` | The Bash prompt and Ubuntu release inside `mini-ubuntu`. |
| `fastapi-container-health.png` | The published port and successful health check on the VM. |
| `fastapi-swagger.png` | The two routes listed in the running app's Swagger UI. |
| `sqlite-volume-replacement.png` | Two container IDs, one named volume, and the same course record. |
| `docker-hub-push-pull.png` | The matching push and pull digests for tag `1`. |

## Docker Hub reference images

These PNG files were extracted unchanged from the user-supplied **Cloud Computing 2026-2027 - Lab 02.docx**. They illustrate Docker Hub controls in [Tutorial 4](../lab/docker-hub.md); they are reference UI, not screenshots of a completed Week 6 exercise. The source DOCX was not modified.

| Extracted file | Source media path inside DOCX | Topic | Caption used in the tutorial |
| --- | --- | --- | --- |
| `docker-hub-signup-reference.png` | `word/media/image2.png` | Account creation | Select Personal if asked; current account screens may differ. |
| `docker-hub-signin-reference.png` | `word/media/image4.png` | Docker Hub account controls | Reference location of Sign in / Sign up. |
| `docker-hub-create-repository-reference.png` | `word/media/image44.png` | Create repository control | Reference Create repository button. |
| `docker-hub-tags-reference.png` | `word/media/image66.png` | Published repository tags | Source sample uses `my-web-server` and older tags; Week 6 uses `week6-courses-api:1`. |

All four images were visually inspected before reuse. Source `word/media/image45.png` was reviewed and omitted because its prominent private-repository quota message is specific to the source account. Source login/password and terminal screenshots were omitted in favour of current token-based instructions and commands tailored to the Courses API. Lab 03 is a MySQL/Compose exercise and supplies no SQLite screenshots for this tutorial.
