### How to Redeem Your GCP Coupon and Create Your First Virtual Machine

1. In the Moodle **Preparation** tile, click the **Student Coupon Retrieval Link.**

   Use your **Birkbeck email** to complete the form.

![1](assets/1.png)

2. Check your email inbox and verify your account.  

![2](assets/2.png)

3. After a short while, you will receive a second email containing your coupon code.  

![3](assets/3.png)

> [!IMPORTANT]
>
> **From this point forward, use your personal Gmail account. Do not use your work's, organization’s or Birkbeck email.**
>
> **Only your personal email. If you don't have a personal gmail account please create.**
>
> Your Google Cloud coupon will be linked to your personal Gmail account, so make sure you redeem it there. This way, the coupon will stay yours.

4. **Enter the coupon code** on the screen and **click Accept and continue**.  

![4](assets/4.png)

5. In the search bar, look for **Compute Engine**. If it doesn’t appear, type it manually.  

![7](assets/7.png)

6. Create a new project: click on the project selector at the topleft corner (mine shows already acc-2026), then choose **New Project**.  

![11](assets/11.png)

7. Name your project as you like. I entered acc-2026.  

![13](assets/13.png)

8. Go back to **Compute Engine** and select **VM instances** from the sidebar.  

![8](assets/8.png)

9. Click **Create a new instance.** You’ll be taken to a screen asking you to enable the Compute Engine API — click **Enable** to continue.

![22](assets/22.png)

*Note: The screen may look slightly different in some cases. Follow the same and enable it.*  

![9](assets/9.png)

10. Now, let’s create a virtual machine (VM). Click **Create Instance** and rename it to **lab-1**.  

![14](assets/14.png)

11. Under **OS and storage**, click **Change** to select the operating system.  

![15](assets/15.png)

12. Choose **Ubuntu** as your operating system. Leave the rest of the configurations as they are.

![16](assets/16.png)

13. Go to **Networking** and enable both **HTTP** and **HTTPS** traffic.  That's all! Click on **Create** at the bottom of the page.

![17](assets/17.png)

14. Your VM will now begin creating.  

![18](assets/18.png)

15. After a minute, when it’s ready, click the **SSH** button.  

![19](assets/19.png)

16. Click **Authorize** to allow access.  

![20](assets/20.png)

17. You’re now ready to go! 🎉  

![21](assets/21.png)  

Try running a command like `ls`, which lists files and folders (you’ll see nothing yet).

18. Finally, delete the instance, we’ll create more in future labs.  

![22](assets/23.png)

**🚀 You’re all set for your first class!**
