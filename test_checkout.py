import unittest
from checkout import Item, calculate_total

class TestCalculateTotal(unittest.TestCase):
    def test_normal_cases(self):
        items = [
            Item("Milk", "Wic Eligible food", 3.00),
            Item("Jeans", "Clothing", 40.00),
            Item("Fur Jacket", "Clothing", 150.00),
            Item("Laptop", "Everything else", 800.00)
        ]

        self.assertAlmostEqual(calculate_total("NJ", items), 1055.70, places=2)
        self.assertAlmostEqual(calculate_total("DE", items), 993.00, places=2)
        self.assertAlmostEqual(calculate_total("PA", items), 1050.00, places=2)

    def test_empty_item_type(self):
        items = [
            Item("Milk", "Wic Eligible food", 3.00),
            Item("Jeans", "", 40.00)
        ]

        with self.assertRaises(ValueError, msg="Item type cannot be empty."):
            calculate_total("NJ", items)

    def test_empty_cart(self):
        items = []

        with self.assertRaises(ValueError, msg="No items in cart. Please add at least one item."):
            calculate_total("NJ", items)

    def test_zero_total(self):
        items = [
            Item("Milk", "Wic Eligible food", 3.00),
            Item("Bread", "Wic Eligible food", 2.00)
        ]

        with self.assertRaises(ValueError, msg="Total cannot be zero. Please add a taxable item to the cart."):
            calculate_total("DE", items)

    def test_invalid_state(self):
        items = [
            Item("Milk", "Wic Eligible food", 3.00),
            Item("Jeans", "Clothing", 40.00)
        ]

        with self.assertRaises(ValueError, msg="Invalid state. Supported states are 'NJ', 'DE', and 'PA'."):
            calculate_total("NY", items)

if __name__ == '__main__':
    unittest.main()