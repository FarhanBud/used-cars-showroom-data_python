# CAPSTONE PROJECT 1
# Muhamad Farhan Budiana JCDSBSDAM29

# Used Cars Business Sales Database based on Python
# ID : Data Penjualan Usaha Mobil Bekas berbasis Python

# CODE START

# DATA DEFAULT BEFORE CHANGE
cars = [
    {
        "id": "MB001",
        "brand": "Toyota",
        "model": "GR Supra 3.0 Silver Metal",
        "year": 2020,
        "price": 1800000000,
        "status": "On Stock"
    },
    {
        "id": "MB002",
        "brand": "Honda",
        "model": "Civic Type R RED Full Package",
        "year": 2018,
        "price": 1200000000,
        "status": "Full Detailing Progress"
    },
    {
        "id": "MB002",
        "brand": "BMW",
        "model": "M3 G80 Green ",
        "year": 2018,
        "price": 1500000000,
        "status": "On Stock"
    }
]

# --- Main Menu ---
def main_menu():

    # Show the main menu of FarhanBud Garage.
    # Directs user to CRUD functions or exits the program.

    while True:
        print("\n===== FARHANBUD GARAGE =====")
        print("===== ADMIN DATABASE =====")
        print("1. Available Used Cars ")
        print("2. Add New Used Cars ")
        print("3. Update/Change Available Used Cars Data ")
        print("4. Delete Data -- (Proceed with Care ! )")
        print("5. Exit Program ")

        choice = input("Select menu (1-5): ")

        if choice == "1":
            read_data()
        elif choice == "2":
            create_data()
        # elif choice == "3":
        #     update_data()
        # elif choice == "4":
        #     delete_data() BELUM SELESAI
        elif choice == "5":
            print("Thank you for using FarhanBud Garage Admin Database.")
            break
        else:
            print("Invalid choice. Please try again.\n")

# --- Helper Functions ---
def find_car_by_id(car_id):

    # Find the index of a car in the 'cars' list by its unique ID.
    # Returns the index if found, otherwise -1.

    for i, car in enumerate(cars):
        if car["id"] == car_id:
            return i
    return -1

def show_all_cars():

    # Display all cars in the current data collection in a dynamic table format
    # (column widths adjust to the longest value).

    if not cars:
        print("\nNo car data available. Please Try Again \n")
        return

    # headers
    headers = ["ID", "Brand", "Model", "Year", "Price", "Status"]

    # convert data into rows (as strings)
    rows = []
    for car in cars:
        rows.append([
            str(car['id']),
            str(car['brand']),
            str(car['model']),
            str(car['year']),
            f"Rp{car['price']}",
            str(car['status'])
        ])

    # include headers for width calculation
    all_rows = [headers] + rows

    # compute max width of each column
    col_widths = [max(len(row[i]) for row in all_rows) for i in range(len(headers))]

    # build a dynamic format string like "{:<6} {:<10} ..." based on widths
    fmt = "  ".join("{:<" + str(w) + "}" for w in col_widths)

    # print header
    print("\n=== CAR LIST ===")
    print(fmt.format(*headers))
    print("-" * (sum(col_widths) + 2 * (len(headers)-1)))

    # print rows
    for row in rows:
        print(fmt.format(*row))
    print()


# --- CRUD Functions ---
def read_data():

    # Show the Read Data menu.
    # Allows user to display all cars or search by unique ID.

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
                      f"| Year: {car['year']} | Price: Rp{car['price']} | Status: {car['status']}\n")
            else:
                print("Car with this ID not found.\n")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.\n")

def create_data():

    # Show the Create Data menu.
    # Allows user to add a new car to the collection after validating inputs.

    while True:
        print("\n=== CREATE DATA MENU ===")
        print("1. Add new car")
        print("2. Return to Main Menu")
        choice = input("Select menu (1-2): ")

        if choice == "1":
            car_id = input("Enter unique car ID: ").strip()
            if find_car_by_id(car_id) != -1:
                print("ID already exists, duplicates are not allowed!\n")
                continue

            brand = input("Enter car brand: ").title()
            model = input("Enter car model: ").title()

            try:
                year = int(input("Enter car year (number): "))
                price = int(input("Enter car price (number): "))
            except ValueError:
                print("Year and price must be numbers.\n")
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
                print("Car data added successfully.\n")
            elif confirm == "N":
                print("Data not saved.\n")
            else:
                print("Invalid confirmation choice.\n")

        elif choice == "2":
            break
        else:
            print("Invalid choice. Please try again.\n")

# RUN PROGRAM
main_menu()
