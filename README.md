Lost & Found Management System

A console-based Python program to manage lost and found items, allowing users to report lost or found items and administrators to manage reports, match items, and view statistics.

Features
User Features

Report a Found Item

Report a Lost Item

Admin Features

Admin login with password protection

View all found items

View all lost reports

Mark items as claimed

Auto-match lost items with found items

View statistics: total items, claimed items, unresolved reports

How It Works

Users can report lost or found items by entering details like name, description, contact, and date.

All reports are saved in text files (found.txt and lost.txt) for persistence.

Admins can log in with a password and manage reports through a console menu.

The program can automatically suggest potential matches between lost and found items.

Provides a statistics dashboard to monitor reports and claims.

Requirements

Python 3.x

Standard library modules: random, datetime, os

Optional for improved interface: colorama (for colored console output)

Installation & Usage

Clone the repository:

git clone https://github.com/yourusername/lost-and-found.git


Navigate to the project folder:

cd lost-and-found


Run the program:

python main.py


Follow the on-screen menu:

Report found/lost items

Admin login: password is admin123

lost-and-found/
│
├─ main.py          # Main program
├─ found.txt        # Stores reported found items
├─ lost.txt         # Stores reported lost items
└─ README.md        # Project documentation


Sample Output
========= LOST AND FOUND SYSTEM =========
1. Report Found Item
2. Report Lost Item
3. Admin Login
4. Exit
Select an option: 1

--- Report Found Item ---
Item Name: Umbrella
Description: Black umbrella
Your Name: John
Contact Number: 1234567890
Item Recorded Successfully! Found ID = 12345

Future Improvements

Add categories for items (electronics, clothing, etc.)

Implement a search by ID or name feature

Add colored output for improved TUI

Allow automatic resolution when a match is confirmed
