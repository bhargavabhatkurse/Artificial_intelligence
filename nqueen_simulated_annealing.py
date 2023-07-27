import random
import math
from operator import itemgetter

def simulated_annealing(initial_state):
    visited = set()
    initial_temp = 10
    final_temp = 0.1
    alpha = 0.01 #decay
    
    current_temp = initial_temp
    current_state = initial_state
    
    best_cost = get_cost(initial_state)
    best_state = current_state

    visited.add(tuple(current_state))

    while current_temp > final_temp:
        neighbor = min(get_neighbor(current_state), key = itemgetter(0))[1]
        if tuple(neighbor) not in visited:
            visited.add(tuple(neighbor))
        print(neighbor)
        print()

        
        cost_diff = get_cost(current_state) - get_cost(neighbor)

        # if the new solution is better, accept it
        if cost_diff > 0 or random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
            current_state = neighbor
       
        #Check if neighbor is best so far
        if get_cost(current_state) < best_cost:
            best_state = list(current_state)
            best_cost = get_cost(current_state)

        # decrement the temperature
        current_temp -= alpha

    return best_state

def get_cost(state):
    n = len(state)
    attacks = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(state[i] - state[j]) == abs(i - j): #same diagonal || row and column conflicts are ensured not to occur
                attacks += 1
   
    return attacks



def get_neighbor(state):
   new_states = []
   while len(new_states) != len(state):
    new_state = list(state)
    i,j,k,l = random.sample(range(len(state)), 4)
    #swapping 4 random queens
    #to get diverse solutions
    new_state[i],new_state[j] = new_state[j],new_state[i]
    new_state[k],new_state[l] = new_state[l],new_state[k]
   

    cost = get_cost(new_state)
    if(new_state not in new_states):  #to not include same/repeated neighbours 
        new_states.append((cost,new_state))

    
   

   return new_states


n=25
# initial = random.sample(range(1, n+1), n)
# solution = simulated_annealing(initial)

while True:
    initial = random.sample(range(1, n+1), n)
    solution = simulated_annealing(initial)
    if(get_cost(solution) == 0):
        break


print("soln:\n",solution,"\nconflicts: ",get_cost(solution))

print()

#Plot the chessboard with queens
for i in range(len(solution)):
    for j in range(len(solution)):
        if (j,i) in [(r,s-1) for r,s in enumerate(solution)]:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()

# [6, 9, 14, 1, 5, 8, 13, 16, 12, 2, 7, 10, 3, 15, 4, 11] 
# conflicts:  0

# . . . Q . . . . . . . . . . . . 
# . . . . . . . . . Q . . . . . . 
# . . . . . . . . . . . . Q . . . 
# . . . . . . . . . . . . . . Q . 
# . . . . Q . . . . . . . . . . . 
# Q . . . . . . . . . . . . . . . 
# . . . . . . . . . . Q . . . . . 
# . . . . . Q . . . . . . . . . . 
# . Q . . . . . . . . . . . . . . 
# . . . . . . . . . . . Q . . . . 
# . . . . . . . . . . . . . . . Q 
# . . . . . . . . Q . . . . . . . 
# . . . . . . Q . . . . . . . . . 
# . . Q . . . . . . . . . . . . . 
# . . . . . . . . . . . . . Q . . 
# . . . . . . . Q . . . . . . . . 

