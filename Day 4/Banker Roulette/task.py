import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# option 1
friends_name = random.randint(0,4)
print(friends[friends_name])

# option 2
print(random.choice(friends))