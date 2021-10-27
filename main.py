from random import randint
from images import rock, paper, scissors

game_images = [rock, paper, scissors]
images_str = ["Rock","Paper","Scissors"] 
while True:
    user_choice = input('''Type
0 For Rock
1 For Paper
2 For Scissors
>>> ''')          
    bot_choice = randint(0,2)
    
    if user_choice == "0" or user_choice == "1" or user_choice == "2":
        user_choice = int(user_choice)
        print("You Chose "+images_str[user_choice]+game_images[user_choice])
        print("Computer Chose "+images_str[bot_choice]+game_images[bot_choice])
        if user_choice == bot_choice:
            print("It's A Draw 😑")
        elif user_choice == 0:
            if bot_choice == 2:
                print("You Win 😄")
            else:
                print("Computer Wins 😎")
        elif user_choice == 1:
            if bot_choice == 0:
                print("You Win 😄")
            else:
                print("Computer Wins 😎")
        else:
            if bot_choice == 1:
                print("You Win 😄")
            else:
                print("Computer Wins 😎")
        play_again = input('''Do You Want To Play Again?
Type
Y for Yes
No for No
>>> ''')
        if play_again.lower() == "y":
            print("Ok Play Again 🤗")
        elif play_again.lower() == "n":
            print("Ok Fine 😔")
            break
        else:
            print("Invalid")
            break
    else:
        print("Invalid")
        break
#Coded By MegaByte007
#Github: https://github.com/MegaByte007
