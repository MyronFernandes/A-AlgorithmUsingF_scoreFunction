import heapq
import copy
closed_set=[]
print("Start State=")
start_state =  [[int(x) for x in input(f"Enter the {i+1} row of the start matrix=  ").split(" ",3)] for i in range(3)]
print("Goal State=")
goal_state =[[int(x) for x in input(f"Enter the {i+1} row of the Goal matrix=  ").split(" ",3)] for i in range(3)]
def heuristic(state,gn):
    distance = 0
    for i in range(3):
        for j in range(3):
            if (state[i][j] != goal_state[i][j])and(state[i][j]!=0):
                 distance=distance+1
    return distance+gn
def h(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if (state[i][j] != goal_state[i][j])and(state[i][j]!=0):
                 distance=distance+1
    return distance
def astar(start_state):
    open_list = []
    closed_set.append((start_state,0,"Stable"))
    gn=0
    heapq.heapify(open_list)
    heapq.heappush(open_list, (heuristic(start_state,gn), (start_state,"Stable")))
    while open_list:
        current_cost, temp= heapq.heappop(open_list)
        current_state ,direct=temp
        gn=current_cost-h(current_state)
        closed_set.append((current_state,gn,direct))
        gn=gn+1
        for next_state,direction in generate_next_states(current_state,direct):
            print("current_cost F(n)=G(n)+h(n)=",heuristic(next_state,gn),",G(n)=",gn,"h(n)=",heuristic(next_state,gn)-gn,"          ",direction)
            for row in next_state:
                print(row)
            if next_state == goal_state:
                print("Goal State Found:")
                print("direction=  H(n):",heuristic(next_state,gn),",G(n)=",gn,",direction =",direction )
                for row in next_state:
                    print(row)
                return next_state,direction,gn  # Return goal state if found
            if tuple(map(tuple, next_state)) not in closed_set:
                heapq.heappush(open_list, (heuristic(next_state,gn),( next_state,direction)))
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
def previous_states_path(state,dir):
    zero_x, zero_y = find_zero_position(state)
    if dir == "Right":
        new_x, new_y = 0 + zero_x,  zero_y-1 
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            return new_state
    elif dir == "Left":
        new_x, new_y = 0 + zero_x, 1 + zero_y
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            return new_state
    elif dir == "Down":
        new_x, new_y =  zero_x-1 , 0 + zero_y
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            return new_state
    elif dir == "Up":
        new_x, new_y = 1 + zero_x, 0 + zero_y
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            new_state[zero_x][zero_y] = new_state[new_x][new_y]
            new_state[new_x][new_y] = 0
            return new_state
    return state
def find_zero_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
state,direction,gn=astar(start_state)
closed_set.append((state,gn,direction))
print("Reverse path from goal to intial node=")
print(f"GN({gn})for the following state are=")
for row in state:
    print(row)
while gn!=0:
    gn=gn-1
    state=previous_states_path(state,direction)
    tuple_to_search=(state,gn)
    for item in closed_set:
        if item[:2] == tuple_to_search:
            direction = item[2]
            break
    print(f"GN({gn})for the following state are=")
    for row in state:
        print(row)
