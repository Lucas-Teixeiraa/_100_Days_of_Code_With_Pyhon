import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Let's Play Rock, Paper and Scissor!!")
print("------------------------------------")
print("------------------------------------")
print("------------------------------------")

playerChoose = input("What's your choose?\n")

computerRandomChoose = [scissors, paper, rock]
computerChoose = random.choice(computerRandomChoose)

if playerChoose == 'paper' and computerChoose == scissors:
    print(f"player choose: {paper}")
    print(f"computer choose: {computerChoose}")
    print("Computer Win!")
elif playerChoose == 'rock' and computerChoose == paper:
    print(f"player choose: {rock}")
    print(f"computer choose: {computerChoose}")
    print("Computer Win!")
elif playerChoose == 'scissor' and computerChoose == rock:
    print(f"player choose: {scissors}")
    print(f"computer choose: {computerChoose}")
    print("Computer Win!")
elif playerChoose == computerChoose:
    print("DRAWN! =0")
else:
    print("You Win!")



