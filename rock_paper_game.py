import random
class RockPaperScissors:
    def __init__(self):
        self.rounds_played = 0
        self.user_wins = 0
        self.computer_wins = 0

    def play_round(self):
        # Get the user's choice
        user_choice = input("Choose rock, paper, or scissors: ")

        # Generate the computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the winner
        winner = self.determine_winner(user_choice, computer_choice)

        # Update the round count and wins
        self.rounds_played += 1
        if winner == "user":
            self.user_wins += 1
        elif winner == "computer":
            self.computer_wins += 1

        # Display the results
        print(f"You chose {user_choice} and the computer chose {computer_choice}.")
        print(f"The winner is {winner}!")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == "rock" and computer_choice == "scissors":
            return "user"
        elif user_choice == "scissors" and computer_choice == "paper":
            return "user"
        elif user_choice == "paper" and computer_choice == "rock":
            return "user"
        elif user_choice == computer_choice:
            return "tie"
        else:
            return "computer"

    def play_again(self):
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")

        # If the user says yes, play another round
        if play_again == "y":
            self.play_round()

        # Otherwise, exit the program
        else:
            print("Thank you for playing!")
            print(f"You won {self.user_wins} rounds.")
            print(f"The computer won {self.computer_wins} rounds.")
            print(f"There were {self.rounds_played - self.user_wins - self.computer_wins} ties.")

# Example usage:

game = RockPaperScissors()

# Play the game
game.play_round()

# Ask the user if they want to play again
game.play_again()
