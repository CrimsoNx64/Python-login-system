#CrimsoN
#Login System

def login69():
    if user1=="login":
        num1=0#sets counter to 0 , ensures that you cant just put a random pass / username
        name1=input("\n"+"Enter your username: ")
        file=open(name1+"usernames.txt","r")#opens specified username txt file
        with open(name1+"usernames.txt") as openfile:
            f = open(name1+"usernames.txt", "r")
            searchlines = f.readlines()
            f.close()
            for i, line in enumerate(searchlines):#searches for the name in the file
                if name1 in line:
                    num1=num1+1#adds 1 to counter if its there 
                else:
                    num1=num1     
        password2=input("Enter your password: ")
        file=open(name1+"passwords.txt","r")
        with open(name1+"passwords.txt") as openfile:
            f = open(name1+"passwords.txt", "r")
            searchlines = f.readlines()
            f.close()
            for i, line in enumerate(searchlines):#searches for password
                if password2 in line:
                    num1=num1+1#adds 1 to counter if it is found
                else:
                    num1=num1
        if num1==2:#both conditions must be met for it to = 2
            print("Welcome")
            print("You are under the username:",name1)
        else:#if 1 or 0 are met will give you this
            print("That username and password did not match, try again")
    


def new69():
    username2=input("\n"+"Enter the username you would like: ")
    file=open(username2+"usernames.txt","w")#creates the new file
    file.close()
    file=open(username2+"usernames.txt","r")#noiw allows to be read from
    with open(username2+"usernames.txt") as file:
        contents=file.read()
        if username2 not in contents:#searches for name
            file.close()
            file=open(username2+"usernames.txt","a")
            file.write(username2)#adds name
            file.close()
            password1=input("Enter the password you would like: ")#idk why this works ill see######
            file=open(username2+"passwords.txt","a")
            file.write(password1)
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






