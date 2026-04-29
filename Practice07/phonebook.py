import csv
from connect import get_db_connection, create_phonebook_table

# 1. Insert single contact
def insert_contact(connection, first_name, phone_number):
    query = "INSERT INTO phonebook (first_name, phone_number) VALUES (%s, %s);"
    cursor = connection.cursor()
    cursor.execute(query, (first_name, phone_number))
    connection.commit()
    cursor.close()
    print("Contact added successfully")

# 2. Import contacts from CSV
def import_contacts_from_csv(connection, file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_contact(connection, row['first_name'], row['phone_number'])
    print("All contacts imported from CSV")

# 3. Update contact (name or phone)
def update_contact(connection, old_name, new_name=None, new_phone=None):
    cursor = connection.cursor()
    if new_name:
        query = "UPDATE phonebook SET first_name = %s WHERE first_name = %s;"
        cursor.execute(query, (new_name, old_name))
    if new_phone:
        query = "UPDATE phonebook SET phone_number = %s WHERE first_name = %s;"
        cursor.execute(query, (new_phone, old_name))
    connection.commit()
    cursor.close()
    print("Contact updated successfully")

# 4. Search contacts
def search_contacts(connection, name=None, phone_prefix=None):
    cursor = connection.cursor()
    if name:
        cursor.execute("SELECT * FROM phonebook WHERE first_name = %s;", (name,))
    elif phone_prefix:
        cursor.execute("SELECT * FROM phonebook WHERE phone_number LIKE %s;", (phone_prefix + '%',))
    else:
        cursor.execute("SELECT * FROM phonebook;")
    
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()

# 5. Delete contact
def delete_contact(connection, name=None, phone=None):
    cursor = connection.cursor()
    if name:
        cursor.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
    elif phone:
        cursor.execute("DELETE FROM phonebook WHERE phone_number = %s;", (phone,))
    connection.commit()
    cursor.close()
    print("Contact deleted successfully")

# Console Menu
def main():
    conn = get_db_connection()
    if not conn:
        return
    
    create_phonebook_table(conn)
    
    while True:
        print("\n===== PhoneBook Application =====")
        print("1. Add Contact Manually")
        print("2. Import Contacts from CSV")
        print("3. View/ Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter first name: ")
            phone = input("Enter phone number: ")
            insert_contact(conn, name, phone)
        
        elif choice == '2':
            import_contacts_from_csv(conn, "contacts.csv")
        
        elif choice == '3':
            print("\nSearch Options:")
            print("1. Search by name")
            print("2. Search by phone prefix")
            print("3. Show all contacts")
            opt = input("Choose option: ")
            if opt == '1':
                name = input("Enter name: ")
                search_contacts(conn, name=name)
            elif opt == '2':
                prefix = input("Enter phone prefix: ")
                search_contacts(conn, phone_prefix=prefix)
            else:
                search_contacts(conn)
        
        elif choice == '4':
            old_name = input("Enter current name: ")
            print("1. Update name")
            print("2. Update phone number")
            opt = input("Choose option: ")
            if opt == '1':
                new_name = input("Enter new name: ")
                update_contact(conn, old_name, new_name=new_name)
            elif opt == '2':
                new_phone = input("Enter new phone: ")
                update_contact(conn, old_name, new_phone=new_phone)
        
        elif choice == '5':
            print("1. Delete by name")
            print("2. Delete by phone")
            opt = input("Choose option: ")
            if opt == '1':
                name = input("Enter name to delete: ")
                delete_contact(conn, name=name)
            elif opt == '2':
                phone = input("Enter phone to delete: ")
                delete_contact(conn, phone=phone)
        
        elif choice == '6':
            conn.close()
            print("Connection closed. Exiting...")
            break
        
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()