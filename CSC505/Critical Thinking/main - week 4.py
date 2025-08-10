class Person:
    def __init__(self, name, description):
        self.name = name
        self.description = description


num_of_steps = 0
person_name = input("What is your name? ")
num_of_steps += 1
person_description = input("Tell me something about yourself: ")
num_of_steps += 1
p1 = Person(person_name, person_description)
num_of_steps += 1

person_name = input("What is your name? ")
num_of_steps += 1
person_description = input("Tell me something about yourself: ")
num_of_steps += 1
p2 = Person(person_name, person_description)
num_of_steps += 1

print("\nPerson 1:")
print(f"Name: {p1.name}, Description: {p1.description}")
print("\nPerson 2:")
print(f"Name: {p2.name}, Description: {p1.description}")
print(f"\nNumber of important steps: {num_of_steps}")
