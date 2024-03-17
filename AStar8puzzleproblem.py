import heapq
import copy
print("Goal State=")
goal_state =[[int(x) for x in input(f"Enter the {i+1} row of the Goal matrix=  ").split(" ",3)] for i in range(3)]
'''[[1,2,3],
             [8,0,4],
             [7,6,5]]'''
def heuristic(state,gn):
    distance = 0
    for i in range(3):
        for j in range(3):
            if (state[i][j] != goal_state[i][j])and(state[i][j]!=0):
                 distance=distance+1
    return distance+gn
def astar(start_state):
    open_list = []
    closed_set = set()
    gn=0
    heapq.heapify(open_list)
    heapq.heappush(open_list, (heuristic(start_state,gn), (start_state,"Stable")))
    while open_list:
        current_cost, temp= heapq.heappop(open_list)
        current_state ,direct=temp
        pre_dir=direct
        closed_set.add(tuple(map(tuple, current_state)))
        for next_state,direction in generate_next_states(current_state,pre_dir):
            print("current_cost F(n)=G(n)+h(n)=",heuristic(next_state,gn),",G(n)=",gn,"h(n)=",heuristic(next_state,gn)-gn,"          ",direction)
            for row in next_state:
                print(row)
            if next_state == goal_state:
                print("Goal State Found:")
                print("direction=  H(n):",",direction =",direction )
                for row in next_state:
                    print(row)
                return current_state  # Return goal state if found
            if tuple(map(tuple, next_state)) not in closed_set:
                heapq.heappush(open_list, (heuristic(next_state,gn),( next_state,direction)))
        gn=gn+1
def generate_next_states(state,pre_dir):
    next_states = []
    zero_x, zero_y = find_zero_position(state)
    dir_tuple=[(0, 1, "Right"), (0, -1, "Left"), (1, 0, "Down"), (-1, 0, "Up")]
    if pre_dir == "Right":
        dir_tuple = [tup for tup in dir_tuple if tup != (0, -1, "Left")]
    elif pre_dir == "Left":
        dir_tuple = [tup for tup in dir_tuple if tup != (0, 1, "Right")]
    elif pre_dir == "Down":
        dir_tuple = [tup for tup in dir_tuple if tup != (-1, 0, "Up")]
    elif pre_dir == "Up":
        dir_tuple = [tup for tup in dir_tuple if tup != (1, 0, "Down")]
    else:
        dir_tuple = [tup for tup in dir_tuple]
    for dx, dy, direction in dir_tuple:
        new_x, new_y = zero_x + dx, zero_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            next_states.append((new_state, direction))
    return next_states
def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
print("Start State=")
start_state =  [[int(x) for x in input(f"Enter the {i+1} row of the start matrix=  ").split(" ",3)] for i in range(3)]
'''
[[2,8,3],
                [1,6,4],
                [7,0,5]]#'''
astar(start_state)
