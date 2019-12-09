# Group28

<table>
<tr>
  <td>Python Version</td>
  <td>
    <a href="https://www.python.org/downloads/release/python-374/">
    <img src="https://img.shields.io/badge/Python-3.7.4-blue.svg?style=flat-square" alt="latest release"/>
    </a>
  </td>
</tr>
<tr>
  <td>Django Version</td>
  <td>
		<a href="https://www.djangoproject.com/download/">
		<img src="https://img.shields.io/badge/Django-2.2.7-green.svg?style=flat-square" alt="status" />
		</a>
  </td>
</tr>
<tr>
  <td>Download Squirrel Data</td>
  <td>
    <a href="https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw">
    <img src="https://img.shields.io/badge/Data-786KB total-orange.svg?style=flat-square" alt="license" />
    </a>
  </td>
</tr>
</table>   
   
   
In order to meet Joffrey Hosencratz's demand, we developped a web application with the [Django](https://www.djangoproject.com/) framework. This application can perform the following functions. First, it can show the the distribution of squirrel on a map. Second, it shows the whole list with all the squirrels in the database with add, edit and delete buttoms on it. Besides, these 3 kinds of buttoms can perform the adding, editing and deleting functions respectively. Finally, there is a stats page shows the attributes of all the squirrels in the database.



Build up Project and App Structure
-----------------
### Build up Project

Install pip:
```
$ pip install -U pip
```
Use [pip](https://pip.pypa.io/en/stable/) to install [django](https://www.djangoproject.com/) in your computer:
```
$ pip install django
```
Create a directory called Group28 to store our project:
```
$ mkdir Group28
```
Create a django project called top in the directory:
```
$ django-admin startproject top
```
This will create a top directory in our current directory Group28. In this directory, there are following files and directories, Let's look at what the startproject create:
```
top/
   manage.py
   top/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
The outter top directory is just a directory contains all the files and directories, the inner top directory is the real project.
### Build up Application
To build up our application, we change into the outter top directory:
```
$ cd top/
```
Create a django application called squirrel in the directory:
```
$ django-admin startapp squirrel
```
This will create a squirrel directory in our current directory top. In this directory, there are following files and directories, Let's look at what the startapp create:
```
top/
   manage.py
   squirrel/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	views.py
   top/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
Then add the application to the project by adding 'squirrel' into INSTALLED_APPS list:
```
$ vim top/settings.py
```

#### Note: 
This project is done on our own terminal and no virtual environment has been set up.

Import Data
-----------------
### Construct Management Commands directory
On the outter top directory we create a management directory:
```
$ mkdir management
```
Change into managenent directory:
```
$ cd management
```
Create a commands directory:
```
$ mkdir commands
```

### Our dataset
In this part, we want to realize a function to import the data into our database. Our dataset is collected from the
He would like to start keeping track of all the known squirrels and plans to start with Central Park. He’s asked you to build an application that can import the 2018 Central Park Squirrel Census data and allow his team to add, update, and view squirrel data.

### Import Squirrel data


Now our directory looks like this:
```
top/
   manage.py
   management/
   	commands/
		import_squirrel_data.py
   squirrel/
	__init__.py
	admin.py
	apps.py
	models.py
	tests.py
	views.py
   top/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```
 



Models
-----------------

Views
-----------------
### Map

### List All Squirrels

### Add Squirrel

### Edit Squirrel

### Delete Squirrel

Export Data
-----------------



<div align="center">
  <img src="https://dev.pandas.io/static/img/pandas.svg"><br>
</div>

-----------------



  

 
