from dataclasses import dataclass
from record import items

@dataclass
class Item:
    name: str
    item_type: str
    price: float


def calculate_total(state, items):
    def is_fur_clothing(item):
        return "clothing" in item.item_type.lower() and "fur" in item.name.lower()

    def is_tax_exempt(item, state):
        if "wic eligible food" in item.item_type.lower():
            return True
        if "clothing" in item.item_type.lower() and state in ["PA", "NJ"] and not is_fur_clothing(item):
            return True
        return False

    def apply_sales_tax(item, state):
        if is_tax_exempt(item, state):
            return item.price
        elif state == "NJ":
            return item.price * 1.066
        elif state == "PA":
            return item.price * 1.06
        else:
            return item.price

    if state not in ["NJ", "DE", "PA"]:
        raise ValueError("Invalid state. Supported states are 'NJ', 'DE', and 'PA'.")

    if not items:
        raise ValueError("No items in cart. Please add at least one item.")

    total = 0
    for item in items:
        if not item.item_type:
            raise ValueError("Item type cannot be empty.")
        total += apply_sales_tax(item, state)

    if total == 0:
        raise ValueError("Total cannot be zero. Please add a taxable item to the cart.")

    return total

def main():
    print("Please select your state:")
    print("1. New Jersey (NJ)")
    print("2. Delaware (DE)")
    print("3. Pennsylvania (PA)")

    state_choice = input("Enter the number corresponding to your state: ")

    state_map = {
        "1": "NJ",
        "2": "DE",
        "3": "PA"
    }

    if state_choice in state_map:
        state = state_map[state_choice]
    else:
        raise ValueError("Invalid choice. Please enter a number between 1 and 3.")

    total = calculate_total(state, items)
    print(f"The total to charge a customer at checkout: ${total:.2f}")

if __name__ == "__main__":
    main()