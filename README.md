![Example badge](https://github.com/tschoolderman/CD-assignment/actions/workflows/main.yml/badge.svg)
# Assignment-cd

Three components and their problems of my assignment:  
- [Assignment-cd](#assignment-cd)
  - [Creating the ssh-key](#creating-the-ssh-key)
  - [Setting up the Digital Ocean server](#setting-up-the-digital-ocean-server)
  - [Updating the Flask-app](#updating-the-flask-app)
  
---
&nbsp;
## Creating the ssh-key
There are several ways of creating an ssh-key. With using PuTTY I managed to create keys and connect to my server with it, I tried to make it into a GitHub action. I failed to get a GitHub to connect to my server.  
After some further reading, I settled on creating an ssh-key on the server and use this to connect with. Putting the `SSH_KEY` (private-key), `SSH_HOST` (IP-address) and `SSH_USERNAME` into GitHub secrets and using the Public-key in my "SSH and GPG keys"-setting on GitHub. 

---
&nbsp;
## Setting up the Digital Ocean server
After the creation of the server it was upgraded by using `apt update` and `apt upgrade`. The webserver NGINX is installed. To use the Flask-app created the server needs to have Flask and gunicorn installed and configured. First, pip had to be installed with `apt install python3-pip` before being able to pip-install Flask and gunicorn. The server was setup by using the configurations as shown in the exercises.  

---
&nbsp;
## Updating the Flask-app
To connect to the server with GitHub Actions there are multiple ways. I settled on using the ssh-action from appleboy, since it seemed the simplest way to do. The connection was made and I was able to clone my GitHub repository to the server. A script was made in the GitHub Actions to change to the `/home/` directory and `clone` the repository. Whenever a `push` event was done to the repository the action gave an error. I found out that a `clone` can only be made the first time, hereafter a `pull` has to be used to apply the changes made to the GitHub repository.  
Changing a `clone` to `pull` was not enough. The error: `err: fatal: not a git repository (or any of the parent directories): .git` popped up. Making the script change directory in the server, before issueing the `pull` action fixed this.  
To make sure a change is seen in the Flask-app the service of the application needs to be restarted by using: `systemctl restart assignment-cd.service`.
