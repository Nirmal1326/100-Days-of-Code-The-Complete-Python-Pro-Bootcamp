# Lesson 1 (Working with Attributes, Class Constructors and the __init__() Function)

class Car:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name

driver_1 = Car("001","lucifer")

print(driver_1.id,driver_1.username)

# driver_2 = Car()
# driver_2.id = "002"
# driver_2.username = "Joe"

# Lesson 2 (Adding method to a class)

class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001","Lucifer")
user_2 = User("002","Trixie")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)