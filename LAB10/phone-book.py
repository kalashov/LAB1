import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="paradise",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def insert_manual():
    first = input("First name: ")
    last = input("Last name: ")
    phone = input("Phone number: ")
    cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)",
                (first, last, phone))
    conn.commit()
    print("Added")

def insert_from_csv(file_path):
    with open(file_path, newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            cur.execute("INSERT INTO phonebook (first_name, last_name, phone_number) VALUES (%s, %s, %s)", row)
    conn.commit()
    print("CSV added")

def update_user():
    phone = input("Enter phone number to update: ")
    new_name = input("New first name: ")
    new_phone = input("New phone number: ")
    cur.execute("""
        UPDATE phonebook
        SET first_name = %s, phone_number = %s
        WHERE phone_number = %s
    """, (new_name, new_phone, phone))
    conn.commit()
    print("Updated")

def search_user():
    print("🔍 Search by any field (leave empty to skip):")
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    phone = input("Phone number: ").strip()

    query = "SELECT * FROM phonebook WHERE 1=1"
    params = []

    if first:
        query += " AND first_name ILIKE %s"
        params.append(f"%{first}%")
    if last:
        query += " AND last_name ILIKE %s"
        params.append(f"%{last}%")
    if phone:
        query += " AND phone_number ILIKE %s"
        params.append(f"%{phone}%")

    cur.execute(query, params)
    results = cur.fetchall()

    if not results:
        print("No matching records.")
    else:
        print("Found:")
        for row in results:
            print(row)

def delete_user():
    phone = input("Enter phone number to delete: ")
    cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
    conn.commit()
    print("Deleted")

def main():
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Add user manually")
        print("2. Upload users from CSV")
        print("3. Update user")
        print("4. Search user")
        print("5. Delete user")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_manual()
        elif choice == "2":
            insert_from_csv("phonebook.csv")
        elif choice == "3":
            update_user()
        elif choice == "4":
            search_user()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice")

    cur.close()
    conn.close()

main()