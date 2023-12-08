print("Hello , welcome to Coffee Shop")

name = input("Whats is your name? ")

if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here Evil Ben!! Get out!!")
        exit()
    else:
        print("Oh, se you're one of those good Bens. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today \n")

# menu = "Black Coffee, Espresso, Latte, Cappucino"

# print(name + " what would you like from our menu today? Her is what we are serving. \n" + menu)

# um = input()

# price = 8

# quantity = int(input("How many coffee would you like\n"))

# total = price * quantity

# print("Thank you. Your total is: $" + str(total))

# print("Sounds good " + name + ", we'll have that " + um + " ready for you in a moment.")
