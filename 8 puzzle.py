# 8 puzzle using Best first search

from queue import PriorityQueue

class node:
	def __init__(self,state,parent,action,h):
		self.state = state
		self.parent = parent
		self.action = action
		self.h = h

	def __lt__(self,other):
		return self.h<other.h

def heuristic(state,goal):
	#heuristic: no. of wrong tiles 
	cost = 0
	for i in range(9):
		if state[i] != goal[i] and state[i] != 0:
			cost += 1

	return cost

def path(node):
	path = []
	while node != None:
		path.append(node.state)
		node = node.parent

	path.reverse()

	for state in path:
		print(state[0:3])
		print(state[3:6])
		print(state[6:])
		print()


def puzzle(initial,goal):
	m = set()
	pq = PriorityQueue()

	initial = node(initial,None,None,heuristic(initial,goal))
	pq.put(initial)

	while pq.empty() == False:

		current_node = pq.get()
		current_state = current_node.state
		

		if tuple(current_state) in m:
			continue

		if current_state == goal:
			print("found: ")
			path(current_node)
			return 

		moves = possible_moves(current_state)

		for move in moves:
			child = apply_move(current_state,move)
			child_node = node(child,current_node,move,heuristic(child,goal))
			pq.put(child_node)

		m.add(tuple(current_state))




def apply_move(state,move):
	
	#applying the move to the current state and generating a new state. The new state is returned 
	new_state = list(state)

	i = state.index(0)

	if move == "UP":
		new_state[i-3],new_state[i] = new_state[i],new_state[i-3]
	if move == "DOWN":
		new_state[i+3],new_state[i] = new_state[i],new_state[i+3]
	if move == "LEFT":
		new_state[i-1],new_state[i] = new_state[i],new_state[i-1]
	if move == "RIGHT":
		new_state[i+1],new_state[i] = new_state[i],new_state[i+1]

	return new_state



def possible_moves(state):
	#finding the possible moves for a given state

	i = state.index(0)
	moves = []
	cx = i//3			#x coordinate
	cy = i%3			#y coordinate

	if cx - 1 >= 0:
		moves.append("UP")
	if cx + 1 < 3:
		moves.append("DOWN")
	if cy + 1 < 3:
		moves.append("RIGHT")
	if cy - 1 >= 0:
		moves.append("LEFT")

	return moves




def main():
	
	initial = [0,1,3,
			   4,2,6,
			   7,5,8,]

	goal =    [1,2,3,
			   4,5,6,
			   7,8,0,]

	puzzle(initial,goal)
	


if __name__ == "__main__":
	main();