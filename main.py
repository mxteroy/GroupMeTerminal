from groupy.client import Client
import json

def getChats(client):    
    return client.chats.list()

def main():
    client = Client.from_token("mzDFlBv3e9JycnZ9LXynMVul2RWgPPWW8SXYa3bC")

    x = []
    i = 1
    for chat in client.chats.list():
        print(str(i) + ' - ', end="")
        print( chat.other_user['name'])
        x.append(chat)
        i+=1

    chats = getChats(client)

    while(True):
        input_target = input("who do you want to talk to?")
        input_message = input("message: ")
        
        message = x[int(input_target)-1].post(text = input_message)
        



if __name__ == "__main__":
    main()