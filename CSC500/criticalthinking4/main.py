# dictionary with course names as keys and attributes as the values
courses = {
    "CSC101": {
        # nested dictionary to more easily contain all the info for a course
        "room number": 3004,
        "instructor": "Haynes",
        "time": "8:00am"
    },
    "CSC102": {
        "room number": 4501,
        "instructor": "Alvarado",
        "time": "9:00am"
    },
    "CSC103": {
        "room number": 6755,
        "instructor": "Rich",
        "time": "10:00am"
    },
    "NET110": {
        "room number": 1244,
        "instructor": "Burke",
        "time": "11:00am"
    },
    "COM241": {
        "room number": 1411,
        "instructor": "Lee",
        "time": "1:00pm"
    }
}


# function to get course info. course number passed in as an argument
def get_course_info(course_number):
    # setting default values to be updated if course is found
    room_number = 0
    instructor = ""
    time = ""
    # if the course is not found inform the user and break out
    if course_number not in courses:
        print(f"{course_number} is not one of the listed courses")
        return
    else:
        # loops through keys in courses dictionary
        for key in courses.keys():
            if key == course_number:
                # once found, reassigns the variables
                room_number = courses[key]["room number"]
                instructor = courses[key]["instructor"]
                time = courses[key]["time"]
    # prints the course number that was selected and all the information
    print(f"{course_number}:")
    print(f"Room: {room_number}, Instructor: {instructor}, Meeting Time:{time}")


# get the course the user wants information for
selected_course = input("What course would you like information for? ").upper()
# call the function and pass the user input in as an argument
get_course_info(selected_course)
