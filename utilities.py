import numpy as np

POS_PLAYER_MOVE = {"UP": [-1, 0], "DOWN": [1, 0], "LEFT": [0, -1], "RIGHT": [0, 1]}

def load_maze(path):
    a = np.loadtxt("./problem/"+path, dtype=str)
    return tuple(map(tuple, a))

def load_goal_state(path):
    a = np.loadtxt("./goal_state/"+path, dtype=str)
    if any(isinstance(t, np.ndarray) for t in a):
        return list(a)
    return [list(a)]

def get_box_position(state):
    list_position=list([])
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '*':
                list_position.append([str(i),str(j)])
    return list_position

def get_player_position(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'x':
                return [str(i),str(j)]
    return None

def is_over_bound_maze(maze, pos):
    if pos[0] >= len(maze) or pos[0] < 0 or pos[1] >= len(maze[1]) or pos[1] < 0:
            return True
    return False
def is_more_box_collision(maze, pos, action):
    next_pos = (pos[0] + POS_PLAYER_MOVE[action][0], pos[1] + POS_PLAYER_MOVE[action][1])
    if is_over_bound_maze(maze, next_pos):
        return True
    if maze[next_pos[0]][next_pos[1]] == '*' and maze[pos[0]][pos[1]] == '*':
        return True
    return False

def is_wall_collision(maze, pos):
    if maze[pos[0]][pos[1]] == '1':
        return True
    return False

def is_box_wall_collsion(maze, pos, action):
    next_pos = (pos[0] + POS_PLAYER_MOVE[action][0], pos[1] + POS_PLAYER_MOVE[action][1])
    if is_over_bound_maze(maze, next_pos):
        return True
    if maze[next_pos[0]][next_pos[1]] == '1' and maze[pos[0]][pos[1]] == '*':
        return True
    return False

def can_move(maze, pos, action):
    return not (is_over_bound_maze(maze, pos) or is_more_box_collision(maze, pos, action) or is_wall_collision(maze, pos) or is_box_wall_collsion(maze, pos, action))


