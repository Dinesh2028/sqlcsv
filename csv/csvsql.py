import sqlite3
import csv

# Database setup
conn = sqlite3.connect("results.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()

def add_result(name, score, date):
    cursor.execute("INSERT INTO results (name, score, date) VALUES (?, ?, ?)", (name, score, date))
    conn.commit()
    print("Result added successfully!")

def save_to_csv():
    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()
    
    with open("results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Score", "Date"])
        writer.writerows(results)
    print(" Results saved to results.csv!")

def view_results():
    cursor.execute("SELECT * FROM results")
    results = cursor.fetchall()
    if results:
        print("\n Results:")
        for result in results:
            print(f"ID: {result[0]}, Name: {result[1]}, Score: {result[2]}, Date: {result[3]}")
    else:
        print(" No results found!")

if __name__ == "__main__":
    create_table()
    
    while True:
        print("\nResults Management System:")
        print("1. Add Result")
        print("2. View Results")
        print("3. Save Results to CSV")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            try:
                score = int(input("Enter score: "))
                date = input("Enter date (YYYY-MM-DD): ")
                add_result(name, score, date)
            except ValueError:
                print(" Invalid input! Score must be a number.")
        elif choice == "2":
            view_results()
        elif choice == "3":
            save_to_csv()
        elif choice == "4":
            print(" Exiting...")
            conn.close()
            break
        else:
            print(" Invalid choice! Try again.")
