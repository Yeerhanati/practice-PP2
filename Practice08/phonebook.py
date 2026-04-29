from connect import get_connection, create_contacts_table
import psycopg2

# Initialize table on startup
create_contacts_table()

# 1. Call search function
def search_contacts(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    results = cur.fetchall()

    print("\nSearch Results:")
    if not results:
        print("No contacts found.")
    else:
        for row in results:
            print(f"Name: {row[0]} | Phone: {row[1]}")

    cur.close()
    conn.close()

# 2. Call upsert procedure
def upsert_contact(name, phone):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()
    print("Operation completed successfully!")
    cur.close()
    conn.close()

# 3. Call bulk insert procedure
def bulk_insert(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL bulk_insert_contacts(%s, %s, %s)", (names, phones, psycopg2.sql.Placeholder('invalid_data')))
    invalid = cur.fetchone()[0]
    conn.commit()

    print("Bulk insert finished!")
    if invalid:
        print("Invalid entries:")
        for item in invalid:
            print(f"- {item}")

    cur.close()
    conn.close()

# 4. Call pagination function
def get_paged_contacts(limit, offset):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paged(%s, %s)", (limit, offset))
    results = cur.fetchall()

    print("\nPaginated Results:")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

    cur.close()
    conn.close()

# 5. Call delete procedure
def delete_contact(keyword):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (keyword,))
    conn.commit()
    print("Contact deleted successfully!")
    cur.close()
    conn.close()

# Main English Menu
def main():
    while True:
        print("\n===== PhoneBook - Practice 8 =====")
        print("1. Search Contacts by Pattern")
        print("2. Add/Update Contact (Upsert)")
        print("3. Bulk Insert Contacts")
        print("4. View Paginated Contacts")
        print("5. Delete Contact")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pattern = input("Enter search pattern: ")
            search_contacts(pattern)
        elif choice == "2":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            upsert_contact(name, phone)
        elif choice == "3":
            names = input("Enter names (comma-separated): ").split(",")
            phones = input("Enter phones (comma-separated): ").split(",")
            bulk_insert(names, phones)
        elif choice == "4":
            limit = int(input("Enter items per page: "))
            offset = int(input("Enter offset: "))
            get_paged_contacts(limit, offset)
        elif choice == "5":
            keyword = input("Enter name or phone to delete: ")
            delete_contact(keyword)
        elif choice == "0":
            print("Exiting application...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()