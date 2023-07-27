from queue import PriorityQueue
x = float('inf')

class node:
	def __init__(self,state,parent,h):
		self.state = state
		self.parent = parent
		self.h = h

	def __lt__(self,other):
		return self.h < other.h


a= {
 "A":[0,6,x,x,x,3,x,x,x,x],
 "B":[6,0,3,2,x,x,x,x,x,x],
 "C":[x,3,0,1,5,x,x,x,x,x],
 "D":[x,2,1,0,8,x,x,x,x,x],
 "E":[x,x,5,8,0,x,x,x,5,5],
 "F":[3,x,x,x,x,0,1,7,x,x],
 "G":[x,x,x,x,x,1,0,x,3,x],
 "H":[x,x,x,x,x,7,x,0,2,x],
 "I":[x,x,x,x,5,x,3,2,0,3],
 "J":[x,x,x,x,5,x,x,x,3,0]
}

mapping = {
  0: "A",
  1: "B",
  2: "C",
  3: "D",
  4: "E",
  5: "F",
  6: "G",
  7: "H",
  8: "I",
  9: "J",
}

heuristic = {
  "A":10,
  "B":8,
  "C":5,
  "D":7,
  "E":3,
  "F":6,
  "G":5,
  "H":3,
  "I":1,
  "J":0,
}


def path(node): 
	path = []

	while node is not None:
		path.append(node.state)
		node = node.parent

	path.reverse()

	print(path)


def hill(start,end):
	pq = PriorityQueue()
	m = set()
	initial_node = node(start,None,heuristic[start])
	pq.put(initial_node)

	while pq.empty() == False:
		current_node = pq.get()
		current_state = current_node.state

		if current_state in m:
			continue

		while pq.empty() ==False:		#emptying the queue
			pq.get(False)

		if current_state ==end:
			print("solution found")
			path(current_node)
			return

		for i,weight in enumerate(a[current_state]):
			if(weight != 0 and weight != x):
				child = mapping[i]
				child_h = heuristic[child]
				child_node = node(child,current_node,child_h)

				if child_h < current_node.h:   #only if the child node is better than the current node, we append it to the open list
					pq.put(child_node)

				

		m.add(current_state)

def main():
	start = "A"
	end = "J"

	hill(start,end)


if __name__ == "__main__":
	main();