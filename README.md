# FriendVenture API

**Advanced Front-End Portfolio Project(PP5) - Code Institute**

The *Friendventure API* is the backend for the FriendVenture application, built using Django Rest Framework. It serves as the foundation for a social network focused on organizing and participating in (sporting) activities with friends(to be), both indoor and outdoor.<br>

*FriendVenture API* is designed for users who want to create and join events, called "FriendVenture," which include a title, date, time, description, and location. Other users can confirm their participation or bookmark the FriendVenture for later. Each event is also open for comments, fostering communication and coordination among participants.<br>

Additionally, users have the ability to follow others, allowing them to stay updated on FriendVentures their friends/followees plan to post in the future.
<br>
The API is organized into several key apps:<br>

_friendventures_: Manages the creation and details of events.<br>
_profiles_: Handles user profiles and related information.<br>
_participants_: Tracks user participation in various events.<br>
_comments_: Enables users to comment on Friendventures.<br>
_bookmarks_: Allows users to save Friendventures they are interested in.<br>
_followers_: Facilitates the following and tracking of other users' activities.<br>
<br>
This API is designed to be consumed by a React frontend, providing a seamless experience for users looking to connect and engage in activities together.
<br>
<br>
The deployed API can be found here: [Friendventure API](https://friendventure-api-8b417af3d1a0.herokuapp.com/)<br>

## Table of Contents

- [User Experience](#user-experience)
- [Structure](#structure)
- [Database](#database)
- [Features](#features)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Bugs](#bugs)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Tools](#tools)
  - [Frameworks](#frameworks)
  - [Libraries and modules](#libraries-and-modules)
- [Testing](#testing)
  - [Python Validator Testing](#python-validator-testing)
  - [Manual testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Browser Compatibility](#browser-compatibility)
- [Deployment](#deployment)
  - [Heroku](#heroku)
  - [Local deployment](#local-deployment)
  - [Forking this GitHub repository](#forking-this-github-repository)
  - [Clone this repository](#clone-this-repository)
  - [Cloudinary](#cloudinary)
  - [Create PostgreSQL using Code Institute Database Maker](#create-postgresql-using-code-institute-database-maker)
- [Credits](#credits)
  - [Code](#code)
  - [ReadMe](#readme)
  - [Acknowledgments](#acknowledgments)


## User Experience (NEEDS UPDATE)

I used an Agile methodology approach to plan this project. This was implemented through the GitHub Project board with milestones, epics, user stories and tasks.
Each user story was classified with a label according to MoSCoW prioritization.<br>
The Kanban board can be seen [here](https://github.com/users/queenisabaer/projects/4).

More about the user stories can be found in the Readme for the frontend part that can be found [here]()

## Structure (NEEDS UPDATE)

The first database schema was crafted during the planning phase of the project and was created with [dbdiagramm](https://dbdiagram.io/home).

![Initial Database Schema](documentation/readme)<br>
Final ERD:<br>
![Final Database Schema](documentation/readme/)<br>

## Database<br>
I used a PostgreSQL provided by Code Institute as relational database.<br>

- **FieldTypes:**<br>
  - AutoField: An integer field that automatically increments.
  - CharField: A text field with a maximum length.
  - EmailField: A CharField that checks if the value is a valid email address.
  - DateTimeField: A field for storing date and time.
  - DateField: A field for storing dates.
  - TimeField: A field for storing time.
  - TextField: A large text field.
  - ImageField: A field for storing images
  - OneToOneField: A one-to-one relationship.
  - ForeignKey: A many-to-one relationship.
  - IntegerField: An integer field.
  - EmailField: An email field<br>
- **Relationships:**<br>
  - A User has one Profile.
  - A Profile belongs to one User.
  - A Friendventure is created by one User.
  - A User can create many Friendventures.



## Features

### Existing Features

<details>
<summary> User Authentication </summary>
<br>

Users can sign up for an account and login. When a user signs up, the profile is created automatically. <br>

</details>

### Features, which I would like to implement in the future

- tagulous for tags
- Messaging between users
- 


## API Endpoints


## Bugs

<details>
<summary> 404 error on default profile image link in admin console</summary>
<br>
When attempting to click on the link for the default profile image in the admin console, a 404 error was displayed. After trying various approaches and consulting with tutor support, we identified different Django versions as a potential issue. The problem was resolved by downgrading from Django 5 to Django 4.

It is important to note that the issue was not directly caused by Django itself but by the Django Cloudinary Storage plugin, which has not been updated since 2020 and is therefore not compatible with Django 5.
<br>
<br>

![Screenshot of the error message in browser](/documentation/bugs/bug_django5.png)<br>

</details>

<details>
<summary> Error during test for logged-in user creating a new friendventure </summary>
<br>
When setting up the test to ensure that only a logged-in user can create a new friendventure, the following error was displayed in the terminal:<br>

_[ErrorDetail(string='The submitted data was not a file. Check the encoding type on the form.', code='invalid')]_<br>

The error message indicates that the image field is expected to be a file upload, but the submitted data is not a valid file. I suspected that this was because the ImageField was not set to blank=True and my testimage had the wrong path. After adding the attribute to the model and migrating it to the database, the test executed without any issues.
<br>
<br>

![Screenshot of the error message in the terminal](/documentation/bugs/bug_imagefield_friendventure.png)<br>

</details>

<details>
<summary> Axios error during log in </summary>
<br>
When tryning to log in to an account in my frontend project, the following error was displayed in the console:<br>

![Screenshot of the error message in the console](/documentation/bugs/bug_log_in.png)<br>

I assumed it was because of the newest version of dj-rest-auth, that I am using and the settings I did with the walkthrough project(using an older version). In previous versions, settings such as JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, etc., were accessed directly from the settings module. However, the new structure requires accessing these settings through the REST_AUTH dictionary. After updating my settings file and trying to deploy it to heroku, the building process failed. <br>

![Screenshot of the error message in the console](/documentation/bugs/bug_log_in2.png)<br>

The error occurred because JWT-related settings were being imported into the views.py directly from settings.py, while in the new version of dj-rest-auth, these settings are now nested within the REST_AUTH dictionary. To resolve this issue, I updated the views.py file to access the JWT settings from the REST_AUTH dictionary rather than importing them directly.
<br>
<br>

</details>

<details>
<summary> CORS policy error </summary>
<br>
When working on the EditFriendventureForm, from one second to the next, I wasn't no longer able to interact with the site. In the console it showed the following error:<br>

![Screenshot of the error message in the console](/documentation/bugs/bug_cors.png)<br>

At first I thought the server was down, as it seemed to be really sudden and not related to my work on the code. After a certain time had passed, and I still could not access the site, I contacted Tutor support. I had to edit the settings in relation to the CLIENT_ORIGIN_DEV, after which I could access everything again. 
<br>
<br>

</details>



## Technologies Used

### Languages:
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Tools:
- [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub](https://github.com/) was used to save and store the files for the website.
- [GitHub Issues](https://docs.github.com/en/issues) have been used for Agile methodology by assigning user stories to issues and using labels to organize user stories.
- [GitHub Projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) have been used for Agile sprint planning and task tracking.
- [Heroku](https://www.heroku.com) was used to deploy the application.
- [CI Gitpod](https://codeinstitute-ide.net/) was used as IDE. 
- [Code Insitute Database Maker](https://dbs.ci-dbs.net/) PostgreSQL database hosting for this project
- [Black Formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) to beautify the code
- [LanguageTool](https://languagetool.org/) was used to check the grammar and spelling in the README and the Code. 
- [Pixelied](https://pixelied.com/convert/jpg-converter/jpg-to-webp) was used to convert jpg images into wepb images.
- [Tinypng](https://tinypng.com/) was used to compress the webp background-image.
- [Pixabay](https://www.pixabay.com/de-de/) was used to search and load the ghost for the logo.
- [Browserling](https://www.browserling.com/) was used to test the application on different browsers.
- [Cloudinary](https://cloudinary.com/) was used to store the item images.
- [Canva](https://www.canva.com/) was used to create the logo and the default image for a friendventure.
- [Favicon.io](https://favicon.io/favicon-generator/) was used to create the favicon.
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools?hl=de) were used to check the application for responsiveness and errors. 

### Frameworks:  
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))


### Libraries and modules:
- [os](https://docs.python.org/3/library/os.html) provides functions to interact with the operating system. 
- [sys](https://docs.python.org/3/library/sys.html) was used to get system-specific functions.
- [datetime](https://docs.python.org/3/library/time.html) supplies classes for manipulating dates and times.
- [Gunicorn](https://gunicorn.org/) provides a way to serve Python web applications.
- [Pycopg 2](https://pypi.org/project/psycopg2/) is a PostgreSQL database adapter for Python.
- [django-allauth](https://pypi.org/project/django-allauth/): was used to handle authentication and user management for Django
- [dj_database_url](https://pypi.org/project/dj-database-url/) enables the ability to represent their database settings via a string.
- [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/): was used to connect Cloudinary as Django file storage
 
- [django-cors-headers](https://pypi.org/project/django-cors-headers/): Handle Cross-Origin Resource Sharing in Django
- [django-filter](https://pypi.org/project/django-filter/): Provides filtering with URL parameters for querysets

## Testing

The app was tested regularly and deployed to Heroku to make sure both local and remote worked the same.

### Python Validator Testing (NEEDS UPDATE)

- All created python files were checked with the [Code Insitute validator - CI Python Linter](https://pep8ci.herokuapp.com/#). <br>

### Manual Testing



### Automated Testing
To cover all the user story scenarios, the following automated tests have been written into the Friendventure API. <br>


### Browser Compatibility
  The tests were conducted using the following browser:

- Google Chrome Version 127.0.6533.120 <br>

## Deployment (NEEDS UPDATE!)

### Heroku
This site is deployed using Heroku. To deploy it from its GitHub repository to Heroku, I took the following steps:

1. Create a list of requirements in the requirements.txt file by using the command _pip3 freeze > requirements.txt_
2. Log in (or sign up) to Heroku
3. Click on the _New_ button and select _Create new app_
4. Give it a unique name and choose the region _Europe_
5. Click the *Settings* tab, go to the _Config Vars_ section and click on the _Reveal Config Vars_ button
6. Add all variables from *env.py* to _ConfigVars_ of Heroku
![Screenshot of config vars](documentation/readme/)<br>
7. Click the _Add_ button
8. Click the *Deploy* tab, go to the _Deployment method_ section, select _GitHub_ and confirm this selection by clicking on the _Connect to Github_ button
9. Search for the repository name on github _friendventure_ and click the _Connect_ button
10. Add in the setting.py the Heroku app URL into ALLOWED HOSTS<br>
11. Gather all static files of the project by using the command _python3 manage.py collectstatic_ in the terminal
12. Make sure that DEBUG=FALSE in settings.py
13. Create a _Procfile_ in the root directory and add *web: gunicorn fv_api.wsgi*
13. In Heroku enable the automatic deploy or manually deploy the code from the main branch

To see the [view of the live site](https://friendventure-api-8b417af3d1a0.herokuapp.com/) click on the _Open app_ button in the top right corner or, if you enabled automatic deploy (step 13), log in to GitHub, navigate to the repository for this project by selecting [*queenisabaer/friendventure*](https://github.com/queenisabaer/friendventure), click on the _Deployments_ heading and choose in the _Environments_ section xxx. On top of the latest deployment is the link to the [live site](https://friendventure-api-8b417af3d1a0.herokuapp.com/).<br>

### Local deployment

1. Generate an env.py file in the root directory of the project
2. Configure the environment variables within this file.
3. Create a virtual environment
4. Install all required dependencies using _pip install_ command into the .venv
5. Add dependencies to the requirements.txt file using _pip3 freeze > requirements.txt_ command

### Forking this GitHub repository
1.  Log in to GitHub.
2.  Navigate to the repository for this project by selecting [*queenisabaer/friendventure*](https://github.com/queenisabaer/friendventure)
3. Click at the top of the repository on the **Fork** button on the right side

### Clone this repository
1. Log in to GitHub.
2. Navigate to the repository for this project by selecting [*queenisabaer/friendventure*](https://github.com/queenisabaer/friendventure)
3. In the top-right corner, click on the green *Code* button
4. Copy the HTTPS URL in the tab *Local*
5. Go to the code editor of your choice and open the terminal
5. Type `git clone` and paste the URL you copied into your terminal
6. Press the enter key

### Cloudinary
1. Navigate to [Cloudinary](https://cloudinary.com/)
2. Sign up or log in to account
3. Go to the dashboard
4. Click on _Go to API Keys_ button
5. Generate a new API Key
6. Provide the API environment variable in format: *CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@ds5rjhhxu* in _env.py_ and _Config Vars_
7. Update settings.py

### Create PostgreSQL using Code Institute Database Maker
1. As Student of the Code Institute, navigate to the [CI Database Maker](https://dbs.ci-dbs.net/)
2. Input your email address
3. Paste the provided URL in as your DATABASE_URL value

## Credits

### Code
- The initial setup and overall architecture of this project were guided by the Code Institute's Django Rest Framework walkthrough project. The core elements of the Profile, Friendventure, Follower, Bookmark, Participant, and Comment models, along with their respective serializers, filtering capabilities, and tests, were derived from the walkthrough project and subsequently tailored to meet the unique requirements of this project.
- A great help and inspiration were the advanced frontend projects by [Kelly Hutchinson](https://github.com/quiltingcode/events-backend-api), [Ronja Sjögren](https://github.com/Ajn0r/pet-palace-api), [Johannes Bernet](https://github.com/nacht-falter/sonic-explorers-api), and [Shubham Sinha](https://github.com/Sinha5714/pp5-api-ref/tree/main/pp5_api)

- How to Create and Use Signals in Django (To automatically include user who owns a friendventure as participant.) was found in an article by kt775629 at [GeeksForGeeks](https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/)

- The following websites were used as a source of knowledge: <br>
  - [Google](www.google.com)
  - [mdn](https://developer.mozilla.org/en-US/)
  - [W3C](https://www.w3.org/)
  - [W3schools](https://www.w3schools.com/)
  - [DevDocs](https://devdocs.io/)
  - [Stack Overflow](https://stackoverflow.com/)
  - [reddit](https://www.reddit.com/)
  - [forum djangoproject](https://forum.djangoproject.com/)
  - Documentation for [Django](https://www.djangoproject.com/), [Django Rest Framework]((https://www.django-rest-framework.org/)), [Cloudinary](https://cloudinary.com/documentation)
  - Slack Community

### ReadMe

- One last time, a big thank you to [Kera Cudmore](https://github.com/kera-cudmore) and all of her tips on what makes a good README.


### Acknowledgements

- Tutor support.
- Gareth MCGirr

**This is for educational use.**