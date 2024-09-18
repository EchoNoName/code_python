game = True
player = 1
ticTacToe = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("=============")
print("| " + ticTacToe[0] + " | " + ticTacToe[1] + " | " + ticTacToe[2] + " |")
print("=============")
print("| " + ticTacToe[3] + " | " + ticTacToe[4] + " | " + ticTacToe[5] + " |")
print("=============")

print("| " + ticTacToe[6] + " | " + ticTacToe[7] + " | " + ticTacToe[8] + " |")
print("=============")
while game == False:
    if player == 1:
        print("Player 1, please enter your move (#)")
    else:
        print("Player 2, please enter your move (#)")
