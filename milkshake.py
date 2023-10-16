shakes = {
  "vanilla": 1,
  "chocolate": 2,
  "strawberry": 3
}

budget = float(input("Enter your budget: £"))

while True:
  print("\nWhat can I fix you?")
  for milkshake, price in shakes.items():
    print(f"{milkshake}: £{price}")

  choice = input("Enter your choice (or 'Q' to quit): ").lower()

  if choice == "q":
    break

  if choice not in shakes:
    print("Invalid choice.")
  else:
    if shakes[choice] > budget:
      print("You don't have enough money.")
    else:
      print(f"Here is your {choice} milkshake. Enjoy!")
      budget -= shakes[choice]
      print(f"Remaining budget: £{budget:.2f}")

print("Thank you for coming. I hope you find love soon.")
