
b= [
 ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
 ['w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'c', 'c', 'c', 'w', 'c', 'w'],
 ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
 ['w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
 ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
]


a = [
        ['w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
        ['w', 'c', 'c', 'w', 'c', 'w', 'c', 'c', 'w', 'w', 'c', 'c', 'c', 'c','c', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'w', 'c', 'w', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w','c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c','c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'w', 'w', 'c', 'w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c','c', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'c', 'c', 'w'],
        ['w', 'c', 'w', 'c', 'w', 'w', 'w', 'w', 'c', 'c', 'w', 'c', 'w', 'w','w', 'c', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'c', 'w', 'w', 'c', 'c', 'c', 'w', 'c','w', 'w', 'w', 'w', 'w', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'w'],
        ['w', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'w', 'w', 'w', 'c', 'w', 'c','c', 'c', 'c', 'c', 'c', 'c', 'c', 'w', 'c', 'w', 'c', 'w', 'w'],
        ['w', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c','w', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'w', 'c', 'c', 'w'],
        ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w','w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'c', 'w']
    ]


from collections import deque
from queue import PriorityQueue

def bfs(start,goal,a):
    m=len(a)
    n=len(a[0])
    q = deque()
    q.append((start,[start]))
    visited = set()
    
    while len(q)>0:
       current,path = q.popleft()
       
       if(current[0]<0 or current[1]<0 or current[0]>=m or current[1]>=n or a[current[0]][current[1]] == 'w'):
            continue
          
       
       if(current in visited):
           continue
       
       if(current == goal):
           print("bfs path is: ")
           print(path)
           print("path length is: ",len(path))
           print("nodes traversed: ",len(visited))
           return
       
       
       q.append(((current[0]-1,current[1]),path + [(current[0]-1,current[1])]))
       q.append(((current[0]+1,current[1]),path + [(current[0]+1,current[1])]))
       q.append(((current[0],current[1]-1),path + [(current[0],current[1]-1)]))
       q.append(((current[0],current[1]+1),path + [(current[0],current[1]+1)]))
       
       visited.add(current)
    print("not found")


def a_star(start,goal,a):
    m=len(a)
    n=len(a[0])
    maximum = 99999
    heuristic  = [[ maximum for x in range(0,n)] for y in range (0,m)]
    for i in range(0,m):
        for j in range(0,n):
            if(a[i][j] == 'c'):
                heuristic[i][j] = (goal[0]-i) + (goal[1]-j)
    
    # for i in range(0,m):
    #     for j in range(0,n):
    #         print(heuristic[i][j]," ",end='')
    #     print("\n")
        
    pq = PriorityQueue()
    pq.put((heuristic[start[0]][start[1]],(start,[start])))
    visited = set()
    
    while pq.empty() == False:
       
       current,path = pq.get()[1]
       
       
       if(current[0]<0 or current[1]<0 or current[0]>=m or current[1]>=n or a[current[0]][current[1]] == 'w'):
            continue
        
       if(current in visited):
          
           continue
       
       if(current == goal):
           print("A* path is: ")
           print(path)
           print("path length is: ",len(path))
           print("nodes traversed: ",len(visited))
           return
       
       
      
       pq.put((1+heuristic[current[0]-1][current[1]],(((current[0]-1,current[1]),path + [(current[0]-1,current[1])]))))
       pq.put((1+heuristic[current[0]+1][current[1]],(((current[0]+1,current[1]),path + [(current[0]+1,current[1])]))))
       pq.put((1+heuristic[current[0]][current[1]-1],(((current[0],current[1]-1),path + [(current[0],current[1]-1)]))))
       pq.put((1+heuristic[current[0]][current[1]+1],(((current[0],current[1]+1),path + [(current[0],current[1]+1)]))))
       
       visited.add(current)
    

    print("not found")

bfs((1,1),(2,5),b)
print("\n")
a_star((1,1),(2,5),b)

print("\n\n")

bfs((0,1),(10,25),a)
print("\n")
a_star((0,1),(10,25),a)


       
       
       
    
    
    
