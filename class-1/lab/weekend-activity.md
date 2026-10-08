### Week 1: Weekend Activity

This weekend, learn the GitHub basics, publish your University API homework, and share your work with the class.

#### Part A: Learn the GitHub Basics

**Git** tracks changes to your code. **GitHub** hosts Git repositories online so you can share your projects and collaborate with others. A repository is a place to store your project files and their change history.

Watch **videos 1–5 only**, in playlist order, from the official [GitHub for Beginners video series](https://www.youtube.com/playlist?list=PL0lo9MOBetEFcp4SCWinBdpml9B2U25-f).

Follow along with the examples. Practise creating a repository, recording changes with commits, and pushing your work to GitHub.

#### Part B: Publish Your Homework

1. Use your completed [Homework 1: University API](../homework/homework-1.md) project.
2. Create a GitHub account if you do not already have one.
3. Create an **empty public repository** for your homework, for example `week1-university-api`. Public means anyone can view it. Leave the README, `.gitignore`, and licence initialisation options unchecked on GitHub; you will add your project files locally before pushing. See [Creating a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) if you need help.
4. Add a `.gitignore` file to your project before committing. Include:

   ```gitignore
   .venv/
   __pycache__/
   *.pyc
   .env
   ```

5. Include `main.py`, `requirements.txt`, `.gitignore`, and your `routers` folder, including `routers/__init__.py`. Add a short `README.md` explaining what the API does, how to install its requirements, how to run it, and which URLs to test.
6. Commit your project files with a clear message, then **push your homework to the public repository** using what you learned in the tutorials.
7. Open the repository on GitHub and check that your files and README are visible. Your `.venv` folder should not be included; other students will create their own environment and install packages from `requirements.txt`.

#### Part C: Share and Review

Post your **GitHub repository link** in the Teams channel [Lab Exercises and Solutions](https://teams.microsoft.com/l/channel/19%3A7cb8bd3bc3084d559fd93a5d1372c6f4%40thread.tacv2/Lab%20Exercises%20and%20Solutions?groupId=0f8f51d6-f7ce-4a6e-beeb-249bd6aca600&tenantId=89d07f47-d258-463c-8700-635ffaeca38e). Include a short description of your University API and any questions you have.

Everyone is encouraged to review each other's repositories and leave helpful comments in the relevant Teams thread. Look at the code, README, and endpoint behaviour. Share what is clear, ask questions, and suggest improvements where needed. Keep feedback respectful and specific.

#### Completion Checklist

- You watched videos 1–5 of the official GitHub tutorials.
- You pushed your University API homework to a public GitHub repository.
- Your repository includes the code, requirements, `.gitignore`, and a README.
- Your repository excludes the virtual environment.
- You posted your repository link in the Teams channel.

**Recommended:** review classmates' work and comment where helpful.

Week 1 is complete!
