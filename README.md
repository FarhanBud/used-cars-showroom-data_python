## FarhanBud Garage - Used Cars Admin CRUD System

   A simple Python console-based CRUD application for managing a used cars showroom database.
   Built as Capstone Project 1 for JCDSBSDAM29 by Muhamad Farhan Budiana.

## 📖 Description

This project is a text-based admin system for FarhanBud Garage, a fictional used car showroom.
Admins can login, view, add, update, and delete car records stored in a Python list of dictionaries.
The app also supports changing the admin password.
It’s designed with basic Python concepts only:

Variables & data types

Conditional statements

Looping

Lists & dictionaries

Functions

No external database is used. All data is stored in memory.

✨ Features

Admin Login (default: username admin, password admin123)

View all cars in a formatted dynamic table

Search car by ID

Add new car records

Update car records (except the unique ID)

Delete car records

Change admin password

Logout / exit program safely

🛠️ Requirements

Python 3.6 or newer

Works on Windows, Linux, or macOS terminal

No extra libraries required (only built-in Python sys).

🚀 How to Run

Clone this repository:

git clone https://github.com/yourusername/farhanbud-garage.git
cd farhanbud-garage


Run the program:

python farhanbud_garage.py


Login with default credentials:

Username: admin
Password: admin123


Follow on-screen menus to manage the used car database.

📝 Usage Notes

All data is stored in memory; when you exit the program, changes are lost.

You can change the admin password from the menu (option 5).

After changing password, the program returns to the login screen and you must login with the new password.

📂 Project Structure
farhanbud-garage/
├── usedcars   # Main Python file
└── README.md             # This documentation

