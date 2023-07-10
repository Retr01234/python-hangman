# Hangman Game - Python

## Introduction

For the 3rd Project of the Code Institute Course, I decided to make an Interactive Hangman Game where the User has to guess letters of a random word to try to win the game.

Hangman Game is a Single Player Game where a randomly generated word will be selected by the Computer and the User has limited tries to try and guess the Correct Word. Wether the Letter is correct or not, the User will receive real-time feedback.

Please find the live project [here:]() 

![AmIResponsive](images/responsive.jpg)

## Table Of Contents

+ [UX](#ux "UX")
  + [User Stories](#userstories "User Stories")
    + [As a player:](#first-time-user "As a player")
+ [Features](#features "Features")  
  + [Introduction](#Introduction "Introduction")
  + [Instructions](#Instructions "Instructions") 
  + [Start Game](#Start-Game "Start Game")
  + [Play Game](#Start-Game "Play Game")
+ [Future Features](#future-features "Future Features") 
+ [External Sources Used](#external-sources-used "External Sources Used")  
+ [Python Libraries Used](#python-libraries-used "Python Libraries Used")  
+ [Testing](#testing "Testing")
+ [Bugs and Solutions](#bugs-and-solutions "Bugs and Solutions")
+ [Development and Deployment](#development-and-deployment "Development and Deployment")
+ [Credits](#Credits "Credits")


## UX:
### User Stories
#### As a player 

## Existing Features:

### Introduction

![Introduction](images/introduction.jpg) 

### Instructions

![Instructions](images/instructions.jpg) 


### Start Game

![Start Game](images/start.jpg) 


### Play Game

![Play Game](images/play.jpg)

### Play Again or Quit

![Play Game](images/game-over.jpg)


## Future Features

## Technology Used

 - [Python](https://www.python.org/)
## External Sources Used

- Stack Overflow
- W3 School
- Youtube
- [Am I Responsive](https://ui.dev/amiresponsive)


## Python Libraries Used

- [Random](https://docs.python.org/3/library/random.html)  for computer random moves

## Testing

Testing was conducted very carefully through the entire project. Pep 8 validator came back with no issues
[Pep8](http://pep8online.com/)

![Validator Pep8](images/python-test.jpg)

### Exception/Error testing:

- User's name validation was tested checking all possible inputs. Empty spaces, numbers or symbols not accepted.

![Name Validation](images/name-validation.png)

![Start Input Validation](images/start-input-validation.png)

![Spot Input Validation](images/spot-input-validation.png)

![Same spot Input Validation](images/same-spot-validation.png)

![Quit replay Validation](images/quit-replay-validation.png)

- Python Pylint Report:

## Bugs and Solutions

## Development and Deployment

This project was developed with Visual Studio Code, using the template provided by Code Institute. Every step was documented and pushed thoroughly via GitHub.

The deployment is made using [Heroku](https://www.heroku.com/) following the listed steps:

1. Log in or register a new account on Heroku
2. Click on 'New' in the dashboard and select 'Create New App'
3. Select a name for the app and choose your region.
4. Click on "Create app"
4. When the app is created click on Setting 
5. To improve compatibility with various Python libraries add  Config Var with Key = PORT and the Value = 8000 
5. Add a buildpack: Python
6. Go back at the top and click on "Deploy" and select "GitHub"
7. Scroll down and click on 'Connect to GitHub'
8. Search for your GitHub repository name by typing it 
9. Click on "Connect"
10. Scroll down and click on "Deploy Branch"
11. You will see a message "The app was successfully deployed" when the app is built with python and all the depencencies
12. Click on view and you will see the [deployed site]()

## Credits

- A huge thanks goes to my mentor Jubril Akolade. who guided me with clear directions to finish the challenge.

[Back to top](#table-of-contents)
