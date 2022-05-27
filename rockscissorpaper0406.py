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

# Write your code below this line 👇
images = [rock, paper, scissors]

my = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if my >= 3 or my < 0:
  print("You typed an invalid number, you lose!")
else :
  print(images[my])
  computer = random.randint(0, 2)
  print("Computer chose:")
  print(images[computer])

  if my == 0 and computer == 2:
    print("You win!")
  elif computer == 0 and my == 2:
    print("You lose")
  elif computer > my:
    print("You lose")
  elif my > computer:
    print("You win!")
  elif computer == my:
    print("It's a draw")



