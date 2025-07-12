# # Exercise 1: Vowel or Consonant
# #
# # Write a Python function named `check_letter` that determines if a given letter
# # is a vowel or a consonant.
# #
# # Requirements:
# # - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# # - It should handle both uppercase and lowercase letters.
# # - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# # - If the letter is a consonant, print: "The letter x is a consonant."
# # - Replace 'x' with the actual letter entered by the user.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Utilize the `in` operator to check for vowels.
# # - Ensure to provide feedback for non-alphabetical or invalid entries.

# def check_letter():
#     # Your control flow logic goes here
#     letter = input("enter a letter (a-z or A-Z):").lower()
#     if not letter.isalpha() or len(letter) > 1:
#         print("enter single letters only")
#     else:
#         if letter in "aeiou":
#             print(f"The letter {letter} is a vowel") 
#         else:
#             print(f"The letter {letter} is a consonant")
# #
# # Call the function
# check_letter()


# # Exercise 2: Old enough to vote?
# #
# # Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# # Fill in the logic to perform the eligibility check inside the function.
# #
# # Function Details:
# # - Prompt the user to input their age: "Please enter your age: "
# # - Validate the input to ensure the age is a possible value (no negative numbers).
# # - Determine if the user is eligible to vote. Set a variable for the voting age.
# # - Print a message indicating whether the user is eligible to vote based on the entered age.
# #
# # Hints:
# # - Use the `input()` function to capture the user's age.
# # - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# # - Use a conditional statement to check if the age meets the minimum voting age requirement.

# def check_voting_eligibility():
#     # Your control flow logic goes here
#     age = int(input("Please enter your age:"))
#     voting_age = 18
#     if age <1:
#         print("enter positive number")
#     else:
#         print("you can vote" if age >=voting_age else "you cant vote")

# # Call the function
# check_voting_eligibility()


# # Exercise 3: Calculate Dog Years
# #
# # Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# # Fill in the logic to perform the calculation inside the function.
# #
# # Function Details:
# # - Prompt the user to enter a dog's age: "Input a dog's age: "
# # - Calculate the dog's age in dog years:
# #      - The first two years of the dog's life count as 10 dog years each.
# #      - Each subsequent year counts as 7 dog years.
# # - Print the calculated age: "The dog's age in dog years is xx."
# # - Replace 'xx' with the calculated dog years.
# #
# # Hints:
# # - Use the `input()` function to capture user input.
# # - Convert the string input to an integer using `int()`.
# # - Apply conditional logic to perform the correct age calculation based on the dog's age.

# def calculate_dog_years():
#     # Your control flow logic goes here
#     dog_age =int(input("input a dog's age:"))
#     culcated_age=0
#     for age in range(dog_age+1):
#         if age == 1 or age == 2:
#             culcated_age +=10
#         elif age >2:
#             culcated_age +=7
#     print(f"The dog's age in dog years is {culcated_age}.")

# # Call the function
# calculate_dog_years()


# # Exercise 4: Weather Advice
# #
# # Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
# #
# # Requirements:
# # - The script should prompt the user to enter if it is cold (yes/no).
# # - Then, ask if it is raining (yes/no).
# # - Use logical operators to determine clothing advice:
# #   - If it is cold AND raining, print "Wear a waterproof coat."
# #   - If it is cold BUT NOT raining, print "Wear a warm coat."
# #   - If it is NOT cold but raining, print "Carry an umbrella."
# #   - If it is NOT cold AND NOT raining, print "Wear light clothing."
# #
# # Hints:
# # - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

# def weather_advice():
#     # Your control flow logic goes here
#     isCold = input("enter if it is cold (yes/no): ")
#     isRaining = input("enter if it is raining (yes/no): ")
#     if isCold =="yes" and isRaining =="yes":
#         print("Wear a waterproof coat")
#     elif isCold =="yes" and isRaining == "no":
#         print("Wear a warm coat")
#     elif isCold =="no" and isRaining =="yes":
#         print("Carry an umbrella")
#     elif isCold =="no" and isRaining =="no":
#         print("Wear light clothing")
#     else:
#         print("enter yes or no only")

# # Call the function
# weather_advice()