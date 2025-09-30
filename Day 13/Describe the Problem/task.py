def my_function():
#    for i in range(1, 20): # Before debugging
     for i in range(1, 21): # After debugging
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
       # For loop is passing the int values from 1 to 19
# 2. When is the function meant to print "You got it"?
       # The if condition meant "You got is" when (i) met 20
# 3. What are your assumptions about the value of (i)?
       # (i) will go from 1 to 19 because the rage of the for loop is meant as 1 to 20,
#        so it goes up to 19 because that's how rage works in python.
#        So if we change the range to 21, we can see the "You got it"
#        in the output console.