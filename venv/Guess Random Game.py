"""
Pseudocode
1. The user see the welcome title
2. each guess has 5 limit, if the player is not guessing the right game plus 1 bet and it will limit the play up to 5
3. The game will ask if you wanna play or not if yes (the player will bet upto 5 limit), if no it will terminate the game

"""
welcome = """
          😆 ❤ Welcome to Guessing Number Game ❤ 😆
                            🥰🥰🥰 
    Instrution : You need to know the random number from 1-100. 
    You need to guess the number until you reach the 5 chances.
                        Good Luck!!!
"""
print(welcome)


player = input("Do you wanna play: Select Y/N: ")
if player.upper() == "Y" or player.lower() == "y":
    secret_number =  100
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
blntime = """        
        Better  Luck Next Time!!!
        You can Bet Again By Simple Run the Site
"""
print(blntime)

