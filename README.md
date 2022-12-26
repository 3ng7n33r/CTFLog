# CTF-Log
My CS50x Final Project
#### Video Demo:  https://youtu.be/N4v45fbqvTc
#### URL:  https://ctflog.eu.pythonanywhere.com/
#### Description:
A simple website to store solutions, passwords and notes for capture the flag competitions.
Built using the Django Framework. To run locally, install django, cd into the folder and use: $ python manage.py runserver. This starts the local django development server. The website can then be accessed under 127.0.0.1:8000/

## What is a Capture the Flag Competition?

Capture the flag (CTF) is a type of cybersecurity competition that involves finding and exploiting vulnerabilities in computer systems and networks. The goal is usually to "capture" a flag, which is usually a string of text, hidden within the system or network.

In a CTF competition, teams of players work together to find and exploit vulnerabilities in order to capture the flag. The team that captures the most flags or completes the challenges the fastest is typically declared the winner.

CTF competitions can be organized in a variety of formats, including online and in-person events. They can range in difficulty from beginner to advanced, and may focus on a specific area of cybersecurity, such as web security or cryptography.

CTF competitions are a popular way for cybersecurity professionals and enthusiasts to test their skills and learn about new technologies and techniques. They are also used by companies and organizations as a way to identify and recruit talented cybersecurity professionals.

## Prerequisites

- Python 3.7 or higher
- Django 3.1 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/3ng7n33r/CTFLog.git
```
2. Navigate to the project directory:
```bash
cd CTFLog
``` 
3. Install the required packages:
(Optional but recommended):
- create a virtual environment:
```bash
virtualenv env
```
- Install the packages
```bash
pip install -r requirements.txt
```
4. Run the migrations:
```bash
python manage.py migrate
```
5. Start the development server:
```bash
python manage.py runserver
```
6. (Optional) Install fixtures to get a small preselection of websites and ctf's
```bash
python manage.py loaddata CTFLog.json
```
7. (Optional) If you want to contribute to the project or modify code for yourself, it is recommended to install the linter and autoformatter pre-commit hooks
```
pre-commit install
```


The project will be available at http://127.0.0.1:8000/.

## Usage

1. Create an account
2. Create a website or choose from the pre-existing content (Be sure to install the fixtures from installation step 6 for this.
3. Solve a ctf and enter the data into the webform.

Afterwards, past entries can be found in the sidebar

## License

This project is licensed under the [MIT License](LICENSE).

## Inspiration

The idea behind this project came from me trying to solve the bandit series of the over the wire website and having to restart over and over again because I misplaced the file I wrote the passwords into.
I further realised during following playthroughs that I did not memorise certain techniques well. In some cases, I found solutions I was proud of but forgot what exactly they were. In the moment I was just too focused on pushing to the next level. This is why I wanted a simple application where I could store the commands I used to replay the ctf and the solution in my head, a notes section to explain the code in case it uses commands which I can not easily recognize and of course the password for the next section in case I wanted to continue where I left off.

## Model design

The Django models make it fairly easy to structure this logic into database tables. If we look into models/ctf.py we can see that the main models are site, campaign and ctf. Every model has a unique slug attribute which automatically gets generated from the name given during creation.
With this slug, navigation to the exact part of the website is as easy as knowing the name of the ctf.
The models/favorites.py section is a model that will be useful for future functionality. At the moment, a user sees only events created by himself. Something I would like to implement, should this ever become an actual website, would be a functionality for users to share solutions to ctf's they have already solved. If a  user found an elegant solution, one could favorite it to be able to keep track. This can also be seen in the "public" attribute of the ctf model which, at the moment, has no function but will distinguish between published ctf's and ctf's the user wants to keep private in the future.

## Front end

For the front end, I combined multiple Bootstrap templates into a responsive site with a sidebar. The design is kept minimalistic as functionality is the priority.

## Users

The users functionality is fairly uninteresting when run on a local machine as it can be expected to be run by only a single user. However, it is planned for this project to become a website where multiple users will be able to upload and share their solutions with one another. The Django user model has not been further modified at the moment.

## Black and Flake8

Black and Flake8 are the autoformatter and linter used in this project to make sure the stylerules are consistently followed. To make sure they are run before every commit with as little extra effort as possible, pre-commit hooks have been implemented as well.
