### Simple Adverising Project linear Regression

### Softwares and Tools Required

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
2. [VS Code IDE](https://code.visualstudio.com/)
3. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

- Create a new environment 
```
conda create -p venv python==3.9.7 -y
```
- Create requirements.txt file to install required libraries and install them by following command
```
pipreqs
pip intall -r requirements.txt
```
- Create app.py file which contains code for web page by using flask web framework.

- Create a templates folder, it contains html files.

- Create Procfile, in which I provide a command for our app deployment process in Heroku
```
web: gunicorn app:app
```

- After all set up, I push files to my github repository by following commands from command prompt
```
git add 'file_name' # add file to github 
git commit -m 'commit message'  # to tell the commit message 
git push origin main # push file to git repository from origin to main branch
```

