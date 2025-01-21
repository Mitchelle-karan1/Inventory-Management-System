import sqlite3

# Function to initialize the database and create the table
def initialize_database():
    conn = sqlite3.connect("db/inventory.db")  # Connect to database (creates if not exists)
    cursor = conn.cursor()

    # Create the Inventory table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT,
        quantity INTEGER NOT NULL CHECK(quantity >= 0),
        price REAL NOT NULL CHECK(price >= 0),
        supplier TEXT,
        added_date DATE DEFAULT CURRENT_DATE
    )
    """)
    conn.commit()
    print("Database and table setup complete.")
    conn.close()

# Function to add an item to the inventory
def add_item(name, category, quantity, price, supplier):
    conn = sqlite3.connect("db/inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Inventory (name, category, quantity, price, supplier)
        VALUES (?, ?, ?, ?, ?)
    """, (name, category, quantity, price, supplier))
    conn.commit()
    print(f"Item '{name}' added successfully!")
    conn.close()

# Function to view all inventory items
def view_inventory():
    conn = sqlite3.connect("db/inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

# Function to delete an item from the inventory
def delete_item(item_id):
    conn = sqlite3.connect("db/inventory.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Inventory WHERE id = ?", (item_id,))
    conn.commit()
    print(f"Item with ID {item_id} deleted successfully!")
    conn.close()

# Initialize the database when the script runs
if __name__ == "__main__":
    initialize_database()
