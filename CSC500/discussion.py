# random test scores
test_scores = [85, 89, 92, 78, 99, 86, 92]
# get the length of the array
length = len(test_scores)
# set the highest score to the first entry in the array
highest_score = test_scores[0]
# set average to 0
average_score = 0

# loop through the array and compare score to the highest
for i in range(0, len(test_scores)):
    if test_scores[i] > highest_score:
        # if new score is higher, replace existing score with new
        highest_score = test_scores[i]

# loop through the array and add all scores together
for i in range(0, len(test_scores)):
    average_score = average_score + test_scores[i]

# get the average score
average_score = average_score / length

# output the highest score and average score
print(f"Your highest score was {highest_score}")
print(f"Out of {length} scores, that's an average of {average_score:.2f}")
