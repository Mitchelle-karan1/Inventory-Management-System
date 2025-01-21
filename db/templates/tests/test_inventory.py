from inventory_manager import add_item, view_inventory, delete_item

# Test adding items
add_item("Laptop", "Electronics", 10, 800.00, "Tech Supplier")
add_item("Desk Chair", "Furniture", 5, 120.50, "Office Supplies Inc")

# Test viewing items
print("Current Inventory:")
view_inventory()

# Test deleting an item
delete_item(1)  # Assuming '1' is the ID of the first item added
print("Inventory after deletion:")
view_inventory()
