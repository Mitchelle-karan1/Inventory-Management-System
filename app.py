from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

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
