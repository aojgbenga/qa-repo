# Import statistics Library
import statistics

data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

# Split the string by delimiter
grades = data.split(',')

# Cast grades into a list of ints.
grades = list(map(int, grades))

# Display the minimum and maximum grades
print(min(grades))
print(max(grades))

# Calculate the sum of the grades
sum_of_grades = sum(grades)

# Calculate the number of grades
number_of_grades = len(grades)

# Calculate the average grade
average_grade = sum_of_grades / number_of_grades

# Round the average grade to 2 decimal points
average_grade = round(average_grade, 2)

# Display the average grade
print(average_grade)

# Using the statistics library
average = statistics.mean(grades)
print(f"The average of grades is {average:.2f}")

