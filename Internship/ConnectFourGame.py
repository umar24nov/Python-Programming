import random

def create_board():
    board = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(0)
        board.append(row)
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))
        
def drop_piece(board, column, player):
    for i in range(5, -1, -1):
        if board[i][column] == 0:
            board[i][column] = player
            return True
    return False
def check_win(board, player):
    # check horizontal win
    for i in range(6):
        for j in range(4):
            if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
                return True
            
    #check vertical win 
    for i in range(3):
        for j in range(7):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
                return True       
    
    # check diagonal win (downward sloping)
    for i in range(3):
        for j in range(4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    
    # check diagonal win (upward sloping)
    for i in range(3,6):
        for j in range(4):
            if board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
                return True
            
    return False

def check_draw(board):
    for row in board:
        if 0 in row:
            return False
    return True

def play_game():
    board = create_board()
    print_board(board)
    
    players = [1, 2]
    current_player = random.choice(players)
    
    while True:
        print(f"player {current_player}'s turn:")
        
        while True:
            column = int(input("Enter a column (1-7): ")) -1
            if 0 <= column < 7 and drop_piece(board, column, current_player):
                break
            else:
                print("Invalid column. Please try again.")
                
        print_board(board)
        
        if check_win(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        current_player = 3 - current_player
        
if __name__ == "__main__":
    play_game()
            
            