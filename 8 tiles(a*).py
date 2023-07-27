# ref -> https://www.cs.princeton.edu/courses/archive/spr10/cos226/assignments/8puzzle.html#:~:text=The%208%2Dpuzzle%20problem%20is,that%20they%20are%20in%20order.
from queue import PriorityQueue

class Node:
    def __init__(self, state, parent=None, action=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.g = g  # Path cost
        self.h = h  # Heuristic value
        self.f = self.g + self.h

    def __lt__(self, other):
        return self.f < other.f
        

def heuristic(state,goal_state):
    cost = 0
    
    # heuristic 1: 
    # tiles in incorrect position --> not good
    # for i in range(9):
    #     if state[i] != goal_state[i] and state[i] != 0:
    #         cost += 1;


    # # heuristic 2: Manhattan distance 
    for i in range(9):
         if state[i] != 0:

           cx = i // 3
           cy = i % 3


           index = goal_state.index(state[i])
           gx = index // 3
           gy = index % 3
           

           cost += abs(gx - cx) + abs(gy - cy);


    return cost

def get_possible_moves(state):
    moves = []
    i = state.index(0)

    cx = i // 3         #x coordinate
    cy = i % 3          #y coordinate

    if cx - 1 >= 0:
        moves.append('Up')
    if cx + 1 < 3:
        moves.append('Down')
    if cy - 1 >= 0:
        moves.append('Left')
    if cy + 1 < 3:
        moves.append('Right')
    
    return moves


def apply_move(state, move):
    new_state = state[:] #copy of the current state
    i = new_state.index(0)

    #swap

    if move == 'Up':
        new_state[i], new_state[i - 3] = new_state[i - 3], new_state[i]
    elif move == 'Down':
        new_state[i], new_state[i + 3] = new_state[i + 3], new_state[i]
    elif move == 'Left':
        new_state[i], new_state[i - 1] = new_state[i - 1], new_state[i]
    elif move == 'Right':
        new_state[i], new_state[i + 1] = new_state[i + 1], new_state[i]
    return new_state

def print_solution(node,nodes_traversed):
    no_of_states = 0
    path = []
    print('Path:') 
    while node is not None:
        path.append(node.state)
        node = node.parent
    path.reverse()
    for state in path:
        print(state[0:3])
        print(state[3:6])
        print(state[6:])
        no_of_states += 1
        print()

    print('Goal state found\nThe number of moves: ', no_of_states)
    print('The number of states_traversed: ', nodes_traversed)





def solve_puzzle(initial_state,goal_state):
    open_list = PriorityQueue()
    closed_list = set()
    start_state = Node(initial_state, None, None, 0, heuristic(initial_state,goal_state))
    open_list.put(start_state)
    

    while open_list.empty() == False:

        current_node = open_list.get()
        current_state = current_node.state
        

        if current_state == goal_state:

            print_solution(current_node,len(closed_list))
            return

        closed_list.add(tuple(current_state))

        moves = get_possible_moves(current_state)
        # print(moves)
        for move in moves:
            next_state = apply_move(current_state, move)
            if tuple(next_state) not in closed_list:
                g = current_node.g + 1
                h = heuristic(next_state,goal_state)
                next_node = Node(next_state, current_node, move, g, h)
                open_list.put(next_node)

    print('No solution found.')

# Example usage:
# initial_state = [1, 2, 3,
#                  4, 0, 6, 
#                  7, 5, 8]

initial_state = [1, 2, 3,
                 5, 6, 0,
                 7, 8, 4] 


goal_state = [1, 2, 3,
              4, 5, 6, 
              7, 8, 0]

solve_puzzle(initial_state,goal_state)
