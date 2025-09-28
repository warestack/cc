### How to Redeem Your GCP Coupon and Create Your First Virtual Machine

1. In the **Preparation** tile, click the coupon redemption link. Use your **Birkbeck email** to complete the form.  

![1](/Users/steliossotiriadis/Desktop/lab-1/assets/1.png)

2. Check your email inbox and verify your account.  

![2](/Users/steliossotiriadis/Desktop/lab-1/assets/2.png)

3. After a short while, you will receive a second email containing your coupon code.  

![3](/Users/steliossotiriadis/Desktop/lab-1/assets/3.png)

> [!IMPORTANT]
>
> **From this point forward, use your personal Gmail account. Do not use your organization’s or Birkbeck email.**

4. Enter the coupon code on the screen.  

![4](/Users/steliossotiriadis/Desktop/lab-1/assets/4.png)

5. In the search bar, look for **Compute Engine**. If it doesn’t appear, type it manually.  

![7](/Users/steliossotiriadis/Desktop/lab-1/assets/7.png)

6. Create a new project: click on the project selector at the top, then choose **Create Project**.  

![11](/Users/steliossotiriadis/Desktop/lab-1/assets/11.png)

7. Name your project as you like.  

![13](/Users/steliossotiriadis/Desktop/lab-1/assets/13.png)

8. Go back to **Compute Engine** and select **VM instances** from the sidebar.  

![8](/Users/steliossotiriadis/Desktop/lab-1/assets/8.png)

9. You will need to enable the Compute Engine API. Click **Enable**.  

![22](/Users/steliossotiriadis/Desktop/lab-1/assets/22.png)

*Note: The screen may look slightly different in some cases. Follow the same and enable it.*  

![9](/Users/steliossotiriadis/Desktop/lab-1/assets/9.png)

10. Now, let’s create a virtual machine (VM). Click **Create Instance** and rename it to `lab-1`.  

![14](/Users/steliossotiriadis/Desktop/lab-1/assets/14.png)

11. Under **OS and Storage**, click **Change** to select the operating system.  

![15](/Users/steliossotiriadis/Desktop/lab-1/assets/15.png)

12. Choose **Ubuntu** as your operating system.  

![16](/Users/steliossotiriadis/Desktop/lab-1/assets/16.png)

13. Go to **Networking** and enable both **HTTP** and **HTTPS** traffic.  

![17](/Users/steliossotiriadis/Desktop/lab-1/assets/17.png)

14. Your VM will now begin creating.  

![18](/Users/steliossotiriadis/Desktop/lab-1/assets/18.png)

15. After a minute, when it’s ready, click the **SSH** button.  

![19](/Users/steliossotiriadis/Desktop/lab-1/assets/19.png)

16. Click **Authorize** to allow access.  

![20](/Users/steliossotiriadis/Desktop/lab-1/assets/20.png)

17. You’re now ready to go! 🎉  

![21](/Users/steliossotiriadis/Desktop/lab-1/assets/21.png)  

Try running a command like `ls`, which lists files and folders (you’ll see nothing yet).  

18. Finally, delete the instance — we’ll create more in future labs.  

![22](/Users/steliossotiriadis/Desktop/lab-1/assets/23.png)