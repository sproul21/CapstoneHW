from dataclasses import dataclass


@dataclass
class Item:
    name: str
    item_type: str
    price: float

# Example usage:
items = [
    Item("Milk", "Wic Eligible food", 3.00),
    Item("Jeans", "Clothing", 40.00),
    Item("Fur Jacket", "Clothing", 150.00),
    Item("Laptop", "Everything else", 800.00),
    Item("Bread", "Wic Eligible food", 2.50),
    Item("T-shirt", "Clothing", 15.00),
    Item("Fur Coat", "Clothing", 300.00),
    Item("Smartphone", "Everything else", 600.00)
]