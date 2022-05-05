#import pygame
import numpy as np
from BFS import BFS, SokobanProblem
from utilities import get_position, load_maze,load_goal_state

# def game_zone():
#     running = True
#     while running:
#         pass

def goal_test(state,goal):
        count = 0
        list_position = get_position(state)
        for i in list_position:
            if i in goal:
                count +=1
        if count == len(goal):
            return True
        return False

if __name__ == '__main__':
    maze = load_maze("1.txt")
    goal_state = load_goal_state("1.txt")
    problem = SokobanProblem(maze,goal_state)
    print(goal_test(maze,goal_state.tolist()))
    #print()



