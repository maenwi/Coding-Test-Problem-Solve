N = int(input())

chats = {}
gomgom = 0

for _ in range(N):
    user = input()

    if user == "ENTER":
        chats = {}
    
    else:
        try:
            chats[user] += 1

        except:
            chats[user] = 0
            gomgom += 1

print(gomgom)