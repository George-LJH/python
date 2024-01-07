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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    mylist = ["rock", "paper", "scissor"]

    cpu=random.choice(mylist)

    print("Rock, paper, or scissor?: ")
    user = input("")
    print("User: ")
    #print user
    if user=="scissor":
        print(scissor)
    if user=="rock":
        print(rock)
    if user=="paper":
        print(paper)
    if user not in mylist:
        print("wrong input")
    else:
        #print cpu
        if cpu=="paper":
            print("cpu: "+paper)
        if cpu=="rock":
            print("cpu: "+rock)
        if cpu=="scissor":
            print("cpu: "+scissor)
        # win lose condition
        if cpu=="rock":
            if user=="paper":
                print("You win")
        if cpu=="paper":
            if user=="rock":
                print("You lose")
        if cpu=="scissor":
            if user=="rock":
                print("You win")
        if cpu=="rock":
            if user=="scissor":
                print("You lose")
        if cpu=="scissor":
            if user=="paper":
                print("You lose")
        if cpu=="paper":
            if user=="scissor":
                print("You win")
        if cpu==user:
            print("Tie")