# Compare It

## Introduction
Compare It is a simple webapp written in Django to compare text using python difflib.

## Usage
Launch the django local server, input text on "Original Text" Textbox and press submit.Similarly, input text on "User Text" Textbox and press submit. Then, Press Get Report to check for differences.

## Installation

### Requirements
The Compare It app requires `Python3` and `Django`. Install the requirements by:
`pip install -r requirements.txt`

### Installation
Clone the repo or download the zip.
Create a virtual environment inside the CompareIt directory, activate the virtualenv and install the requirements.
```git clone https://github.com/divyamani1/CompareIt.git
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt```
Finally, run `python manage.py runserver` to run the local server and access the local server from `127.0.0.1:8000`.
