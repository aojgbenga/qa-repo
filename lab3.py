### Task 1 Using while loops
#i = 1
#while i**2 <= 2000:
#  print(i, i**2)
#  i += 1


### Task 2 Factorial
# Get the user's input
#num = int(input("Enter an integer: "))

# Initialize the factorial variable and the product string
#factorial = 1
#product_string = ""

# Calculate the factorial of the number using a while loop
#while num > 0:
#  factorial *= num
#  product_string += str(num) + "*"
#  num -= 1

# Remove the last asterisk from the product string
#product_string = product_string[:-1]

# Print the factorial of the number
#print(f"The factorial of {product_string} is {factorial}")


### Task 3 Investment
#initial_investment = 100
#target_value = 1000
#interest_rate = 10

#years = 0
#while initial_investment < target_value:
#  initial_investment += initial_investment * interest_rate / 100
#  years += 1

#print(f"It will take {years} years to reach the target value.")


### Task 4 Input an Integer Between Two Limits

#min_value = 1
#max_value = 100

#attempts = 0
#while attempts < 3:
#  user_input = input(f"Enter an integer between {min_value} and {max_value}: ")

  # Check if the input is an integer
#  if not user_input.isdigit():
#    print("Invalid input. Please enter an integer.")
#    attempts += 1
#    continue

  # Check if the input is within the range of min and max values
#  if int(user_input) < min_value or int(user_input) > max_value:
#    print("Invalid input. Please enter an integer between {} and {}.".format(min_value, max_value))
#    attempts += 1
#    continue

  # If we reach here, the input is a valid integer within the range
#  print(f"You entered {user_input}.")
#  break

# If the user has tried three times and failed, print None
#if attempts == 3:
#  print(None)

### Task 5 Count vowels in a word

# Get the word from the user
word = input("Enter a word: ")

# Initialize a counter for the number of vowels
vowel_count = 0

# Iterate over each character in the word
for character in word:
  # Check if the character is a vowel
  if character in ["a", "e", "i", "o", "u"]:
    # Increment the vowel count
    vowel_count += 1

# Print the number of vowels in the word
print(f"The word {word} has {vowel_count} vowels.")


### Task 6 Exam average
# Get the marks from the user
math_mark = 0
english_mark = 0
ict_mark = 0

# Validate the math mark
while math_mark < 0 or math_mark > 100:
  math_mark = int(input("Enter your math mark: "))

# Validate the English mark
while english_mark < 0 or english_mark > 100:
  english_mark = int(input("Enter your English mark: "))

# Validate the ICT mark
while ict_mark < 0 or ict_mark > 100:
  ict_mark = int(input("Enter your ICT mark: "))

# Calculate the average mark
average_mark = (math_mark + english_mark + ict_mark) / 3

# Print the average mark
print(f"Your average mark is {average_mark}.")

# Print whether the student passed or failed
if average_mark >= 65:
  print("You passed!")
else:
  print("You failed.")

# Print the average class mark
print(f"The average class mark is {average_mark}.")

### For loops Task 1
for i in range(1, 101):
  square = i * i
  if square > 2000:
    break
  print(i, square)

