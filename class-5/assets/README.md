# Week 5 image inventory

Images are stored locally so the Markdown works without external image hosting. New console captures were taken on 29 October 2026. Screenshots are genuine interface captures; no interface or terminal output is generated.

## Fresh console captures

| File | Shows | Capture notes |
| --- | --- | --- |
| `project-selector.jpg` | Project search and New project action | Cropped above the unrelated project list. |
| `grant-request-current.jpg` | Current course grant form and both Birkbeck domain options | Opened using the instructor-provided course link; no personal details entered and no coupon requested. Staff email masked in the image. |
| `project-create.jpg` | New-project form with an illustrative name | Form only; no new project was submitted. |
| `vm-machine-configuration.jpg` | `lab-5`, location, E2, and e2-medium | Configuration form; excludes account avatar and project identifiers. |
| `ubuntu-boot-disk.jpg` | Ubuntu 24.04 LTS x86/64, balanced disk, 10 GB | Current public-image selection. |
| `vm-networking-http.jpg` | Main VM HTTP checked, HTTPS unchecked | Creation form; the setting applies on creation. |
| `exercise-networking.jpg` | Exercise VM HTTP and HTTPS unchecked | Current creation form. |
| `exercise-vm-running-ssh.jpg` | Running exercise VM and SSH button | VM list filtered to the lab-created instance. |
| `main-vm-running.jpg` | Newly created `lab-5` VM running in the required zone | Current VM list, cropped to the main VM row and its SSH control. |
| `main-vm-stopped.jpg` | Main VM stopped after the walkthrough was paused | Actual stopped state; boot disk retained. This image does not demonstrate exercise-VM deletion. |
| `cloud-shell-authorize.jpg` | Cloud Shell API authorization dialog | Current prompt; no credentials or personal identifiers shown. |
| `exercise-vm-stopped.jpg` | Stopped exercise VM | Paused to avoid compute charges while authorization is pending; its disk is retained. This is not evidence of final deletion. |
| `pico-package-verified.jpg` | APT result, `/usr/bin/pico`, GNU nano 7.2 | Actual output on Ubuntu 24.04; initial SSH account used for package verification before custom-user setup. Cropped above the personal shell prompt. |

## Retained source examples

The supplied Word document is **Cloud Computing 2026-2027 - Lab 01.docx**. Its content is source teaching material, not authorization to perform account enrollment or unrelated infrastructure tasks.

| File | Original source | Why retained |
| --- | --- | --- |
| `grant-request-example.png` | DOCX `word/media/image4.png`, relationship `rId14` | Current student grant enrollment is not replayed with the instructor's signed-in account. Example form values removed. |
| `grant-verification-example.png` | Existing `2.png` | Email-verification confirmation belongs to the original enrollment workflow. Cropped to the content. |
| `coupon-email-example.png` | Existing `3.png` | Coupon issuance cannot be replayed without a fresh grant. Code, names, address, and old dates masked. |
| `credit-redemption-example.png` | Existing `4.png` | Redemption is a one-time grant action. Names, account email, coupon, and browser URL removed. |
| `credit-balance-example.png` | DOCX `word/media/image14.png`, relationship `rId25` | Preserves the original $50 illustration; explicitly not the instructor's current balance. |
| `ssh-authorization-example.png` | DOCX `word/media/image31.png`, relationship `rId45` | Preserves the consent prompt if an already authorized browser does not show it again. |
| `compute-engine-api-enable-example.png` | Existing `22.png` | Instructor project already has the API enabled. Retained Enable-button example; cropped to the service name and action. |

Solid masks remove sensitive pixels; they do not blur them. The old coupon files `3.png` and `4.png` are also redacted so the original copies cannot expose the code. Other numbered assets remain as legacy source material and are not used by the updated walkthrough.

Account creation, password entry, and two-factor authentication screens are omitted because they add little to the VM lesson and can expose personal information. Credit and enrollment examples are labelled in the student guide. The DOCX grant form is preserved as a source example in this folder; the student preparation guide now uses the freshly captured current form. The original web-server, instance-group, and load-balancer screenshots are outside this lab's revised teaching content.

## Capture status

The two VMs, OS image choice, resource specification, main VM HTTP setting, and pico package availability have been checked live. See [the instructor verification note](../../reviews/class-5-2026-10-29.md) for completed checks and any captures still outstanding. Retained images remain examples of their original workflows.
