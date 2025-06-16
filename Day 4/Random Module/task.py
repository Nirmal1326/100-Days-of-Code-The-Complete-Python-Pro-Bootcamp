import random
random_integer = random.randint(1, 10)
print(random_integer)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

decision = random.randint(0,1)
# print(decision)
if decision == 1:
    print("Heads")
else:
    print("tails")