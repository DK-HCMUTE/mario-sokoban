#import pygame
import numpy as np
from BFS import *
from utilities import *


# def game_zone():
#     running = True
#     while running:
#         pass

if __name__ == '__main__':
    maze = load_maze("1.txt")
    goal_state = load_goal_state("1.txt")
    problem = SokobanProblem(maze,goal_state)
    res = BFS(problem)
    print(res.solution())



