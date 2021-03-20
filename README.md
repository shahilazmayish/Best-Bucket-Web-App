# Best Bucket v1.0
![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)

## Installation

Best Bucket requires [Python](https://www.python.org/) to run.

**Install [Python](https://www.python.org/downloads/)**
For software framework we are going to use Django...
**in project folder command prompt:**
```sh
pip install django
```
## Instalation of the database and database UI
**Install [Postgresql](https://www.postgresql.org/download/)**
> Note: `Install everything at default settings` is required.
>Password: `12123`
>Uncheck: `Lunch Stack Builder.. `
> Finish

**Install [PGadmin4](https://www.pgadmin.org/download/)**
>Open PGadmin4
>Password: `12123`
Server/Postgresql/Database/Create Database: **BestBucket**

## Install the dependencies and devDependencies and start the server
**in project folder command prompt:**
```sh
pip install psycopg2
pip install pillow
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
**Page Link: http://127.0.0.1:8000/**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

       
