import random

choices = ['rock', 'paper', 'scissors']
player = input("Choose rock, paper, or scissors: ").lower()
computer = random.choice(choices)
print("Computer chose:", computer)

if player == computer:
    print("🤝 It's a tie!")
elif (player, computer) in [('rock','scissors'), ('scissors','paper'), ('paper','rock')]:
    print("🎉 You win!")
else:
    print("😢 You lose!")
