while True:
    p = input("what is your word?: ")
    p = p.lower()
    numbers = {"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0,"0":0}
    for i in p:
        if i in numbers:
            numbers[i] += 1
    panagram = True
    for i in numbers.values():
        if i == 0:
            panagram = False
    if panagram == True:
        print("Yay its a panagram")
    else:
        print("nope its not a panagram")
