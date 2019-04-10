from groupy.client import Client
import json

def main():
    input_token = input("token: ")
    client = Client.from_token(input_token)

    x = []
    i = 1
    print("Targets")
    print("0 - Quit")
    for chat in client.chats.list():
        print(str(i) + ' - ', end="")
        print( chat.other_user['name'])
        x.append(chat)
        i+=1

    message = "fck"
    i = 1
    while(True):
        '''
        input_target = input("target: ")

        if input_target == '0':
            break
        
        input_message = input("message: ")
        '''
        #x[int(input_target)-1].post(text = input_message)
        x[int(2)-1].post(text = "Yo where you at?")
        print("message sent to: ", end="")
        print(x[1])
        print("#: ")
        print(i)
        i+=1
        '''
        message +="k"
        '''




if __name__ == "__main__":
    main()