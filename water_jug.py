from collections import deque

def waterjug(a,b,target):

	q = deque()
	m = set()					#keeping track of visited nodes

	q.append(((0,0),[[0,0]]))		#initial node

	while len(q) > 0:
		u,path = q.popleft()		#BFS

		if (u[0],u[1]) in m:		#checking if already visited
			continue

		if u[0]<0 or u[1]<0 or u[0]>a or u[1]>b:		#checking if it meets the constraints
			continue

		if u[0] == target or u[1] == target:			#checking if it is the target
			print(path);
			return

		m.add((u[0],u[1]));			#marking as visited

		#6 cases to generate children:

		#completely filling one of the jug
		q.append(((a,u[1]),path + [[a,u[1]]]))
		q.append(((u[0],b),path + [[u[0],b]]))
		

		#transfering from one jug to another
		a_to_b = min(u[0],b-u[1])
		b_to_a = min(a-u[0],u[1])

		q.append(((u[0]-a_to_b,u[1]+a_to_b),path + [[u[0]-a_to_b,u[1]+a_to_b]]))
		q.append(((u[0]+b_to_a,u[1]-b_to_a),path + [[u[0]+b_to_a,u[1]-b_to_a]]))


		#emptying one of the jug
		q.append(((0,u[1]),path + [[0,u[1]]]))
		q.append(((u[0],0),path + [[u[0],0]]))

	

def main():
	a,b,target = 5,3,2
	waterjug(a,b,target)


if __name__ == "__main__":
	main();

