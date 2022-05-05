import numpy as np

def load_maze(path):
    array_from_file = np.loadtxt("./problem/"+path, dtype=str)
    return array_from_file

def load_goal_state(path):
    array_from_file = np.loadtxt("./goal_state/"+path, dtype=str)
    return array_from_file

def get_position(state):
    list_position=list([])
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j]=='*':
                list_position.append([str(i),str(j)])
    return list_position
