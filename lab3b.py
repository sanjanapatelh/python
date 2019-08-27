import string
import random

str1 = string.printable

for i in range(6):
    print(str1[random.randint(0,100)],end="")
