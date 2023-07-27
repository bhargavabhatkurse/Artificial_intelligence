from queue import PriorityQueue
import random

def Nqueen(N,initial):
	pq = PriorityQueue()
	m = set()
	pq.put((get_cost(initial),initial))		#initial state


	while pq.empty() == False:

		cost,current_state = pq.get()

		if tuple(current_state) in m:		#checking if already visited
			continue	

		if cost == 0:
			return current_state,cost

		for i in range(8):
			child = generate(current_state)
			pq.put((get_cost(child),child))



		m.add(tuple(initial))




def get_cost(state):
	#cost = no. of attacking queens
	#only consider diagonal attack as row and column attacks are guaranteed to be 0 as they are taken care of by keeping only 
	#one queen in each row and column 
	cost = 0
	for i in range(0,len(state)):
		for j in range(i+1,len(state)):
			if abs(state[i]-state[j]) == abs(i-j):
				cost += 1
	
	return cost

def generate(state):
	
	#swapping two random rows
	new_state = list(state)
	i,j = random.sample(range(0,len(state)),2)
	new_state[i],new_state[j] = new_state[j],new_state[i]

	return new_state



def main():
	N = 20

	initial = random.sample(range(1,N+1),N)
	

	solution,cost = Nqueen(N,initial)
	print(solution,"cost: ",cost)

	

	#printing board: 

	for i in range(len(solution)):
		for j in range(len(solution)):
			if (j,i) in [(r,s-1) for r,s in enumerate(solution)]:
				print("Q",end =" ")
			else:
				print(".", end = " ")
		print()





if __name__ == "__main__":
	main();