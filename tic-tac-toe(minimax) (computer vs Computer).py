board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def printBoard(board):
    print(board[1], '|', board[2], '|', board[3])
    print('----------')
    print(board[4], '|', board[5], '|', board[6])
    print('----------')
    print(board[7], '|', board[8], '|', board[9])
    print("\n\n")


def checkDraw(board):
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def spaceIsFree(position):
        if board[position] == ' ':
            return True
        
        return False


def evaluate(board):
    if (board[1] == board[2] == board[3] and board[1] != ' ') or \
       (board[4] == board[5] == board[6] and board[4] != ' ') or \
       (board[7] == board[8] == board[9] and board[7] != ' ') or \
       (board[1] == board[4] == board[7] and board[1] != ' ') or \
       (board[2] == board[5] == board[8] and board[2] != ' ') or \
       (board[3] == board[6] == board[9] and board[3] != ' ') or \
       (board[1] == board[5] == board[9] and board[1] != ' ') or \
       (board[7] == board[5] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def insert(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)

    if evaluate(board):
        if letter == 'x':
            print("computer1 wins!")
            exit()
        else:
            print("computer2 wins!")
            exit()

    if checkDraw(board):
        print("draw!")
        exit()


def computer1Move(bot):
    best_score = float('-inf')
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '

            if score > best_score:
                best_score = score
                best_move = key

    insert(bot, best_move)

def computer2Move(bot):
    best_score = float('inf')
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, True)
            board[key] = ' '

            if score < best_score:
                best_score = score
                best_move = key

    insert(bot, best_move)

def minimax(board, depth, isMaximizing):
    if evaluate(board):
        if isMaximizing:
            return -1
        else:
            return 1
    
    elif checkDraw(board):
        return 0

    if isMaximizing:
        best_score = float('-inf')

        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer1
                score = minimax(board, depth + 1, False)
                board[key] = ' '

                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float('inf')

        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer2
                score = minimax(board, depth + 1, True)
                board[key] = ' '

                best_score = min(best_score, score)

        return best_score


computer1 = 'x'
computer2 = 'o'


while not evaluate(board) and not checkDraw(board):
   
    computer1Move(computer1)
    computer2Move(computer2)
    
   
        

   
