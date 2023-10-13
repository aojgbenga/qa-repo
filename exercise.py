#y = int(input("What is your grade ?"))

#if y > 85:
#  print("Congtats its a distinction")
#elif y >= 65 and y<= 85:
#  print("Congrats its a pass")
#else:
#  print("Sorry you failed the exam")

# Weight converter app
#weight = float(input("What is your weight ?"))
#unit = input("Enter your preferred unit (Kgs/Lbs): ").lower()
#if unit == "kgs":
#    converted_weight = weight * 2.20462
#    print(f"{weight} Kgs is equal to {converted_weight} Lbs.")
#elif unit == "lbs":
#    converted_weight = weight / 2.20462
#    print(f"{weight} Lbs is equal to {converted_weight} Kgs.")
#else:
#    print("Invalid unit input. Please enter Kgs or Lbs.")

 
# counter variable to keep track of the number of people
counter = 0

while counter < 5:

    # ask for the name of the person
    name = input("Enter your name: ")

    # print out the person's name, followed by the text "is awesome"
    print(f"{name} is awesome!")

    # increment the counter by 1
    counter += 1
