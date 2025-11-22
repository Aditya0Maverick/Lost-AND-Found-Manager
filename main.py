import random
from datetime import datetime
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def item_id():
    return random.randint(10000, 99999)

def timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def save_file(filename, records):
    with open(filename, "w") as f:
        for rec in records:
            f.write(" | ".join(rec) + "\n")

def loadfiles(filename):
    records = []
    if not os.path.exists(filename):
        return records

    with open(filename, "r") as f:
        for line in f:
            fields = [x.strip() for x in line.split("|")]
            records.append(fields)

    return records

def found_item():
    print("\n--- Report Found Item ---")
    item_ID = str(item_id())
    name = input("Item Name: ")
    desc = input("Description: ")
    finder = input("Your Name: ")
    contact = input("Contact Number: ")
    date = timestamp()
    status = "unclaimed"
    claimed_by = "None"

    record = [item_ID, name, desc, finder, contact, date, status, claimed_by]

    with open("found.txt", "a") as f:
        f.write(" | ".join(record) + "\n")

    print(f"Item Recorded Successfully! Found ID = {item_ID}")


def lost_item():
    print("\n--- Report Lost Item ---")
    lost_id = str(item_id())
    name = input("Item Name: ")
    desc = input("Description: ")
    owner = input("Your Name: ")
    contact = input("Contact Number: ")
    date = timestamp()
    status = "unresolved"
    matched = "None"

    record = [lost_id, name, desc, owner, contact, date, status, matched]

    with open("lost.txt", "a") as f:
        f.write(" | ".join(record) + "\n")

    print(f"Lost Report Submitted! Lost ID = {lost_id}")


def admin_login():
    password = "admin123"
    enter = input("Enter admin password: ")
    if enter == password:
        print("Login Successful!")
        return True
    else:
        print("Wrong password")
        return False


def admin_view_found():
    print("\n========= Found Items List =========")
    items = loadfiles("found.txt")

    if not items:
        print("No items found")
        return False

    for i in items:
        print(
            f"ID: {i[0]} | Item: {i[1]} | Description: {i[2]} | "
            f"Finder: {i[3]} | Contact: {i[4]} | Status: {i[6]} | Claimed by: {i[7]}"
        )


def admin_view_lost():
    print("\n========= Lost Reports =========")
    l_items = loadfiles("lost.txt")

    if not l_items:
        print("No items found")
        return False

    for i in l_items:
        print(
            f"ID: {i[0]} | Item: {i[1]} | Description: {i[2]} | "
            f"Owner: {i[3]} | Contact: {i[4]} | Status: {i[6]} | Match: {i[7]}"
        )


def admin_mark_claimed():
    print("\n======== Mark Item as Claimed =========")
    item_id = input("Enter the item ID: ")
    claimed_by = input("Enter name of person who claimed: ")

    items = loadfiles("found.txt")

    for i in items:
        if i[0] == item_id:
            i[6] = "claimed"
            i[7] = claimed_by
            save_file("found.txt", items)
            print("Item marked as claimed successfully!")
            return

    print("Invalid ID")


def admin_auto_match():
    print("\n--- Auto Match Lost vs Found ---")
    found = loadfiles("found.txt")
    lost = loadfiles("lost.txt")

    for L in lost:
        if L[6] == "resolved":
            continue

        print(f"\nLost: {L[1]} (ID: {L[0]})")

        for F in found:
            if F[6] == "claimed":
                continue

            if L[1].lower() in F[1].lower() or F[1].lower() in L[1].lower():
                print(f"➡ Possible Match → Found ID: {F[0]} | {F[1]} | {F[2]}")


def stats():
    found = loadfiles("found.txt")
    lost = loadfiles("lost.txt")   

    total_found = len(found)
    total_lost = len(lost)
    claimed = sum(1 for i in found if i[6] == "claimed")
    unresolved = sum(1 for i in lost if i[6] == "unresolved")

    print("\n---- Statistics Dashboard ----")
    print(f"Total Found Items: {total_found}")
    print(f"Total Lost Reports: {total_lost}")
    print(f"Total Claimed Items: {claimed}")
    print(f"Unresolved Lost Items: {unresolved}")

def admin_menu():
    while True:
           
        print("\n========= ADMIN PANEL =========")
        print("1. View found items list")
        print("2. View Lost Reports")
        print("3. Mark Item as Claimed")
        print("4. Auto-Match Lost vs Found")
        print("5. View Statistics")
        print("6. Back to Main Menu")

        choice = input("Enter choice: ")

        if choice == "1":
            admin_view_found()
        elif choice == "2":
            admin_view_lost()
        elif choice == "3":
            admin_mark_claimed()
        elif choice == "4":
            admin_auto_match()
        elif choice == "5":
            stats()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")
    


def main():
    while True:
        clear_screen()
        print("\n========= LOST AND FOUND SYSTEM =========")
        print("1. Report Found Item")
        print("2. Report Lost Item")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            found_item()
        elif choice == "2":
            lost_item()
        elif choice == "3":
            if admin_login():
                admin_menu()
        elif choice == "4":
            print("Exited successfully.")
            break
        else:
            print("Invalid choice.")


main()
