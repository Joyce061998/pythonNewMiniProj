"""
Pseudocode
1. The user see the welcome title
2. each guess has 5 limit, if the player is not guessing the right game plus 1 bet and it will limit the play up to 5
3. The game will ask if you wanna play or not if yes (the player will bet upto 5 limit), if no it will terminate the game



"""
print(" 😆 ❤ Welcome to Guessing Number Game ❤ 😆")
print("               🥰🥰🥰                                ")

player = input("Do you wanna play: Y/N: ")
if player.upper() == "Y" or player.lower() == "y":
    secret_number = 9
    i = 0
    while i < 5:
        guess = int(input("Guess Number From 1-100: "))
        i += 1
        if guess ==secret_number:
            print("You Win! 🥳 🥳")
            break
        else:
            print("Next 😉")
elif player.lower() == "n" or player.upper() == "N":
    print(" 🫡 Play Next Time! 🫡")
else:
    print("I dont understand")

