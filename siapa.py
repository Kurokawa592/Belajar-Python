print("Hello , welcome to Coffee Shop")

name = input("Whats is your name? ")

if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today \n")

menu = " Black Coffee \n Espresso \n Latte \n Cappucino \n"

order = print(name + " what would you like from our menu today? Her is what we are serving. \n" + menu)

um = input()

if um == "Black Coffee":
    price = 19
elif um == "Latte":
    price = 4
    wp = input("Do you want whipped cream? ")
    if wp == "Yes":
        price = 4 + 11
    else:
        price = 4
    
elif um == "Espresso":
    price = 6
elif um == "Cappucino":
    price = 12
    

quantity = int(input("How many coffee would you like\n"))

total = price * quantity

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have that " + um + " ready for you in a moment.")