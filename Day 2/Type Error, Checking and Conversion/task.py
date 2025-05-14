# TypeError
# len(123)

# No TypeError
print(len("Hello"))

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# solution 1
print("Number of letters in your name: " + str(len(input("Enter your name"))))
# solution 2
name_length = len(input("Enter your name"))
print("Number of letters in your name: " + str(name_length))
# solution 3
name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)
print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int
print("Number of letters in your name: " + str(length_of_name))