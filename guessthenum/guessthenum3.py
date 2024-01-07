import random
def askinteger():
    while True:
        try:
            a = input()
            val = int(a)
            return val 
        except ValueError:
            print("That's not an integer! Try again.")
correct_answer=random.randint(0,100)
min_number=0
max_number=100
numofguess=8
score=0
while True:
    print("Guess a number between",min_number,"to",max_number)
    print("You have",numofguess,"chance left.")
    print("Your score:",score)
    guess=askinteger()
    numofguess=numofguess-1
    if guess==correct_answer:
        max_number=100
        min_number=0
        numofguess=8
        score=score+1
        print("You win!","Guess a number between",min_number,"to",max_number)
        correct_answer=random.randint(0,100)
    elif numofguess==0:
        max_number=100
        min_number=0
        numofguess=8
        score=score-1
        print("Game over! Your score will -1!")
        correct_answer=random.randint(0,100)
    elif guess>correct_answer: #guess=70  correct answer=50
        if guess<max_number:
            max_number=guess
    elif guess<correct_answer:  #guess=50  correct answer=70
        if guess>min_number:
            min_number=guess
        
        