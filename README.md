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
   
   
In order to meet Joffrey Hosencratz's demand, the web application is constructed with the [Django](https://www.djangoproject.com/) framework. This application can perform the following functions. First, it can show the distribution of squirrels on a map. Second, it shows the whole list with all the squirrels in the database with Add, Edit and Delete buttons on it. Besides, these 3 kinds of buttons can perform the adding, editing and deleting functions respectively. Finally, there is a stats page showing 5 attributes of all the squirrels in the database.



Build up Project and Application
-----------------
Create a django project called top under the directory and Create a django application called squirrel under the directory:
```
$ django-admin startproject top
$ cd top/
$ django-admin startapp squirrel
```

##### Note:
This project is done on our own terminal and no virtual environment has been set up.

Import Data
-----------------
All websites should have their own database. In order to construct the database and import the data into it, management/commands/import_squirrel_data.py is created in the outter top directory.
Considering the features of squirrels, longtitude(float), latitude(float), unique_squirrel_id(NVARCHAR), shift(NVARCHAR), date(Date), age(NVARCHAR), primary_fur_color(NVARCHAR), location(NVARCHAR), specific_location(Text), running(Boolean), chasing(Boolean), climbing(Boolean), eating(Boolean), foraging(Boolean), other_activities(Text), kuks(Boolean), quaas(Boolean), moans(Boolean), tail_flags(Boolean), tail_twitches(Boolean), approaches(Boolean), indiffernt(Boolean), runs_from(Boolean) are included into database. Besides, the types and maximum length are setted to the features.

### So how to use this command
The following command can be used to import the data from the 2018 census file (in CSV format), the file path should be specified after the management command:
```
$ python manage.py import_squirrel_data /path/to/file.csv
```
##### Note: Data in db.sqlite3
The data in db.sqlite3 is [the 2018 Central Park Squirrel Census data](https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv).

Views
-----------------
### Map
In the map web page, you can view the distribution of 100-randomly-picked-up squirrels in Central Park which are marked up by their unique squirrel ids. A function named display_map is used to display the map. This function returns to a squirrel/map.html. You can call this function by entering the [/map](https://tools-for-analytics-254314.appspot.com/sightings/).

### List All Squirrels
You can view a list of unique squirrel ids of all the squirrels in a table, above which a green button named Add is presented for you to add a new squirrel. In the end of each row of squirrels in the table, there are two buttons named Edit and Delete. You can realize the add, update and delete functions by pressing these buttons respectively.

See the list of squirrels by entering [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/).

Click the Add button to enter the add-page [/sightings/add](https://tools-for-analytics-254314.appspot.com/sightings/add).

Click the Edit button to enter the update-page [/sightings/<unique_squirrel_id>](https://tools-for-analytics-254314.appspot.com/sightings/<unique_squirrel_id>).

Click the Delete button to delete a squirrel [/sightings/<unique_squirrel_id>](https://tools-for-analytics-254314.appspot.com/sightings/<unique_squirrel_id>).

### Add Squirrel
When you enter this Adding page by clicking add button, you can fill out the information of the squirrel you want to add. For some fields, you need to click the button to choose between some available choices like True and False or something else. 

After filling out the information, click Submit button below and you will be redirected to [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/) where you can find your newly-added squirrel by searching it's unique squirrel id.

### Edit Squirrel
When you enter this editing page by clicking Edit button beside each squirrel, you can see all the detailed information of a specific squirrel. You now can make changes to any attributes. For some fields, you need to click the button to choose between some available choices. The old attributes are marked up by dash lines on each side to distinguish from any new changes you make.

After this, click Submit button below and you will be redirected to [/sightings](https://tools-for-analytics-254314.appspot.com/sightings/) where you can find your newly-updated squirrel.

### Delete Squirrel
When you click the Delete button, the squirrel beside will be deleted from the database. Then you will be redirected to the [/sightings] page where the corresponding squirrel has already been removed. 

Export Data
-----------------
The following command can be used to export the data to a csv file, the file path should be specified after the management command:
```
$ python manage.py export_squirrel_data /path/to/file.csv
```

Group Information
-----------------
##### top Group 28, Section 1

##### UNIs:[yl4296, sc4602]

##### server: https://tools-for-analytics-254314.appspot.com/


