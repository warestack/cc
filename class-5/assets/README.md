# Week 5 image inventory

The refreshed walkthrough uses a dedicated demonstration project, **cc-2026-labs** (`cc-2026-labs-20261029`), created on 29 October 2026 and linked to **Billing Account for Education**. Students create their own project; they must not copy the demonstration project ID.

All images are local, genuine interface captures. Crops remove irrelevant controls and unrelated resources. Solid masks remove personal details where needed; no interface, balance, or terminal output is fabricated. Routine Linux commands are presented as copyable text rather than illustrated individually.

## Fresh captures from the dedicated-project walkthrough

| File | Shows | Source and capture notes |
| --- | --- | --- |
| `grant-request-current.jpg` | Blank current coupon-request form and eligible school domains | Retaken from the course retrieval link; no request submitted. Instructor contact masked. |
| `credit-redemption-current.jpg` | Current coupon redemption form | Retaken without submitting a coupon; personal name fields cleared, account email masked. |
| `project-create.jpg` | Project name, unique ID, and education billing selection | Captured before actually creating the dedicated project. |
| `project-selector.jpg` | Selected lab project and New project action | Retaken; unrelated project rows cropped out. |
| `project-billing-linked.jpg` | Dedicated project linked to education billing | New capture with selected project visible in the header. |
| `education-credit-current.jpg` | Current available credit and expiry | New $100 staff-grant example, explicitly distinguished from the $50 student award. Credit ID hidden with the console's column controls. |
| `compute-engine-api-enable.jpg` | Compute Engine API Enable button | Retaken before enabling the API in the new project. |
| `compute-engine-ready.jpg` | VM instances and Create instance after activation | New capture of the empty project before its first VM. |
| `vm-name-location.jpg` | VM name and us-central1-a zone | Retaken while configuring the actual main VM. |
| `vm-machine-configuration.jpg` | e2-medium, shared CPU allocation, 4 GB RAM, Standard provisioning | Retaken from an unsubmitted Create similar form after the actual VM was created; settings match the verified VM. |
| `ubuntu-boot-disk.jpg` | Ubuntu 24.04 LTS x86/64, balanced disk, 10 GB | Retaken from the same unsubmitted configuration form; settings match the actual VM. |
| `vm-no-backups.jpg` | No backups selected | New capture during actual main-VM configuration. |
| `vm-networking-http.jpg` | Main VM HTTP enabled, HTTPS disabled | Retaken before actual main-VM creation. No web server installed. |
| `exercise-networking.jpg` | Exercise HTTP and HTTPS disabled | Retaken before actual exercise-VM creation from scratch. |
| `main-vm-running.jpg` | Main VM running, zone, and SSH button | Retaken after actual creation in the new project. |
| `exercise-vm-running-ssh.jpg` | Exercise VM running in the required zone | Retaken from the new project; main VM is stopped in the same list. Cropped to status, name, and zone. |
| `ssh-connect-current.jpg` | Browser SSH Connect confirmation naming lab-5 | New capture before connecting to the new main VM. |
| `ssh-connected-current.jpg` | Connected browser SSH and hostname lab-5 | New capture. Initial SSH prompt shortened to `vm:~$` for privacy; it is not evidence of a custom lab-user login. |
| `pico-package-verified.jpg` | APT confirms nano, executable /usr/bin/pico, version | Retaken on the new main VM as its initial SSH user, with shortened prompt. No custom-user ownership claim. |
| `vm-stop-confirmation.jpg` | Stop confirmation and retained-resource charges | New capture from stopping the main VM. |
| `vm-start-menu.jpg` | Start/Resume action on the stopped VM | New capture. Main VM was actually restarted and running state verified, then stopped again. |
| `main-vm-stopped.jpg` | Main and exercise VMs stopped, with e2-medium types | Retaken after both shutdowns completed. Disk storage is retained; this does not demonstrate exercise deletion. |
| `exercise-vm-stopped.jpg` | Same verified stopped state | Inventory-only copy documenting the paused exercise resource. |
| `exercise-delete-confirmation.jpg` | Delete confirmation explicitly naming exercise VM and boot disk | New capture of the final dialog. Deletion awaits confirmation; this image is not evidence of completed deletion. |

## Retained images that cannot currently be replayed

| File | Original source | Why retained |
| --- | --- | --- |
| `grant-verification-example.png` | Existing `2.png` | Email verification requires a new enrollment. Already verified accounts cannot replay this confirmation. |
| `coupon-email-example.png` | Existing `3.png` | Coupon issuance requires a new enrollment. Code, names, address, and obsolete dates masked. |
| `ssh-authorization-example.png` | Supplied DOCX `word/media/image31.png`, relationship `rId45` | Signed-in browser is already authorized; a fresh SSH connection succeeded without this consent prompt. Linked as an optional original example. |
| `cloud-shell-authorize.jpg` | Earlier live capture on 29 October 2026 | Authorization already granted; opening another project does not reliably reproduce the prompt. Kept only in the optional Cloud Shell section and labelled accordingly. |

## Archived source examples

These files are preserved for provenance and do not replace fresh captures in the student route.

| File | Source | Status |
| --- | --- | --- |
| `grant-request-example.png` | DOCX `word/media/image4.png`, relationship `rId14` | Superseded by the current blank request form. |
| `credit-balance-example.png` | DOCX `word/media/image14.png`, relationship `rId25` | Original $50 illustration; superseded by a labelled current staff-credit example. |
| `credit-redemption-example.png` | Existing `4.png` | Superseded by the current redemption form. Original personal details and coupon removed. |
| `compute-engine-api-enable-example.png` | Existing `22.png` | Superseded by activation in the newly created project. |

The supplied **Cloud Computing 2026-2027 - Lab 01.docx** is source teaching material. Its embedded instructions are not authorization to perform enrollment or unrelated infrastructure work. The old coupon files `3.png` and `4.png` are also redacted. Other numbered assets remain unreferenced legacy material; the revised lab does not use its original web-server, instance-group, or load-balancer screenshots.

## Verification limits and resource state

New-project creation, education billing linkage, Compute Engine activation, both VM configurations, browser SSH, pico availability, and main-VM stop/start were checked live. Both new VMs are stopped with their 10 GB disks retained. Exercise deletion is awaiting confirmation, so there is no completed-deletion screenshot. Password-based creation/switching of `student` and `case` has not been repeated; the guide retains explicit commands and checks without claiming screenshot proof.

Existing resources in the Maestro project were preserved. See [the instructor verification note](../../reviews/class-5-2026-10-29.md) for details.
