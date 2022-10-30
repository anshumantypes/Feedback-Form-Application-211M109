
# FEEDBACK-FORM-APPLICATION
This is my 1st task of GDSC NITK
go through readme completely
## please note
## Currently there is an issue if you run this project with NITK-NET wifi,please use your mobile hotspot or some other net for this to work

the following screenshot is when you use NITK-NET

![2022-10-28](https://user-images.githubusercontent.com/114809998/198569398-d5cc07fa-c054-487c-80f5-83c4e8653078.png)


## Documentation

i used Django framework to create this feedback form [djangoproject](https://docs.djangoproject.com/en/4.1/)



## About Django
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

1. It is fast
2. it is secure


## Installation

It is strongly recommended that you use a released version.follow the [Instruction](https://docs.djangoproject.com/en/4.1/topics/install/) to install

    
## About the project
this FEEDBACK FORM is capable of storing all the data you submit in the django admin data base and also send the mail to the mail id entered in the FORM
## screenshots

![2022-10-28 (1)](https://user-images.githubusercontent.com/114809998/198575542-d2566d39-8091-429e-a65e-c9c2b0f6d64e.png)
![2022-10-27 (6)](https://user-images.githubusercontent.com/114809998/198315403-5a655b0b-6537-4707-a035-18d3ff817d55.png)
![2022-10-27 (8)](https://user-images.githubusercontent.com/114809998/198315032-5f739782-2039-4682-8e6b-ac9bad97629b.png)
## the django database
![2022-10-27 (10)](https://user-images.githubusercontent.com/114809998/198316219-80941f5a-3a86-4b13-9ced-1ec0d0f09405.png)
![2022-10-27 (11)](https://user-images.githubusercontent.com/114809998/198316366-a6091e98-2404-4449-ae99-c2b5a32990f0.png)

#### videos



https://user-images.githubusercontent.com/114809998/198323532-6fda44e9-03eb-49ab-8d8b-22077d527c28.mp4







## setup
1. before setup make sure python folder and python script folder is added in environment variable and install the latest version of django
2. clone this repo in an empty folder and open in an IDE,open the terminal and write
`cd feedback`
`python manage.py runserver`

3. now click the the link and use the form



## possible issues and solutions

if you are connected to NITK-NET then you will probably get this message after submitting the form:

#### Error: A connection attempt failed because the connected party did not properly

try running on your mobile hotspot or some other connection other than NITK-NET

___

how to see the database of all people who filled the form and there detail?
## IN the search box in google type \admin after the development server address ie. http://127.0.0.1:8000/admin

