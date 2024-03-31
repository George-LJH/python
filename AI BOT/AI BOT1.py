print("AI: Hello. How may I help you today? You can say simple commands like:")
print(" Tell me a knock knock joke")
print(" Knock Knock")
print(" Tell me a joke")
user= input()
# user=user.lower()
print(user)
while True:
    if user=="knock knock":
        print("TST")
        user=input()
        # user=user.lower()
    elif user=="tell me a joke":
        print("TST2")
        user=input()
        # user=user.lower()
    elif user!= "knock knock" or "tell me a joke":
        print("ERROR")
        user=input
        # user=user.lower()
