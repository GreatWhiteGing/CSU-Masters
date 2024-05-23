# class definition
class ItemToPurchase:
    # setting default values for name, price, quantity and description
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    # class method to calculate the item cost
    def print_item_cost(self):
        self.price = float(self.price)
        self.quantity = int(self.quantity)
        # use a return statement in order to save the string to a variable to print later
        return f"{self.name} {self.quantity} @ ${self.price} = ${self.quantity * self.price}"


# shopping cart class definition
class ShoppingCart:
    # setting default values for customer name, current date, and cart items list
    def __init__(self, customer_name="none", current_date="January 1, 2020", cart_items=None):
        self.cart_items = [] if not cart_items else cart_items
        self.customer_name = customer_name
        self.current_date = current_date

    # method to add item to cart_items list
    def add_item(self):
        name = input("Enter the item name: ")
        description = input("Enter the item description: ")
        price = float(input("Enter the item price: $"))
        quantity = int(input("Enter the item quantity: "))
        self.cart_items.append(ItemToPurchase(name, price, quantity, description))

    # method to remove item from cart_items list
    def remove_item(self):
        item_to_remove = input("What do you want to remove?: ")
        i = 0
        for item in self.cart_items:
            if item.name == item_to_remove:
                del self.cart_items[i]
                break
            else:
                flag = False
            i += 1
            if not flag:
                print("Item not found in cart. nothing removed")

    # method to modify attributes of an item in cart_items list
    def modify_item(self):
        item_to_modify = input("What item are you changing?: ")
        for item in self.cart_items:
            if item.name == item_to_modify:
                price = float(input("Enter new price: $"))
                quantity = int(input("Enter new quantity: "))
                description = input("Enter new description: ")
                item.price = price
                item.quantity = quantity
                item.description = description
                flag = True
                break
            else:
                flag = False
        if not flag:
            print("Item not found in cart. Nothing modified")

    # method to get the total items in cart_items
    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.quantity
        return num_items

    # method to calculate the total cost of items in cart_items
    def get_cost_of_cart(self):
        total_cost = 0
        cost = 0
        for item in self.cart_items:
            cost = item.quantity * item.price
            total_cost += cost
        return total_cost

    # method to print total cost of items in cart_items
    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(total_cost)

    # method to print the item name and description from cart_items
    def print_descriptions(self):
        print("\nOUTPUT ITEMS' DESCRIPTIONS")
        print(f"{customer_name}'s Shopping Cart - {current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

    # method to output the current shopping cart information
    def output_cart(self):
        print("\nOUTPUT SHOPPING CART")
        print(f"{customer_name}'s Shopping Cart - {current_date}")
        print("Number of Items: ", self.get_num_items_in_cart())
        if self.get_num_items_in_cart() == 0:
            print("SHOPPING CART IS EMPTY")
        total = 0
        for item in self.cart_items:
            print(f"{item.name} {item.quantity} @ ${item.price} = ${item.price * item.quantity}")
            total += item.quantity * item.price
        print(f"Total: ${total}")


# function to continually display the menu to the user
def print_menu(shoppingcart):
    customer_cart = newcart
    shopping = True
    while shopping:
        print("\nMenu")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item price/quantity/description")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice.lower() == "a":
            customer_cart.add_item()
        if choice.lower() == "r":
            customer_cart.remove_item()
        if choice.lower() == "c":
            customer_cart.modify_item()
        if choice.lower() == "i":
            customer_cart.print_descriptions()
        if choice.lower() == "o":
            customer_cart.output_cart()
        if choice.lower() == "q":
            shopping = False


customer_name = input("Enter customer name: ")
current_date = input("Enter today's date: ")
newcart = ShoppingCart(customer_name, current_date)
print_menu(newcart)
