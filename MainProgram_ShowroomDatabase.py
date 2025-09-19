# CAPSTONE PROJECT 1
# Muhamad Farhan Budiana JCDSBSDAM29

# Used Cars Showroom Database based on Python
# Admin CRUD System for FarhanBud Garage

import sys
print(sys.version)

# ==== Color Codes for Terminal Output ====
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# ==== Default Admin Credentials ====
admin_username = "admin"
admin_password = "admin123"

# ==== Default Data (List of Dictionaries) ====
cars = [
    {
        "id": "uc001",
        "brand": "Toyota",
        "model": "GR Supra 3.0 Silver Metal",
        "year": 2020,
        "price": 1800000000,
        "status": "On Stock"
    },
    {
        "id": "uc002",
        "brand": "Honda",
        "model": "Civic Type R RED Full Package",
        "year": 2018,
        "price": 1200000000,
        "status": "Sold"
    }, 
    {
        "id": "uc003",
        "brand": "BMW",
        "model": "M3 G80 Green ",
        "year": 2018,
        "price": 1500000000,
        "status": "On Stock"
    },
    {
        "id": "uc004",
        "brand": "Hyundai",
        "model": "Ioniq 5N Special Color",
        "year": 2022,
        "price": 900000000,
        "status": "On Stock"
    },
    {
        "id": "uc005",
        "brand": "Nissan",
        "model": "300ZX 2by2 Red Metallic",
        "year": 1997,
        "price": 350000000,
        "status": "Sold"
    },
    {
        "id": "uc006",
        "brand": "Wuling",
        "model": "Cloud EV White Gold ",
        "year": 2023,
        "price": 300000000,
        "status": "On Stock"
    },
    
]

# ==== LOGIN FUNCTION ====
def login():
    # Ask for admin username & password before entering the main menu.
    global admin_username, admin_password
    while True:
        print("\n" + "=" * 60)
        print("         ===== FARHANBUD GARAGE ADMIN LOGIN =====")
        print("=" * 60)
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username == admin_username and password == admin_password:
            print(GREEN + "\nLogin successful. Welcome Admin!\n" + RESET)
            main_menu()
            break
        else:
            print(RED + "Invalid username or password. Please try again.\n" + RESET)

# ==== MAIN MENU FUNCTION ====
def main_menu():
    # Shows the main admin menu. Directs user to CRUD functions or exits the program.
    global admin_password
    while True:
        print("\n" + "=" * 60)
        print("       ===== FARHANBUD GARAGE - USED CARS DATABASE =====")
        print("                 ===== Admin Used Only =====")
        print("=" * 60)
        print("   1. Available Used Cars ")
        print("   2. Add New Used Cars ")
        print("   3. Update/Change Available Used Cars Data ")
        print("   4. Delete Data -- (Proceed with Care!)")
        print("   5. Change Admin Password")
        print("   6. Logout Program \n")

        choice = input("Select Menu to Start (1-6): ")

        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        elif choice == "3":
            update_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            change_password()
            return    # After change password, going back to login menu
        elif choice == "6":
            print("\nLogging out... Thank You Admin !\n")
            sys.exit()
        else:
            print(RED + "Invalid choice. Please try again.\n" + RESET)

# ==== CHANGE PASSWORD FUNCTION ====
def change_password():
    # Allows admin to change their password.
    global admin_password
    print("\n=== CHANGE ADMIN PASSWORD ===")
    old_pass = input("Enter current password: ").strip()
    if old_pass != admin_password:
        print(RED + "Current password incorrect.\n" + RESET)
        return
    new_pass = input("Enter new password: ").strip()
    confirm_pass = input("Confirm new password: ").strip()
    if new_pass == confirm_pass and new_pass != "":
        admin_password = new_pass
        print(GREEN + "\nPassword changed successfully! Please log in again.\n" + RESET)
    else:
        print(RED + "Passwords do not match or empty.\n" + RESET)

# ==== HELPER FUNCTION ====
def find_car_by_id(car_id):
    # Finds the index of a car in the 'cars' list by its unique ID.
    # Returns the index if found, otherwise -1.
    for i, car in enumerate(cars):
        if car["id"] == car_id:
            return i
    return -1

def show_all_cars():
    # Displays all cars in a table format (column widths adjust auto).
    if not cars:
        print("\n" + RED + "No car data available. Please Try Again.\n" + RESET)
        return

    headers = ["ID", "Brand", "Model", "Year", "Price", "Status"]
    rows = []
    for car in cars:
        rows.append([
            str(car['id']),
            str(car['brand']),
            str(car['model']),
            str(car['year']),
            f"Rp{car['price']:,}",
            str(car['status'])
        ])

    all_rows = [headers] + rows
    col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(headers))]
    fmt = "  ".join("{:<" + str(w) + "}" for w in col_widths)

    print("\n=== CAR LIST ===")
    print(fmt.format(*headers))
    print("-" * (sum(col_widths) + 2 * (len(headers)-1)))
    for row in rows:
        print(fmt.format(*row))
    print()

