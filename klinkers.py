while True:
    w = input("what is your word?: ")
    w = w.lower()
    klinkers = {"a":0,"e":0,"i":0,"o":0,"u":0}
    for i in w:
        if i in klinkers:
            klinkers[i] += 1
    print(klinkers)