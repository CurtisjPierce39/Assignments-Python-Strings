# Question 2 Task 1 

#Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")
if len(first_name) <= 2:
    print("Error:First name is too short. Please try again.")
elif len(last_name) <= 2:
    print("Error:Last name is too short. Please try again.")
else:
    print(first_name, last_name)