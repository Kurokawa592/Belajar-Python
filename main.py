print("Hello , welcome to Coffee Shop")

name = input("Whats is your name? ")

if name == "Ben" or name == "Patricia" or name == "Lokey":
    evil_status = input("Are you evil?\n")
    goog_deeds = int(input("How many good deeds have you done today? \n"))
    if evil_status == "Yes" and goog_deeds < 4:
        print(("You're not welcome here Evil ") + name + ("!! Get out!!"))
        exit()
    else:
        print("Oh, se you're one of those good Bens. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today \n")