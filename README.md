# Project-4-Email-via-Python-REGEXP [Console Based]
## Overview
This is a simple console-based Python program that collects user details such as Name, Date of Birth, Phone Number, Instagram ID, and Email. 
It validates user input using regular expressions (REGEXP) and then sends an email with the collected information using Python's smtplib.

## Features
- Validates user input using regular expressions
- Ensures data format correctness (e.g., Name, DOB, Phone, and Email)
- Sends user details via email using SMTP
- Interactive console-based execution

## Prerequisites
To run this project, ensure you have the following:
- Python 3.x installed
- A Gmail account for sending emails
- Less secure apps access enabled for the Gmail account
- Required Python libraries installed

## Installation
1.Clone this repository:
- git clone https://github.com/your-username/Email-via-Python-REGEXP.git
2.Navigate to the project directory:
- cd Email-via-Python-REGEXP
3.Install dependencies:
- pip install smtplib email re

## Usage
Run the script using:
- python main.py
Follow the on-screen instructions to enter details in the correct format.

## Regular Expression Rules
- Name: Alphabet characters and spaces only
- DOB: Must follow DD-MM-YYYY format
- Phone: Must follow XXX-XXX-XXXX format
- Email: Must be a Gmail address (example@gmail.com)

## SMTP Configuration
The script uses smtplib to send emails. Update the following in main.py:
- msg['From'] = "your-email@gmail.com"
- server.login("your-email@gmail.com", "your-app-password")
For security reasons, use App Passwords instead of your actual Gmail password.

## Error Handling
- The script prompts users until valid input is provided.
- It handles SMTP connection errors gracefully.

## Disclaimer
Using your personal Gmail account for this script requires enabling Less Secure Apps or 
using App Passwords. 
Be cautious when sharing credentials.

## License
This project is licensed under the MIT License.
