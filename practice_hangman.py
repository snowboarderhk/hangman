#hangman-game


def hangman(word):
    wrong = 0
    stages = ["",
              "__________",
              "|        |      ",
              "|        |      ",
              "|        O      ",
              "|       /||     ",
              "|       / |     ",
              "|               "]
    rletters = list(word)
    board =["_"]*len(word)
    win = False
    print("Welcome to Hangman!!")

    while wrong < len(stages) -1:
        print("¥n")
        char = input("say a charactor")
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] ="$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("¥n".join(stages[0:e]))
        if "_" not in board:
            print( "you are win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("¥n".join(stages[0:wrong+1]))
        print("you are lose!Correct answer is {}.".format(word))

#---p139---challenge 1 ---
import random

test = random.randint(0,3)
gamelist = ["cat","ANA","Burton","Starbucks"]
hangman(gamelist[test])
