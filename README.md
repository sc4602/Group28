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

Import Data
-----------------


Models
-----------------

Views
-----------------
### Map
In the map web page, you can view the distribution of 100-randomly-picked-up squirrels in Central Park whiched are marked up by their unique_squirrel_id. A function named display_map is used to display the map. This function returns to a squirrel/map.html. You can call this function by entering the [/map](https://tools-for-analytics-254314.appspot.com/sightings/).

### List All Squirrels
You can view a list of unique_squirrel_id of all the squirrels in a table, above which a green button named add is presented for you to add a new squirrel. In the end of each row of squirrels in the table, there are two buttons named edit and delete. You can realize the add, update and delete functions by pressing these buttons respectively.

See the list of squirrels by entering [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/).

Click the add button to enter the add-page [/sightings/add](https://tools-for-analytics-254314.appspot.com/sightings/add).

Click the edit button to enter the update-page [/sightings/<unique_squirrel_id>](https://tools-for-analytics-254314.appspot.com/sightings/<unique_squirrel_id>).

Click the delete button to delete a squirrel [/sightings/<unique_squirrel_id>](https://tools-for-analytics-254314.appspot.com/sightings/<unique_squirrel_id>).

### Add Squirrel
When you enter this adding page by clicking add button, you can fill out the information of the squirrel you want to add.For some fields, you need to click the button to choose between some available choices like True and False or something else. After filling out the information, click submit button below and you will be redirect to [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/) where you can find your newly-added squirrel by searching it's unique_squrrel_id.

### Edit Squirrel
When you enter this editing page by clicking edit button beside each squirrel, you can see all the detailed information of a specific squirrel. You now can make changes to any attributes. For some fields, you need to click the button to choose between some available choices. The old attributes are marked up by dash lines on each side to distinguish with any new changes you make.
After this, click submit button below to and you will be redirect to [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/) where you can find your newly-updated squirrel.

### Delete Squirrel


Export Data
-----------------



<div align="center">
  <img src="https://dev.pandas.io/static/img/pandas.svg"><br>
</div>

-----------------



  

 
