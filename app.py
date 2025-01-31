from flask import Flask, render_template , request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect("db/inventory.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    rows = cursor.fetchall()
    conn.close()
    return render_template("inventory.html", inventory=rows)

# Add item route (Create)
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = request.form['quantity']
        price = request.form['price']
        supplier = request.form['supplier']
        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Inventory (name, category, quantity, price, supplier) VALUES (?, ?, ?, ?, ?)",
                       (name, category, quantity, price, supplier))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template("add_item.html")

# Update item route (Update)
@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']
        quantity = request.form['quantity']
        price = request.form['price']
        supplier = request.form['supplier']
        
        cursor.execute("UPDATE Inventory SET name = ?, category = ?, quantity = ?, price = ?, supplier = ? WHERE id = ?",
                       (name, category, quantity, price, supplier, item_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    
    cursor.execute("SELECT * FROM Inventory WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    return render_template("update_item.html", item=item)

# Delete item route (Delete)
@app.route('/delete/<int:item_id>', methods=['GET'])
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

# Route to display inventory
@app.route('/')
def home():
    conn = sqlite3.connect("db/inventory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Inventory")
    rows = cursor.fetchall()
    conn.close()
    return render_template("inventory.html", inventory=rows)

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        # Get the updated values from the form
        new_name = request.form['name']
        new_quantity = int(request.form['quantity'])
        new_price = float(request.form['price'])

        # Update the item in the database
        cursor.execute(
            "UPDATE Inventory SET name = ?, quantity = ?, price = ? WHERE id = ?",
            (new_name, new_quantity, new_price, item_id)
        )
        conn.commit()
        conn.close()
        return redirect('/')
    
    # Fetch the current item details
    cursor.execute("SELECT * FROM Inventory WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    conn.close()
    
    return render_template('update.html', item=item)
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Delete the item from the database
    cursor.execute("DELETE FROM Inventory WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = get_db_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        search_term = request.form['search']
        cursor.execute("SELECT * FROM Inventory WHERE name LIKE ?", ('%' + search_term + '%',))
    else:
        cursor.execute("SELECT * FROM Inventory")
    
    rows = cursor.fetchall()
    conn.close()
    
    return render_template("inventory.html", inventory=rows)

def get_db_connection():
    conn = sqlite3.connect('db/inventory.db')
    conn.row_factory = sqlite3.Row
    return conn




   
