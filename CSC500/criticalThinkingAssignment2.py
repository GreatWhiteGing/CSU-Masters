# ask the user to input how much they spent for a subtotal
subtotal = float(input("How much did you spend tonight? "))


# function that takes in the subtotal to calculate the grand total
def calculate_total(meal_amount):
    # 7% tax rate
    tax_rate = 7 / 100
    # 18% tip
    tip = 18 / 100
    # get total with tax
    total_with_tax = (meal_amount * tax_rate) + meal_amount
    # add tip to that total for grand total
    grand_total = (total_with_tax + tip) + meal_amount
    return grand_total


# call function to get grand total
total = calculate_total(subtotal)
# display how much they spent and a message based on the grand total
if total < 18.00:
    print(f"Look at that, your grade total is ${total:.2f}. You got out cheap!")
elif 18.00 <= total <= 30.00:
    print(f"Look at that, your grade total is ${total:.2f}. That's pretty standard average.")
else:
    print(f"Look at that, your grade total is ${total:.2f}. Hope you got a raise at work to cover this...")
