verysecretinfo = {"beagle":"Dogsarethebest","potato":"fries","username":"incorrect"}
u = input("Enter username: ")
if u in verysecretinfo:
    p = input("what is your password: ")
    if p == verysecretinfo[u] :
        print("you are now logged in as "+u)
    else:
        print("your password is incorrect")
        p = input("what is your password: ")
        if p == verysecretinfo[u] :
            print("you are now logged in as "+u)
        else:
            print("your hacked make a new account")

else:
    print("incorrect username")