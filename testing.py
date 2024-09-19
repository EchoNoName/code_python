game = True
moveNum = 0
player = 1
winner = 0
move = -1
ticTacToe = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
while game == True:
    for x in range(3):
        if ticTacToe[x] != " ":
            if ticTacToe[x] == ticTacToe[x+3] and ticTacToe[x+3] == ticTacToe[x+6]:
                game = False
                if ticTacToe[x] == "X":
                    winner = 1
                else:
                    winner = 2

    for x in range(0, 3, 3):
        if ticTacToe[x] != " ":
            if ticTacToe[x] == ticTacToe[x+1] and ticTacToe[x+1] == ticTacToe[x+2]:
                game = False
                if ticTacToe[x] == "X":
                    winner = 1
                else:
                    winner = 2

    x = 0
    if ticTacToe[x] != " ":
        if ticTacToe[x] == ticTacToe[x+4] and ticTacToe[x+4] == ticTacToe[x+8]:
            game = False
            if ticTacToe[x] == "X":
                winner = 1
            else:
                winner = 2

    x = 2
    if ticTacToe[x] != " ":
        if ticTacToe[x] == ticTacToe[x+2] and ticTacToe[x+2] == ticTacToe[x+4]:
            game = False
            if ticTacToe[x] == "X":
                winner = 1
            else:
                winner = 2
            
    print("=============")
    print(f"| {ticTacToe[0]} | {ticTacToe[1]} | {ticTacToe[2]} |")
    print("=============")
    print(f"| {ticTacToe[3]} | {ticTacToe[4]} | {ticTacToe[5]} |")
    print("=============")
    print(f"| {ticTacToe[6]} | {ticTacToe[7]} | {ticTacToe[8]} |")
    print("=============")

    if game == False or moveNum == 9:
        break

    try:
        if player == 1:
            move = int(input("Player 1, please enter your move (#): "))
        else:
            move = int(input("Player 2, please enter your move (#): "))
        if move < 1 or move > 9:
            print("Invalid Input")
            continue
    except:
        print("Invalid Input")
        continue
    
    if ticTacToe[move - 1] != "X" and ticTacToe[move - 1] != "O":
        moveNum += 1
        if player == 1:
            ticTacToe[move - 1] = "X"
            player = 2
        else:
            ticTacToe[move - 1] = "O"
            player = 1
    else:
        print("Space already taken")

if winner == 1:
    print("Player 1 wins!")
elif winner == 2:
    print("Player 2 wins!")
else:
    print("Draw!")