board = ["", "", "_", "", "", "_", "", "", "_"]
currentPlayer = "X"
winner = "NONE"
gameRunning = True

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if inp >= 1 and inp <= 9 and board[inp - 1] == "_":
                return inp - 1
            else:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True
    return False

def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True
    return False

def checkWin():
    global gameRunning
    if checkHorizontal(board) or checkVertical(board) or checkDiagonal(board):
        printBoard(board)
        print(f"Player {winner} wins!")
        gameRunning = False

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

while gameRunning:
    printBoard(board)
    move = playerInput(board)
    board[move] = currentPlayer
    checkWin()
    switchPlayer()

