import string
import random
import pyperclip
import secrets

UPPERCASE_CHARS = string.ascii_uppercase
LOWERCASE_CHARS = string.ascii_lowercase
SPECIAL_CHARS = string.punctuation
NUMBERS = string.digits

upper_input = int(input("Enter number of uppercase letters required: "))
lower_input = int(input("Enter number of lowercase letters required: "))
special_char_input = int(input("Enter number of SPECIAL_CHARS characters required: "))
num_input = int(input("Enter number of NUMBERS required: "))

password = ""

for a in range(0, upper_input):
    random_upper = secrets.choice(UPPERCASE_CHARS)
    password += random_upper
for b in range(0, lower_input):
    random_lower = secrets.choice(LOWERCASE_CHARS)
    password += random_lower
for c in range(0, special_char_input):
    random_special = secrets.choice(SPECIAL_CHARS)
    password += random_special
for d in range(0, num_input):
    random_number = secrets.choice(NUMBERS)
    password += random_number

password_shuffled = ''.join(random.sample(password,len(password)))

pyperclip.copy(password)
print('Your password has been copied to clipboard.')
manual_copy_choice = input('Would you like to see/manually copy your password? (Y/n) :  ').lower()
if manual_copy_choice == 'n':
    pass
else:
    print(password_shuffled)

input("Press any key to exit.")
