import string
import random
letters = string.ascii_letters
random_string = ""
for i in range(5):
    random_string += random.choice(letters)

print(random_string)