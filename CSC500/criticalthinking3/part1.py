# set the amount of months and total rainfall variables to 0
months = 0
total_rainfall = 0

# get number of years
years = int(input("How many years are we looking at?: "))

# loop through the amount of years
for year in range(1, years + 1):
    # loop 12 times per year
    for month in range(1, 13):
        rainfall = int(input("How much rain fell this month in inches?: "))
        total_rainfall += rainfall
        months += 1

# get the average rainfall
average_rainfall = total_rainfall / months

# print the amount of months data captured
print(f"\nYou provided {months} months worth of rainfall")
# print the grand total and average
print(f"There was a grand total of {total_rainfall} inches of rain with an average of {average_rainfall:.2f} inches")
