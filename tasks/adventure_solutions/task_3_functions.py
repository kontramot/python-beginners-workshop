# Function to alert wrong input
def wrong_input(valid):
    print(f"Sorry but the only valid options are: {valid}.")

print()
name = input("What is your name? ")
print(f"Welcome to the dungeon, {name}!")

print("Do you go through door 1 or door 2?")

door = input("> ")

if door == "1":
    print("There is a nice vampire asking you if you enjoy life.")
    print("What do you do?")
    print("1. Smile and nod")
    print("2. Scream and run")

    vampire = input("> ")

    if vampire == "1":
        print(f"Congratulations {name}, you found a new friend!")
    elif vampire == "2":
        print(f"Sorry {name}, the vampire is faster. You become a dinner.")
    else:
        wrong_input("1, 2") # using function

elif door == "2":
    print("You found a room full of coffins.")
    print("What do you do?")
    print("1. Get through them to another door without touching anything.")
    print("2. Explore the room, open a coffin.")

    coffin = input("> ")

    if coffin == "1":
        print(f"Congratulations {name}, you're still alive!")
    elif coffin == "2":
        print("One of the vampires arrived and didn't like to see you messing"
              f" her bed. You're not going to see the light again, sorry {name}.")
    else:
        wrong_input("1, 2") # using function

else:
    wrong_input("1, 2") # using function

print()
bye = input("Say 'Good bye' in a language other than English: ")
print(f"{bye}, {name}!")
