print("AI: Hello. How may I help you today? You can say simple commands like:")


print(" Tell me a knock knock joke")
print(" Knock Knock")
print(" Tell me a joke")
user= input()
# user=user.lower()

while True:

    if user.lower()=="knock knock":
        print("who's there?")
        user=input()
        print(user,"who?")
        print("Ha ha! That's a funny joke!")
        user=input()
        # user=user.lower()
    elif user.lower()=="tell me a joke":
        print("Where do pigs go to school?")
        print("Hogwarts!")
        user=input()
        # user=user.lower()
    elif user.lower()!= "knock knock" or "tell me a joke":
        print("A")
        user=input()


        # user=user.lower()
