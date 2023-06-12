VGDB Portfolio Project

Summary:
-design and implement the back end for a web-based application with a database component

Implement a 2-tier architecture that includes a Postgres database and the web-based application that interacts with the database. 

Use Docker Compose to define and manage the tiers. 

Be pushed to an online repository on GitHub.

Be deployed to the cloud. 

Front End deployment can be added later in the future. 

Steps taken in 4 weeks:

Week 1, you will begin the design of a web-based application that you will containerize as a multi-container application using Docker Compose. What are the various features you would like your project to offer? 
-I'll add an example of each of the standard API endpoints: (POST, GET, PUT, PATCH, and DELETE.)
-I need to insert more data into Tables just to get a better example of how it will work, maybe a sample size of 10-20 in each table.





Provide a description of the database tables required for your application, including column names, data types, constraints, and foreign keys. Include your database name. You can optionally include an ER diagram. 

I might use the DB from the SQL course we just did or possibly do something new like a zoo DB.
 

	-diagram of DB tables added to root project folder.

In Week 2, you will apply what you learned in Week 1 to begin building your application and push it to an online repository.
-setting up VENV before containerization (maintain control over your Python environment & dependencies.)
-(python -m venv . venv) and open new terminal where its says venv.
-pip install --upgrade pip (installed to latest pip version 23.1.2), installed python package manager that will let you install packages that are not default.
-created a folder "app" and added a requirements.txt file:
django==3.2.2
gunicorn==20.0.4
djangorestframework==3.12.4
python-decouple==3.4
psycopg2-binary==2.9.1
-to install = pip install -r requirements.txt, pip list to check what was installed.

Docker:
Docker packages software into standardized units called containers that have everything the software needs to run including libraries, system tools, code, and runtime. Basically we are going to put all our project files and dependencies in a container using or VENV. Easy way to avoid conflicting files/versions/etc.
-Ran docker ps -a to make sure no container were active to avoid conflict. 


Django, python web framework, takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel
-Use django_admin to scaffold out the Django project:
"django-admin startproject vgdb_django ." (creates your management app and the manage.py file right inside your current working directory)
in the settings.py file that was created, I commented out the DB section to turn off the connection for now.
-testing django to see if it will connect via terminal command "python manage.py runserver 8000" and then turning it off. 
			
						Docker Compose, PostgreSQL, pgAdmin

-In the APP Folder, froom the command pallette "Add Docker Files to Workspace" ... this creates the dockerignore, dockerfile, and manage.py files for containers.
- build a Docker image and run a container for the current Django app (image has been checked and container has been created) tested with http://localhost:8000/ basically... Docker container for a Django app has been setup. 

-django_init.sql was created in data/misc folder, contains standard settings for initializing a SQL DB, will be referenced in yml file as well.
-docker-compose.yml file created.It allows to deploy, combine, and configure multiple docker containers at the same time.
yml file contains container for web server, postgres db, and pgadmin client.
Ran docker compose down (stop and remove) and started containers again by using docker compose up -d for detached mode.
-Created new server in PG Admin 4 at localhost/5433 (5433 was set in the yml file)... user is postgres/pass is default admin.

-"docker compose down --rmi all" :this stops containers and removes all images at same time*

Implement password protection with .env and python-decouple, add into .env file and make sure it is in gitignore/dockerignore file. 

docker compose exec web python manage.py migrate --noinput
-migrated to generate default django tables. Since image was rebuilt, pgadmin server will have to be re-created as well. 

-Created and pushed to githib repo (https://github.com/rnqb/vgdb_django_db.git)

- Need to create my DB tables with Django built in ORM now. 

Django automatically converts Python class/object code to be raw SQL
- so we wrote some class/object code to interpret my tables scheme.
-started by creating model.py file with Django ORM to create database tables. 
-note wasn't sure on how to set foreign keys with django ORM after some research, but I can just do this in PG Admin. 

Now that we have Django ORM code that translates into RAW SQL, we will need to migrate the code to PGSQL DB. 
python manage.py migrate --run-syncdb had to be run in terminal in order to see tables in PGADMIN. 


- Need to setup Insomnia to do CRUD actions to  DB tables. 
- Used Django for my project, need to setup pytest with it somehow. 


	
	

	

	 



Week 3, you will continue building out your application in Docker Compose, and you will begin to add tests to it. 

In Week 4, you will attempt to deploy your application to one of the Big Three Cloud Service Providers. Alternatively (or additionally), you will build a GitHub Actions workflow to automate building and testing your application.