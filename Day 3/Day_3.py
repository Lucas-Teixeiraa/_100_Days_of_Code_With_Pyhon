print(r"""
                   .--------------------------------...
               ,'-------------------------------,'   |
              /                                /     |
             /________________________________/    ,'|
             |               ..               |  ,'  |
             |___________-==/88\==-___________|,' /) |.
             |  \    \     ((  ))     /    /  |  (/  |-. .
             |   \    \     \{}/     /    /   |    .' .  .
          . '|    \    \     )(     / _  /    |    ,   .  .
         . . |\    \    \    \/    _.( ~-.   /|\ ,' .   . .
       ` .  -`_-.--.______..._____( ,/  ` \~-.|,' .   .
        .  `    .     .       .  ,'\. ~-  . , .  .  .   .
           .  `   .     ,   .      , ~~-.' .  .    .

""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
moveSet = input("You're at a cross road. Where do you want to go? type 'left' of 'right'\n")
gameOver = False
cont = 0
while not gameOver:
    if moveSet == "right":
        print("Fall in to hole! =(")
        gameOver = True
    else:
        moveSet = input("Swin or Wait?\n")
        if moveSet == "swin":
            print("Attacked by trout")
            gameOver = True
        else:
            moveSet = input("Which door? Blue, Red or Yellow\n")
            if moveSet == "yellow":
                print("YOU WIN!!!!!")
                gameOver = True
            if moveSet == "red":
                print("Burned by fire. Game Over.")
                gameOver = True
            if moveSet == "blue":
                gameOver = 1
                print("Eaten by beasts.Game Over.")


