import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = has_special and meets_criteria

    return pwd



min_length = int(input("Enter the minimum length of the password: "))
numbers = input("Do you want to include numbers? (yes/no): ").lower() == 'yes'
special_characters = input("Do you want to include special characters? (yes/no): ").lower() == 'yes'

pwd = generate_password(min_length, numbers, special_characters)
print("The generated password is:", pwd)