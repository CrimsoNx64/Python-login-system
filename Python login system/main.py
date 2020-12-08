#Dan
#Login System

def login69():
    if user1=="login":
        num1=0
        file=open("usernames.txt","r")
        name1=input("\n"+"Enter your username: ")
        with open("usernames.txt") as openfile:

            for line in openfile:
                for part in line.split():
                    if name1 in part:
                        num1=num1+1
                        file.close()
        file=open("passwords.txt","r")
        password2=input("Enter your password: ")
        with open("passwords.txt") as openfile:
            for line in openfile:
                for part in line.split():
                    if password2 in part:
                        num1=num1+1
                        file.close()
        if num1==2:
            print("Welcome")
            print("You are under the username:",name1)
        else:
            print("That username and password did not match, try again")
    

def new69():
    file=open("usernames.txt","r")
    username2=input("\n"+"Enter the username you would like: ")
    with open("usernames.txt") as file:
        contents=file.read()
        if username2 not in contents:
            file.close()
            file=open("usernames.txt","a")
            file.write("\n"+username2)
            file.close()
            file=open("passwords.txt","a")
            password1=input("Enter the password you would like: ")
            file.write("\n"+password1)
            file.close()
        else:
            print("Username already in use")
    return user1
    return new69
        


while True:
    user1=input("\n"+"Would you like to login or create a new account? Please answer with either `login` or `new`: ").lower()
    if user1=="new":
        new69()
    elif user1=="login":
        login69()
    else:
        print("That was not `new` or `login`, try again")






