# class definition
class ItemToPurchase:
    # setting default values for name, price, and quantity
    def __init__(self, name="none", price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

    # class method to calculate the item cost
    def print_item_cost(self):
        self.price = int(self.price)
        self.quantity = int(self.quantity)
        # use a return statement in order to save the string to a variable to print later
        return f"{self.name} {self.quantity} @ ${self.price} = ${self.quantity * self.price}"


# get item 1 information
print("Item 1")
item1_name = input("Enter the item name: ")
item1_price = int(input("Enter the item price: "))
item1_quantity = int(input("Enter the item quantity: "))

# get item 2 information
print("Item 2")
item2_name = input("Enter the item name: ")
item2_price = int(input("Enter the item price: "))
item2_quantity = int(input("Enter the item quantity: "))

# create an ItemToPurchase class object
item1 = ItemToPurchase(item1_name, item1_price, item1_quantity)
# invoke the print_item_cost method
item1_cost = item1.print_item_cost()

# repeat for item 2
item2 = ItemToPurchase(item2_name, item2_price, item2_quantity)
item2_cost = item2.print_item_cost()

print("TOTAL COST")
print(item1_cost)
print(item2_cost)
print(f"Total ${(item1.price * item1.quantity) + (item2.price * item2.quantity)}")
