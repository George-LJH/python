from googlesearch import search
print("AI: Hello. How may I help you today? You can say simple commands like:")

print(" Hi")
print(" Tell me a knock knock joke")
print(" Knock Knock")
print(" Tell me a joke")
print(" exit()")
user= input()
# user=user.lower()

while True:

    if user.lower()=="knock knock":
        print("AI: who's there?")
        user=input()
        print(user,"who?")
        user=input()
        print("AI: Ha ha! That's a funny joke!")
        user=input()
        # user=user.lower()
    elif user.lower()=="tell me a joke":
        print("AI: Where do pigs go to school?")
        print("AI: Hogwarts!")
        user=input()
    elif user.lower()=="exit()":
        print("AI: Bye!")
        exit()
    elif user.lower()=="hi":
        print("AI: Hello! Nice to meet you!")
        # user=user.lower()
    elif user.lower()=="google search":
        print("What do you need me to search for?")
        query = input()

        for i in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(i)
        print("What else do you want me to do?")
        user = input()
    # elif user.lower()!= "knock knock" or "tell me a joke" or "exit()" or "hi" or "google search":
    else:
        print("AI: I don't understand you... Can you repeat your request?")
        user=input()


        # user=user.lower()
