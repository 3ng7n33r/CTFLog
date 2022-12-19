# CTF-Log
My CS50x Final Project
#### Video Demo:  https://youtu.be/N4v45fbqvTc
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

The project will be available at http://127.0.0.1:8000/.

## Usage

1. Create an account
2. Create a website or choose from the pre-existing content (Be sure to install the fixtures from installation step 6 for this.
3. Solve a ctf and enter the data into the webform.

Afterwards, past entries can be found in the sidebar

## License

This project is licensed under the [MIT License](LICENSE).

