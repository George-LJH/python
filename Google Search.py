from googlesearch import search
print("What do you need me to search for?")
query = input()

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)