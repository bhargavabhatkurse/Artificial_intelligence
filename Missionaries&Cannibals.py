from collections import deque

def M_C(missionary,cannibal,boat_size):

	q = deque()
	m = set()

	q.append(((3,3,0),[[3,3,0]]))  		#initial node

	while len(q) > 0:
		u,path = q.pop()				#DFS 

		if u in m:						#checking if already visited
			continue

		if u[0]<0 or u[1]<0 or u[0]>missionary or u[1]>cannibal: 		#checking if it meets the constraints 
			continue

		if(u[0] < u[1] and u[0]>0):			#checking if the no. of missionaries is less than cannibals on the original riverbank
			continue;

		if(u[0] > u[1] and u[0] < missionary):	#checking if the no. of missionaries is less than cannibals on the other riverbank
			continue;

		if u == (0,0,1):
			print(path);
			return

		m.add(u);			#marking as visited

		#if on the original bank,
		if(u[2] == 0):
			for i in range(0,boat_size+1):
				for j in range(0,boat_size+1):
					if i + j <= boat_size and i+j>0:
						q.append(((u[0]-i,u[1]-j,1),path + [[u[0]-i,u[1]-j,1]]))


		#if on the other bank,
		if(u[2] == 1):
			for i in range(0,boat_size+1):
				for j in range(0,boat_size+1):
					if i + j <= boat_size and i+j>0:
						q.append(((u[0]+i,u[1]+j,0),path + [[u[0]+i,u[1]+j,0]]))


	

def main():
	m,c,boat_size = 3,3,2
	M_C(m,c,boat_size)


if __name__ == "__main__":
	main();

