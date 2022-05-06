from turtle import Screen
import pygame
import numpy as np
from sympy import carmichael
from BFS import *
from utilities import *

maze = load_maze("1.txt")
goal_state = load_goal_state("1.txt")
SCREEN_SIZE = (600, 600)
WIDTH = SCREEN_SIZE[0]/len(maze[0])
HEIGHT = SCREEN_SIZE[0]/len(maze)



def load_game ():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption ('SOKOBAN')
    icon = pygame.image.load ('./assets/icon.jpg')
    pygame.display.set_icon(icon)
    
    global floor
    floor = pygame.image.load ('./assets/background.jpg')
    floor = pygame.transform.scale(floor, (WIDTH, HEIGHT))
    global wall
    wall = pygame.image.load ('./assets/wall.jpg')
    wall = pygame.transform.scale(wall,(WIDTH, HEIGHT))

    global car
    car = pygame.image.load ('./assets/car.jpg')
    car = pygame.transform.scale(car, (WIDTH, HEIGHT))

    global box
    box = pygame.image.load ('./assets/box.jpg')
    box = pygame.transform.scale(box, (WIDTH, HEIGHT))

    global goal
    goal = pygame.image.load ('./assets/goal.jpg')
    goal = pygame.transform.scale(goal, (WIDTH, HEIGHT))


def game_zone(problem):
    pygame.init()
    load_game()

    running = True
    res = BFS(problem)
    board = res.solution()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # screen.blit(background, (0, 0))
        pygame.display.update()
        for k in board:
            for i in range (len(k)):
                for j in range (len(k[i])):
                    if k[i][j] == "1":
                        screen.blit (wall, (j*WIDTH, i*HEIGHT))
                    elif k[i][j] == "0":
                        screen.blit (floor, (j*WIDTH, i*HEIGHT))
                    elif k[i][j] == "x":
                        screen.blit (car, (j*WIDTH, i*HEIGHT))
                    elif k[i][j] == "g":
                        screen.blit (goal, (j*WIDTH, i*HEIGHT))
                    elif k[i][j] == "*":
                        screen.blit (box, (j*WIDTH, i*HEIGHT))
        


if __name__ == '__main__':
    
    problem = SokobanProblem(maze,goal_state)
    # print(res.solution())

    game_zone(problem)
    



