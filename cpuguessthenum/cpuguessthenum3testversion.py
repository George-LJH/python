import random
import math
import time
def askinteger():
    while True:
        try:
            a = input()
            val = int(a)
            return val 
        except ValueError:
            print("That's not an integer! Try again.")
        except if val not 
correct_answer=random.randint(0,100)
min=0
max=100
cpuguess=(math.ceil((min+max)/2))
numofguess=8
score=0
print("Think of a number between 0 to 100 and the cpu will guess it!")
answer=askinteger()
while True:
        max=100
        min=0
        numofguess=8
        score=score+1
        print("Your number is...",answer,"!")
        print("Think of a number between 0 to 100 and the cpu will guess it!")
        answer=askinteger()
    elif numofguess==0:
        max=100
        min=0
        numofguess=8
        score=score-1
        print("Game over! The cpu can't guess your number! What is your new number?")
        answer=askinteger()
    if cpuguess>answer:
        if cpuguess<max:
            print("1...")
            time.sleep(0.5)
            print("2...")
            time.sleep(0.5)
            print("3...")
            time.sleep(0.5)
            print("Cpu is guessing...",cpuguess)
            print("Incorrect!")
            max=cpuguess
            print(min,"to",max)
            cpuguess=(math.ceil((min+max)/2))
            time.sleep(1)
    if cpuguess<answer:  #guess=50  correct answer=70
        if cpuguess>min:
            print("1...")
            time.sleep(0.5)
            print("2...")
            time.sleep(0.5)
            print("3...")
            time.sleep(0.5)
            print("Cpu is guessing...",cpuguess)
            print("Incorrect!")
            min=cpuguess
            print(min,"to",max)
            cpuguess=(math.ceil((min+max)/2))
            time.sleep(1)