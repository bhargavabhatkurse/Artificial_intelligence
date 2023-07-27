from queue import PriorityQueue

player = 'x'
bot = 'o'

board = 		{1:' ',2:' ',3:' ',
				 4:' ',5:' ',6:' ',
				 7:' ',8:' ',9:' '}

def printboard(board):
	print(board[1], '|', board[2], '|', board[3])
	print('----------')
	print(board[4], '|', board[5], '|', board[6])
	print('----------')
	print(board[7], '|', board[8], '|', board[9])
	print("\n\n")

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


def checkDraw(board):
	for key in board.keys():
		if board[key] == ' ':
			return False

	return True

def isFree(position):
		if board[position] == ' ':
			return True

		return False

def insert(letter,position):
	if isFree(position):
		board[position] = letter
		printboard(board)

	if evaluate(board):
		if letter == 'x':
			print("bot wins")
			exit(1)
		else:
			print("player wins")
			exit(1)

	if checkDraw(board):
		print("draw")

def playermove(player):
	position = int(input("player position: "))
	insert(player,position)

def computermove(bot):
	best_score = float('-inf')
	best_move = 0

	for key in board.keys():
		if board[key] == ' ':
			board[key] = bot;
			score = minimax(board,0,True)
			board[key] = ' ';

			if score < best_score:
				best_score = score
				best_move = key

	insert(bot,best_move)


def minimax(board,depth,ismaximising):
	if evaluate(board):
		if ismaximising:
			return 1
		else:
			return -1

	if checkDraw(board):
		return 0

	if ismaximising:
		best_score = float('-inf')

		for key in board.keys():
			if board[key] == ' ':
				board[key] = bot;
				score = minimax(board,0,False)
				board[key] = ' ';

				best_score = max(best_score,score)
		return best_score
		

	else:
		best_score = float('inf')

		for key in board.keys():
			if board[key] == ' ':
				board[key] = bot;
				score = minimax(board,0,True)
				board[key] = ' ';

				best_score = min(best_score,score)
		return best_score

	

def main():
	while evaluate(board) == False and checkDraw(board) == False:
		playermove(player)
		computermove(bot)


if __name__ == "__main__":
	main();