# Ask for a, b and c integer coefficents and calculate the delta
a = int(input("What is a?"))
b = int(input("What is b?"))
c = int(input("What is c?"))
delta = b ** 2 - 4 * a * c

# The different cases
if (a == 0):
    print("That isn't a quadratic! a can't be zero!")
elif (delta > 0):
    print("The roots are", (-b - delta ** 0.5) / (2 * a), "and", (-b + delta ** 0.5) / (2 * a))
elif (delta == 0):
    print("The root is", (-b) / (2 * a))
elif (delta < 0):
    print("There are no real roots")
else:
    print("Unknown error.")

# Exit
quit()