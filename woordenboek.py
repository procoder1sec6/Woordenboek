capitals = {"Netherlands":"Amsterdam","UK":"London"}
print(capitals)
capitals["Dogland"] = "Beagle"
print(capitals)
print(capitals["Dogland"])
i = input("What country are you looking for?")
if i in capitals:
    print("yes")
else:
    print("no")