# ==== CRUD FUNCTIONS ====
def read_data():
    # Shows the Read Data menu. Lets admin display all cars or search by ID.
    while True:
        print("\n=== READ DATA MENU ===")
        print("1. Show all cars")
        print("2. Search car by ID")
        print("3. Return to Main Menu")
        choice = input("Select menu (1-3): ")

        if choice == "1":
            show_all_cars()
        elif choice == "2":
            car_id = input("Enter car ID: ").strip()
            idx = find_car_by_id(car_id)
            if idx != -1:
                car = cars[idx]
                print(f"ID: {car['id']} | Brand: {car['brand']} | Model: {car['model']} "
                      f"| Year: {car['year']} | Price: Rp{car['price']:,} | Status: {car['status']}\n")
            else:
                print(RED + "Car with this ID not found.\n" + RESET)
        elif choice == "3":
            break
        else:
            print(RED + "Invalid choice. Please try again.\n" + RESET)

def create_data():
    # Shows the Create Data menu. Lets admin add a new car to the collection after validation.
    while True:
        print("\n=== CREATE DATA MENU ===")
        print("1. Add new car")
        print("2. Return to Main Menu")
        choice = input("Select menu (1-2): ")

        if choice == "1":
            car_id = input("Enter unique car ID: ").strip()
            if find_car_by_id(car_id) != -1:
                print(RED + "ID already exists, duplicates are not allowed!\n" + RESET)
                continue

            brand = input("Enter car brand: ").title()
            model = input("Enter car model: ").title()

            try:
                year = int(input("Enter car year (number): "))
                price = int(input("Enter car price (number): "))
            except ValueError:
                print(RED + "Year and price must be numbers.\n" + RESET)
                continue

            status = input("Enter status (Available/Sold): ").title()
            confirm = input("Save this data? (Y/N): ").upper()
            if confirm == "Y":
                cars.append({
                    "id": car_id,
                    "brand": brand,
                    "model": model,
                    "year": year,
                    "price": price,
                    "status": status
                })
                print(GREEN + "Car data added successfully.\n" + RESET)
            elif confirm == "N":
                print("Data not saved.\n")
            else:
                print(RED + "Invalid confirmation choice.\n" + RESET)

        elif choice == "2":
            break
        else:
            print(RED + "Invalid choice. Please try again.\n" + RESET)

def update_data():
    # Shows the Update Data menu. Lets admin modify existing car data except for the unique ID.
    while True:
        print("\n=== UPDATE DATA MENU ===")
        print("1. Update car data")
        print("2. Return to Main Menu")
        choice = input("Select menu (1-2): ")

        if choice == "1":
            car_id = input("Enter car ID to update: ").strip()
            idx = find_car_by_id(car_id)
            if idx == -1:
                print(RED + "Car with this ID not found.\n" + RESET)
                continue

            car = cars[idx]
            print("Current data:")
            print(car)

            key_to_update = input("Which field to update? (brand/model/year/price/status): ").lower()
            if key_to_update not in car or key_to_update == "id":
                print(RED + "Invalid field or ID cannot be changed.\n" + RESET)
                continue

            new_value = input("Enter new value: ")
            if key_to_update in ["year", "price"]:
                try:
                    new_value = int(new_value)
                except ValueError:
                    print(RED + "Value must be a number.\n" + RESET)
                    continue

            confirm = input("Confirm update? (Y/N): ").upper()
            if confirm == "Y":
                cars[idx][key_to_update] = new_value
                print(GREEN + "Car data updated successfully.\n" + RESET)
            else:
                print("Update cancelled.\n")

        elif choice == "2":
            break
        else:
            print(RED + "Invalid choice. Please try again.\n" + RESET)

def delete_data():
    # Shows the Delete Data menu. Lets admin remove a car from the collection after confirmation.
    while True:
        print("\n=== DELETE DATA MENU ===")
        print("1. Delete car")
        print("2. Return to Main Menu")
        choice = input("Select menu (1-2): ")

        if choice == "1":
            car_id = input("Enter car ID to delete: ").strip()
            idx = find_car_by_id(car_id)
            if idx == -1:
                print(RED + "Car with this ID not found.\n" + RESET)
                continue

            confirm = input(f"Are you sure you want to delete car ID {car_id}? (Y/N): ").upper()
            if confirm == "Y":
                del cars[idx]
                print(GREEN + "Car data deleted successfully.\n" + RESET)
            else:
                print("Deletion cancelled.\n")

        elif choice == "2":
            break
        else:
            print(RED + "Invalid choice. Please try again.\n" + RESET)

# ==== RUN PROGRAM ====
while True:
    login()   # Program will be loop while in true condition, effected for admin after change password
