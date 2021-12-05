import string
from string import punctuation
import random
import pyperclip

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
special = list(punctuation)
num = list(string.digits)


upper_input = input('Enter number of uppercase letters required: ')
lower_input = input('Enter number of lowercase letters required: ')
special_char_input = input('Enter number of special characters: ')
num_input = input('Enter number of numbers needed: ')

a = random.choices(upper, k = int(upper_input))
b = random.choices(lower, k = int(lower_input))
c = random.choices(special, k = int(special_char_input))
d = random.choices(num, k = int(num_input))

str = ""
password = str.join(a + b + c + d) 
password_shuffled = ''.join(random.sample(password,len(password)))
pyperclip.copy(password_shuffled)
print('Your password has been copied to clipboard.')
inp = input('Would you like to see/manually copy your password? (y/n) :  ')
if inp == 'y':
    print(password_shuffled)
else:
    pass

input()
