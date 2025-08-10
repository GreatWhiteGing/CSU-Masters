shopping_lists = {}


def create_new_list():
    list_name = input("What is the name of this shopping list? ")
    list_items = input("Enter the items you need to buy: ")
    shopping_lists[list_name] = list_items


def print_shopping_list(shopping_list):
    names = []
    for key in shopping_list.keys():
        names.append(key)
    return names


def get_num_of_lists(shopping_list):
    return len(shopping_list)


user_choice = input("Do you want to create a new list? (Type 'break' to exit) ")
while user_choice != "break":
    if user_choice == "Yes" or user_choice == "yes":
        create_new_list()
        user_choice = input("Do you want to create a new list? (Type 'break' to exit) ")
    else:
        num_of_lists = get_num_of_lists(shopping_lists)
        print(f"\nTotal lists is {num_of_lists}")
        list_names = print_shopping_list(shopping_lists)
        print(f"The names of your list(s) are: {list_names}")
        break
