### Lab 3: Part 1

In this tutorial, you will learn how to create a MongoDB cloud account and set up a database that you will later connect to your Node.js application.

##### What is MongoDB?

[MongoDB](https://www.mongodb.com/) is a free, cloud-based NoSQL database that stores data in a flexible, JSON-like format. Unlike traditional SQL databases (which use tables and rows), MongoDB organizes data into collections (similar to tables) and documents (similar to rows). This makes it easier to work with modern applications that handle data as APIs in different shapes and structures.

By the end of this lab, you will be able to:

- Create and configure a MongoDB Atlas account (the cloud version of MongoDB).
- Deploy your first database cluster using the free plan.
- Add collections and documents (the MongoDB terms for tables and rows).
- Obtain and configure your database connection string for Node.js.

This is an essential step before integrating MongoDB with your backend code in the next part of the lab.

> ⚠️ **Important:** Follow each step carefully and double-check your input, especially usernames, passwords, and database names. Any small typo may prevent your Node.js code from connecting to the database later.

---

##### Setting up a MongoDB database

1. Visit the [MongoDB website](https://account.mongodb.com/account/login) and register using your **personal email** (e.g., your Gmail account).  
   - Sign in and accept the terms.  

![Screenshot 2025-10-07 at 17.04.34](assets/mongo1.png)

2. Complete the personalized setup questions, or simply skip them.  

![Screenshot 2025-10-07 at 17.05.04](assets/mongo2.png)

3. On the next screen, choose the **Free** option and click **Create Deployment**.  

![Screenshot 2025-10-07 at 17.05.19](assets/mongo3.png)

4. Create your administrator user:  
      - Choose a username and password that you can remember. 
      - Click **Create Database User**, then **Close**.  
      - **Important:** Write down your username and password, as you’ll need them later. 

![Screenshot 2025-10-07 at 17.05.53](assets/mongo4.png)

5. In the left-hand menu, go to **Network Access**.  

   - Click **ADD IP ADDRESS** → **ALLOW ACCESS FROM ANYWHERE**.  This tells MongoDB Atlas to accept connections from any device, regardless of its IP address. Without this, only specific IPs you add can connect.
   - Then click **Confirm**.  

![Screenshot 2025-10-07 at 17.06.39](assets/mongo5.png)

6. Go back to the clusters and wait about five minutes for your cluster to be deployed.  

![Screenshot 2025-10-07 at 17.06.56](assets/mongo6.png)

7. When you cluster is ready you are good to go.

![Screenshot 2025-10-08 at 07.52.39](assets/mongo7.png)

8. Once the cluster is ready, click **Browse Collections**, then **+ Create Database**.  

> ⚠️ **Important:** Please use the exact names provided here. Do not change them yet, as we’ll be using these names in the code. Later, you’ll have the chance to create your own database.

* Database name

  ```json
  DBFilms
  ```

* Collection name

  ```json
  ColFilms
  ```

![Screenshot 2025-10-08 at 07.53.47](assets/mongo8.png)

9.  Click **INSERT DOCUMENT** and add the following data.  
      - Type carefully and double-check everything, any typo will prevent the code from retrieving your data. The `_id` is generated automatically, so do not edit it.

   ```json
   {
     "title": "The Hobbit: An Unexpected Journey",
     "year": "2012",
     "genre": "Adventure",
     "director": "Peter Jackson",
     "rating": 7.8
   }
   
   ```

   > Note that `rating` is a `Double`.

      - Once done, click **Insert**.  

![Screenshot 2025-10-08 at 07.56.54](assets/mongo9.png)

10. Your data should now appear in the collection.  

![Screenshot 2025-10-08 at 07.57.18](assets/mongo10.png)

11. Add a second document (row) so that your collection looks like this example.

```json
{
  "title": "Jaws",
  "year": "1975",
  "genre": "Thriller",
  "director": "Steven Spielberg",
  "rating": 8
}
```

12. So my final collection looks like this.

![Screenshot 2025-10-08 at 07.59.36](assets/mongo11.png)

11. Go back to **Clusters** in the left-hand menu and click the **Connect** button.  

![Screenshot 2025-10-08 at 07.59.54](assets/mongo12.png)

12. Select Node.js to and **Copy** the **connection string** shown on screen. This is how Node.js will connect to your database.  

![Screenshot 2025-10-08 at 08.00.06](assets/mongo13.png)

13. Open a text editor (notepad in windows or textedit in mac) to paste an d adjust the connection string. Paste it there.

![Screenshot 2025-10-08 at 08.00.33](assets/mongo14.png)

14. Before we proceed to the next part, you will need to adjust the connection url with the information from the database. You will to add your password created in `Step 4` and the database name created in `Step 8`. See the screenshot bellow on where to edit this information.

![mongo15](assets/mongo15.png)

You need to edit the connection string:

- Replace `<db_password>` with the password you created (without the `< >` brackets).
- For example, if your username is `mary` and your password is `1234`, it should look like:

```shell
mongodb+srv://mary:1234@cluster0.h3mixcq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
```

> ⚠️ **Important:** Make sure you remove the brackets `< >`.

15. Add your database name to the URL between the `...net/` and the `?retry...`. In this case, the database is called `DBFilms`.  The final connection string should be like that:

![mongo16](assets/mongo16.png)

> ⚠️ **Important:** Double-check that your **username**, **password**, and **database name** are all correct.
>
> Note that each time you create a new database, you will need to adjust the database name.

17. Save this file somewhere safe on your computer for later use.

✅ Well done! Your MongoDB account and first database are now set up. Let’s move on to the next step.

