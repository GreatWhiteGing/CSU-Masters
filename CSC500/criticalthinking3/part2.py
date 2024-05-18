# get number of books user has purchased
books = int(input("How many books did you purchase this month?: "))

# checks how many books user purchased and prints their points
if books < 2:
    print(f"You purchased {books} book(s) this month. You earned 0 points")
elif 2 <= books < 4:
    print(f"You purchased {books} books this month. You earned 5 points")
elif 4 <= books < 6:
    print(f"You purchased {books} books this month. You earned 15 points")
elif 6 <= books < 8:
    print(f"You purchased {books} books this month. You earned 30 points")
else:
    print(f"You purchased {books} books this month. You earned 60 points")
