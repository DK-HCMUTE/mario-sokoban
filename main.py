from time import *
import os
from turtle import Screen, color
import pygame
import numpy as np
from BFS import *
from utilities import *
pygame.init()
maze = load_maze("1.txt")
goal_state = load_goal_state("1.txt")
SCREEN_SIZE = (600, 600)
SCREEN_MENU = (600,600)
SCREEN_LEVEL = (600,600)
WIDTH = SCREEN_SIZE[0]/len(maze[0])
HEIGHT = SCREEN_SIZE[0]/len(maze)

WIDTH_LEVEL = SCREEN_SIZE[0]/(2*len(maze[0]))
HEIGHT_LEVEL = SCREEN_SIZE[0]/(2*len(maze))



BUTTON = (270,50)
ARROW = (50,50)

max_level = 3


    

    
def render_level(map_level): 
    
    map_size = pygame.font.SysFont("sans",60)
    map_number = map_size.render("Lv." + str(map_level), True, white)
    map_rect = map_number.get_rect(center=(320, 120))
    screen_level.blit(map_number, map_rect)

def level_zone():

    map_level = 1
    running = True
   

    while running:
        scale_image(WIDTH_LEVEL,HEIGHT_LEVEL)
        global maze
        maze = load_maze(f'{map_level}.txt')
        global goal_state 
        goal_state = load_goal_state(f'{map_level}.txt')
        screen_level.blit(background_menu,(0,0))
        screen_level.blit(title_content, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        arrow_left_menu = screen_level.blit(arrow_left,(0,SCREEN_LEVEL[1]/2-ARROW[0]/2))
        arrow_right_menu= screen_level.blit(arrow_right,(SCREEN_LEVEL[0]-ARROW[0],SCREEN_LEVEL[1]/2-ARROW[0]/2))
        render_level(map_level)
        render_map(maze,screen_level,WIDTH_LEVEL,HEIGHT_LEVEL,SCREEN_SIZE[0]/4,SCREEN_SIZE[1]/4)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if arrow_left_menu.collidepoint(mouse_pos):
                        map_level-=1
                        if map_level == 0:
                            map_level = 1
                    if arrow_right_menu.collidepoint(mouse_pos):
                        map_level+=1
                        if map_level > max_level:
                            map_level = max_level
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_zone() 
                        
                    
        pygame.display.update()




   
def menu_zone():

   
    button_pos = SCREEN_MENU[0]/2-BUTTON[0]/2
    running = True
    while running:

        screen_menu.blit(background_menu,(0,0))
        start_button= screen_menu.blit(button_start,(button_pos,200))
        exit_button = screen_menu.blit(quit_button,(button_pos,280))
        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if start_button.collidepoint(mouse_pos):
                        level_zone()
                    if exit_button.collidepoint(mouse_pos):
                        running = False
        pygame.display.update()


    
def render_map(maze,screen,width,height,dx=0,dy=0):
    
     for i in range (len(maze)):
        for j in range (len(maze[i])):
            screen.blit (floor, (j*width+dx, i*height+dy))
            if maze[i][j] == "1":
                screen.blit (wall, (j*width+dx, i*height+dy))
            elif maze[i][j] == "0":
                screen.blit (floor, (j*width+dx, i*height+dy))
            elif maze[i][j] == "x":
                screen.blit (car, (j*width+dx, i*height+dy))
            elif maze[i][j] == "g":
                screen.blit (goal, (j*width+dx, i*height+dy))
            elif maze[i][j] == "*":
                screen.blit (box, (j*width+dx, i*height+dy))



def load_resource():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption ('SOKOBAN')
    icon = pygame.image.load ('./assets/icon.jpg')
    pygame.display.set_icon(icon)
    
    global floor
    floor = pygame.image.load ('./assets/background.png')
    
    global wall
    wall = pygame.image.load ('./assets/wall.png')
   

    global car
    car = pygame.image.load ('./assets/car.png')
    

    global box
    box = pygame.image.load ('./assets/box.png')
    

    global goal
    goal = pygame.image.load ('./assets/goal.png')
    

    global screen_level
    screen_level = pygame.display.set_mode(SCREEN_LEVEL)
    pygame.display.set_caption ('SELECT')

    global white
    white = (255,255,255)

    title_size = pygame.font.SysFont("sans",60)

    global title_content
    title_content = title_size.render('Mario SOKOBAN', True, white)

    global title_rect
    title_rect = title_content.get_rect(center=(320, 60))

    global arrow_left
    arrow_left =  pygame.image.load ('./assets/arrowLeft.jpg')
    arrow_left =  pygame.transform.scale(arrow_left, ARROW)

    global arrow_right
    arrow_right =  pygame.image.load ('./assets/arrowRight.jpg')
    arrow_right =  pygame.transform.scale(arrow_right, ARROW)

    global screen_menu
    screen_menu = pygame.display.set_mode(SCREEN_MENU)
    pygame.display.set_caption ('SOKOBAN')

    global background_menu 
    background_menu =  pygame.image.load ('./assets/loadMenu.png')
    background_menu = pygame.transform.scale(background_menu, SCREEN_MENU)

    global red 
    red = (235,51,36)

    global yellow 
    red = (235,51,36)

    global button_start 
    button_start =  pygame.image.load ('./assets/buttonStart.jpg')
    button_start =  pygame.transform.scale(button_start, BUTTON)

    global quit_button
    quit_button = pygame.image.load ('./assets/buttonQuit.jpg')
    quit_button =  pygame.transform.scale(quit_button, BUTTON)
    
def scale_image(width,height):

    global floor
    floor = pygame.transform.scale(floor, (width, height))
    global wall
    wall = pygame.transform.scale(wall,(width, height))
    global car
    car = pygame.transform.scale(car, (width, height))
    global box
    box = pygame.transform.scale(box, (width, height))
    global goal 
    goal = pygame.transform.scale(goal, (width, height))

def game_zone():
    scale_image(WIDTH,HEIGHT)
    clock = pygame.time.Clock()
    running = True
    problem = SokobanProblem(maze,goal_state)
    res = BFS(problem)
    k = res.solution()
    print(k)
    curr_state = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(2)
        board = k[curr_state]
        render_map(board,screen,WIDTH,HEIGHT)
        pygame.display.update()
        curr_state += 1
        # if curr_state > len(board):
        #     clock.tick(2)
        


if __name__ == '__main__':
    load_resource()
    
    # print(res.solution())
    game_zone()
    #menu_zone()
    



