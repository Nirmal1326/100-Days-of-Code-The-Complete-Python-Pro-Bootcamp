programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."}

# print(programming_dictionary["Bug"])
# print(programming_dictionary)

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])

# programming_dictionary = {}

# print(programming_dictionary)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for mark in student_scores:
    if student_scores[mark] > 90 and student_scores[mark] < 100:
        student_grades[mark] = "Outstanding"
    elif student_scores[mark] > 80 and student_scores[mark] < 90:
        student_grades[mark] = "Exceeds Expectations"
    elif student_scores[mark] > 70 and student_scores[mark] < 80:
        student_grades[mark] = "Acceptable"
    else:
        student_grades[mark] = "Fail"

print(student_grades)