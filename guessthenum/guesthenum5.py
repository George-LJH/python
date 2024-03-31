import random
from tkinter import *

lower = 50
upper = 50
target= 50
gameOver=False

def startGame():
    global lower
    global upper
    global target
    global gameOver
    lower = 1
    upper = 100
    target=random.randrange(lower,upper+1)
    gameOver=False
    message="Guess A Number from %d to %d" % (lower, upper)
    updateGUI(message)   

def checkGuess():
    global lower
    global upper
    global target
    global gameOver
    guess = EntryGuess.get()
    guessInt = int(guess, 10)
    message=""
    if(gameOver):
        return startGame()
    
    if(guessInt == target):
        message = "Correct, the answer is %d!!" % target
        gameOver=True
        return updateGUI(message)

    if (guessInt < lower) or (guessInt > upper):
        message="Wrong Input!!"
    elif (guessInt > target):
        upper=guessInt
    elif (guessInt < target):
        lower=guessInt
    else:
        message="Impossible!!"
    message= message + "Guess A Number from %d to %d" % (lower, upper)
    return updateGUI(message)

def updateGUI(theMessage):
    global lower
    global upper
    global target
    global gameOver
    LabelLower.configure(text=lower)
    LabelUpper.configure(text=upper)
    LabelMessage.configure(text=theMessage)
    if(gameOver):
        ButtonCheck.configure(text="Restart?")
    else:
        ButtonCheck.configure(text="Check My Guess")

# create root window
root = Tk()
root.title("Guess 0 to 100")
root.geometry('360x150')

#column=0
LabelMessage = Label(root,width=40,text="")
LabelMessage.grid(column=0, row=0,columnspan=2)

Label(root,width=20,text="From").grid(column=0, row=1)
Label(root,width=20,text="To").grid(column=0, row=2)
Label(root,width=20,text="Your Guess:").grid(column=0, row=3)
ButtonCheck = Button(root,width=40, text = "", command=checkGuess)
ButtonCheck.grid(column=0, row=4,columnspan=2)

#column=1
LabelLower = Label(root,width=20,text="")
LabelLower.grid(column=1, row=1)
LabelUpper = Label(root,width=20,text="")
LabelUpper.grid(column=1, row=2)
EntryGuess = Entry(root,width=20, text=IntVar(value=99))
EntryGuess.grid(column=1, row=3)


startGame()

#Start the GUI
root.mainloop()