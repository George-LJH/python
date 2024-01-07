import random

def print_hand(hand):
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

    scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
    if hand=="scissor":
        print(scissor)
    if hand=="rock":
        print(rock)
    if hand=="paper":
        print(paper)

def checkwinlose(userhand,cpuhand):
    if cpuhand=="rock":
        if userhand=="paper":
            print("You win")
    if cpuhand=="paper":
        if userhand=="rock":
            print("You lose")
    if cpuhand=="scissor":
        if userhand=="rock":
            print("You win")
    if cpuhand=="rock":
        if userhand=="scissor":
            print("You lose")
    if cpuhand=="scissor":
        if userhand=="paper":
            print("You lose")
    if cpuhand=="paper":
        if userhand=="scissor":
            print("You win")
    if cpuhand==userhand:
        print("Tie")
    

while True:
    mylist = ["rock", "paper", "scissor"]

    cpu=random.choice(mylist)
    print("Rock, paper, or scissor?: ")
    user = input()
    #print user
    print("User: ")
    print_hand(user)
    if user not in mylist:
        print("wrong input")
    else:
        #print cpu
        print("cpu:")
        print_hand(cpu)
        # win lose condition
        checkwinlose(user,cpu)
