### Part 01
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

# Get the age numbers in the list
length_ages = len(ages)
print(length_ages)

# Display the total ages in the list using for loop
for i in ages:
    print(i)

# Add one year to every age
for i in ages:
    i += 1
    print(i)

# Filter for ages 16 to 65
ages_16_to_65 = []

for x in ages:
    if x >= 16 and x < 65:
        ages_16_to_65.append(x)
print(ages_16_to_65)

# Print out ages 16 to 65
length_ages_16_to_65 = len(ages_16_to_65)
print (length_ages_16_to_65)

# Sort the ages using the sort method
ages_16_to_65.sort()
print(ages_16_to_65)

### Task 2 Count vowels in a word

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
