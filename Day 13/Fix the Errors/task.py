# Before debugging (The problem is it works fine with numeric input,
# but if the user has entered the string value, it crashes.

# age = int(input("How old are you?"))
# if age > 18:
#     print("You can drive at age {age}.")

# After debugging
try:
    age = int(input("How old are you? "))
except ValueError:
    print("You have entered a invalid number. Please try again with numerical value like (1, 2, 3, ...)")
    age = int(input("How old are you? "))

if age > 18:
    print(f"You can drive at age {age}.")