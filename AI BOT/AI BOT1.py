print("AI: Hello. How may I help you today? You can say simple commands like:")
print(" Tell me a knock knock joke")
print(" Knock Knock")
print(" Tell me a joke")
user= input()
user= user.lower()



while True:
    while user!="tell me a joke" or "knock knock":
        print("Sorry, I don't understand. Can you please repeat your request?")
        user= input()
        user= user.lower()
    elif user=="tell me a joke":
        print("Where do pigs go to school?")
        print("Hogwarts!")
        user= input()
        user= user.lower()
    elif user=="knock knock":
        print("Who's there?")
        user= input()
        user= user.lower()
        print("user", "who?")
        user= input()
        user= user.lower()
        print("Ha ha! That's a funny joke!")
    elif user=="exit()":
        exit()
