import random
game = True
moveNum = 0
winner = 0
move = -1
turn = 1
winningMove = -1
ticTacToeDisplay = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ticTacToe = [" ", " ", " ", " ", " ", " ", " " , " ", " "]
player = ""
while game:
    player = input("Would you like to be player 1 or 2 (type 1 or 2): ")
    if player == "1" or player == "2":
        player = int(player)
        break
    else:
        print("Invalid Input")

while game == True:
    for x in range(3):
        if ticTacToe[x] != " ":
            if ticTacToe[x] == ticTacToe[x+3] and ticTacToe[x+3] == ticTacToe[x+6]:
                game = False
                if ticTacToe[x] == "X":
                    winner = 1
                else:
                    winner = 2

    for x in range(0, 8, 3):
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
            
    for i in range(9):
        if ticTacToe[i] == "X" or ticTacToe[i] == "O":
            ticTacToeDisplay[i] = ticTacToe[i]

    print("=============")
    print(f"| {ticTacToeDisplay[0]} | {ticTacToeDisplay[1]} | {ticTacToeDisplay[2]} |")
    print("=============")
    print(f"| {ticTacToeDisplay[3]} | {ticTacToeDisplay[4]} | {ticTacToeDisplay[5]} |")
    print("=============")
    print(f"| {ticTacToeDisplay[6]} | {ticTacToeDisplay[7]} | {ticTacToeDisplay[8]} |")
    print("=============")

    if game == False or moveNum == 9:
        break

    if turn == player:
        try:
            move = int(input("Player, please enter your move (#): "))
            if move < 1 or move > 9:
                print("Invalid Input")
                continue
        except:
            print("Invalid Input")
            continue

        moveMade = False
    
        if ticTacToe[move - 1] != "X" and ticTacToe[move - 1] != "O":
            moveNum += 1
            if int(player) == 1:
                ticTacToe[move - 1] = "X"
                turn = 2
            else:
                ticTacToe[move - 1] = "O"
                turn = 1
        else:
            print("Space already taken")
    else:
        if player == 2:
            turn = 2
            if moveNum == 0:
                ticTacToe[0] = "X"
                moveNum += 1
            elif moveNum == 2:
                if ticTacToe[2] == "O" or ticTacToe[6] == "O":
                    ticTacToe[8] = "X"
                    if ticTacToe[2] == "O":
                        winningMove = 6
                    else:
                        winningMove = 2
                elif ticTacToe[1] == "O" or ticTacToe[7] == "O" or ticTacToe[8] == "O":
                    ticTacToe[6] = "X"
                    if ticTacToe[8] == "O":
                        winningMove = 2
                    else:
                        winningMove = 4
                elif ticTacToe[4] == "O":
                    ticTacToe[8] = "X"
                else:
                    ticTacToe[2] = "O"
                    winningMove = 4
                moveNum += 1
            else:
                moveNum += 1
                for i in range(3):
                    check = (ticTacToe[i], ticTacToe[i + 3], ticTacToe[i + 6])
                    if check.count("X") == 2 and check.count(" ") == 1:
                        ticTacToe[i + (check.index(" ") * 3)] = "X"
                        moveMade = True
                
                if moveMade == True:
                    continue

                for i in range (0, 8, 3):
                    check = (ticTacToe[i], ticTacToe[i + 1], ticTacToe[i + 2])
                    if check.count("X") == 2 and check.count(" ") == 1:
                        ticTacToe[i + check.index(" ")] = "X"
                        moveMade = True
                    
                if moveMade == True:
                    continue

                check = (ticTacToe[0], ticTacToe[4], ticTacToe[8])
                if check.count("X") == 2 and check.count(" ") == 1:
                    ticTacToe[i + (check.index(" ") * 3)] = "X"
                    moveMade = True

                if moveMade == True:
                    continue

                check = (ticTacToe[2], ticTacToe[4], ticTacToe[6])
                if check.count("X") == 2 and check.count(" ") == 1:
                    ticTacToe[i + (check.index(" ") * 3)] = "X"
                    moveMade = True

                if moveMade == True:
                    continue

                if winningMove != -1:
                    ticTacToe[winningMove] = "X"
                    winningMove = -1
                    continue
                else:
                    for i in range(3):
                        check = (ticTacToe[i], ticTacToe[i + 3], ticTacToe[i + 6])
                        if check.count("O") == 2 and check.count(" ") == 1:
                            ticTacToe[i + (check.index(" ") * 3)] = "X"
                            moveMade = True

                    if moveMade == True:
                        continue

                    for i in range (0, 8, 3):
                        check = (ticTacToe[i], ticTacToe[i + 1], ticTacToe[i + 2])
                        if check.count("O") == 2 and check.count(" ") == 1:
                            ticTacToe[i + check.index(" ")] = "X"
                            moveMade = True

                    if moveMade == True:
                        continue

                    check = (ticTacToe[0], ticTacToe[4], ticTacToe[8])
                    if check.count("O") == 2 and check.count(" ") == 1:
                        ticTacToe[0 + (check.index(" ") * 4)] = "X"
                        moveMade = True

                    if moveMade == True:
                        continue

                    check = (ticTacToe[2], ticTacToe[4], ticTacToe[6])
                    if check.count("O") == 2 and check.count(" ") == 1:
                        ticTacToe[2 + (check.index(" ") * 2)] = "X"
                        moveMade = True

                    if moveMade == True:
                        continue
                    
                    while True:
                        make = random.randint(0, 8)
                        if ticTacToe[make] != "X" and ticTacToe[make] != "O":
                            ticTacToe[make] == "X"
                            break
        else:
            if player == 1:
                turn = 1

                for i in range(3):
                    check = (ticTacToe[i], ticTacToe[i + 3], ticTacToe[i + 6])
                    if check.count("O") == 2 and check.count(" ") == 1:
                        ticTacToe[i + (check.index(" ") * 3)] = "O"
                        moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                for i in range (0, 8, 3):
                    check = (ticTacToe[i], ticTacToe[i + 1], ticTacToe[i + 2])
                    if check.count("O") == 2 and check.count(" ") == 1:
                        ticTacToe[i + check.index(" ")] = "O"
                        moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                check = (ticTacToe[0], ticTacToe[4], ticTacToe[8])
                if check.count("O") == 2 and check.count(" ") == 1:
                    ticTacToe[i + (check.index(" ") * 3)] = "O"
                    moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                check = (ticTacToe[2], ticTacToe[4], ticTacToe[6])
                if check.count("O") == 2 and check.count(" ") == 1:
                    ticTacToe[i + (check.index(" ") * 3)] = "O"
                    moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                for i in range(3):
                    check = (ticTacToe[i], ticTacToe[i + 3], ticTacToe[i + 6])
                    if check.count("X") == 2 and check.count(" ") == 1:
                        ticTacToe[i + (check.index(" ") * 3)] = "O"
                        moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                for i in range (0, 8, 3):
                    check = (ticTacToe[i], ticTacToe[i + 1], ticTacToe[i + 2])
                    if check.count("X") == 2 and check.count(" ") == 1:                                 
                        ticTacToe[i + check.index(" ")] = "O"
                        moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                check = (ticTacToe[0], ticTacToe[4], ticTacToe[8])
                if check.count("X") == 2 and check.count(" ") == 1:
                    ticTacToe[0 + (check.index(" ") * 4)] = "O"
                    moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue

                check = (ticTacToe[2], ticTacToe[4], ticTacToe[6])
                if check.count("X") == 2 and check.count(" ") == 1:
                    ticTacToe[2 + (check.index(" ") * 2)] = "O"
                    moveMade = True

                if moveMade == True:
                    moveNum += 1
                    continue
            
                if moveNum == 1:
                    moveNum += 1
                    if ticTacToe[0] == "X" or ticTacToe[2] == "X" or ticTacToe[6] == "X" or ticTacToe[8] == "X":
                        corner = True
                        ticTacToe[4] = "O"
                        continue
                    elif ticTacToe[4] == "X":
                        ticTacToe[0] = "O"
                        middle = True
                        continue
                    else:
                        side = True
                        ticTacToe[4] = "O"
                elif moveNum == 3:
                    moveNum += 1
                    if middle == True:
                        if ticTacToe[8] == "X":
                            ticTacToe[6] = "O"
                            continue
                    elif corner == True:
                        if (ticTacToe[0] == "X" and ticTacToe[8] == "X") or (ticTacToe[0] == "X" and ticTacToe[8] == "X"):
                            ticTacToe[1] = "O"
                            continue
                        elif 



