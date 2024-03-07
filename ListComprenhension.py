# list comprenhension = a way to create a new list with less syntax.
#                       Can mimic certain lambda expressions, easier to read
#                       syntaxis, three ways: list = [expression for item in iterable]
#                                             list = [expression for item in iterable if conditional]
#                                             list = [expression if/else for item in iterable]

# Exercise 1 -----------------------------
# Long way
squarePower = []                # creating an empty list
for i in range(1,11):           # creating a for loop
    squarePower.append(i*i)     # define what each loop interaction will do
print(squarePower)

# Short way
squarePower = [i*i for i in range(1,11)] # list comprenhension used here: list = [expression for item in iterable]
print(squarePower)

# Exercise 2 -----------------------------
# Long way
studentsGrades = [95, 75, 35, 60, 50, 45, 30, 90]
passingStudents = list(filter(lambda x:x>=60, studentsGrades)) 
print(passingStudents)

# Short way
passingStudents = [i for i in studentsGrades if i >= 60] # list comprenhension used here: list = [expression for item in iterable if conditional]
print(passingStudents)

passingStudents = [i if i >= 60 else "Failed" for i in studentsGrades] # Using an if/else statement. 
                                                                    # List comprenhension used here: 
                                                                    # list = [expression if/else for item in iterable]}
print(passingStudents)
