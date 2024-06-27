import math
def square(storona):
    if storona.is_integer() == True:
        print(storona ** 2)
    else:
        print(math.ceil(storona ** 2))
square(3.22)
