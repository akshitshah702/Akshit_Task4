# task 4 q12
def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as ze:
    print("Cannot be divided by ZERO!!")
except:
    print("Any other exception")