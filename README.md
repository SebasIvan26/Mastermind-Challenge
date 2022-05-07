# Mastermind Board Game

![image](https://user-images.githubusercontent.com/56465638/166859196-0b88dfe6-a721-4ca3-8ba6-5cc9512ea9da.jpeg)


Mastermind is a code-breaking game. One player decides a secret code of four colors, and the other player has ten chances to crack the code. the computer will generate a 4 number combination code which the user must attempt to break within 10 attempts. The generated numbers by the computer can be selected from a total of 8 different numbers chosen randomly. 

For the rules of Mastermind, see this [Wikihow article](https://www.wikihow.com/Play-Mastermind).

###### Impelemented Extensions
- Adaptable difficulty level and adjust numbers used
- Added Sound to website
- Capacity to provide hints
- User login/registration feature
- Interact with other players through Message Board (Players can interact !!)

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.sqlalchemy.org" target="_blank" rel="noreferrer"> <img src="https://hakin9.org/wp-content/uploads/2019/08/connect-a-flask-app-to-a-mysql-database-with-sqlalchemy-and-pymysql.jpg" alt="mysql" width="60" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## Views/Screenshots

#### Homepage

![mainpage](https://user-images.githubusercontent.com/56465638/166859236-4c5ecdc9-3030-4433-a15d-def32546c44f.png)

---

#### Choose level 

![level choosing](https://user-images.githubusercontent.com/56465638/166859249-cc6cd2d6-5b0e-491e-98cc-738244c81294.png)





---  


#### Game Interface. Also provides the ability to view hints/previous guesses

![Show hints](https://user-images.githubusercontent.com/56465638/166859281-28a695cf-5871-4eb0-af7a-737ac1e6b9c2.png)





---  

#### Message board page where people can hold conversations in the form of posted messages

![message board](https://user-images.githubusercontent.com/56465638/166859292-9c6ff18b-4049-42c2-ab2d-d7e2c03d4f7f.png)





---  

#### Registration Page with expandable navigation bar

![Registration](https://user-images.githubusercontent.com/56465638/167274502-bcb2b4bc-facc-42a8-92d1-c1f409928fa4.png)






## Folder Structure

- ##### [game](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/game)
  - forms template for when user is submitting their guess to the computer
  - support functions for game ex: generatenumbercombination() for user to figure out 
  - session for ability to share data between requests
  - all routing related to game ex: restart game, show hints etc
  - game logic

- #### [templates](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/templates)
  - HTML templates for each webpage
  - Javascript for page animation
  - Bootstrap for styling/components etc

- ##### [error_pages](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/templates/error_pages)
    - handlers to perform exception handling when user visits invalid page or makes an invalid call

- ##### [core](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/core)
  - routing of core pages such as Homepage/ About us/ Discussion Board posts
  - __init__.py file to mark directories as Python package

- ##### [users](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/users)
  - forms template for userlogin, userregistration and userupdates
  - picture handler for user to update profile picture
  - routing for loggin in user, registrating user, logout, viewing account, showing all posts from user on discussion board 
  - Bootstrap for styling/components etc

- ##### [blog_posts](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/blog_posts)
  - forms template for when user is posting to the discussion board
  - routing of when user is creating a post
  - routing of when user is updating their post 
  - routing of when user is deleting their post
  - Retrieves blogpost object from database

- ##### [static](https://github.com/SebasIvan26/Mastermind-Challenge/tree/main/mastermindweb/static)
  - stores default profile pic for user, audio for webpage

- ##### [parent folder](https://github.com/SebasIvan26/Mastermind-Challenge) 
  - creates flask app
  - assign secret key (for purposes of this project only, this is visible)
  - database set up --> choice: SQLAlchemy for ORM use since small database (abstraction not a factor)
  - sets up database model 




## Setup & Installtion

Make sure you have the latest version of Python installed.

```bash
git clone <repo-url>
```

```bash
pip install -r requirements.txt
```

## Running The App

```bash
python app.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`

## Deployed

Alternatively, web app is deployed on Heroku at the following link  [`https://mastermindv1.herokuapp.com`](https://mastermindv1.herokuapp.com)

