import random

computer = random.choice(["stone", "paper", "scissors"])
you = input("Enter your choice (stone or paper or scissors): ").lower()
print(f"You choose {you}")
print(f"Computer choose {computer}")
if computer == you:
    print("It's tie!")
elif computer == "stone" and you == "paper":
    print("You won!")
elif computer == "paper" and you == "scissors":
    print("You won!")
elif computer == "scissors" and you == "stone":
    print("You won!")
elif computer == "stone" and you == "scissors":
    print("You lose!")
elif computer == "paper" and you == "stone":
    print("You lose!")
elif computer == "scissors" and you == "paper":
    print("You lose!")
else:
    print("Invalid input. Type stone, paper or scissors")