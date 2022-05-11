from ctypes.wintypes import SIZE
from time import *
import os
from turtle import Screen, color
import black
from matplotlib.pyplot import show
import pygame
import numpy as np
from sympy import false
from BFS import *
from utilities import *
from tkinter import *
from tkinter import messagebox

pygame.init()

SCREEN_SIZE = (600,600)
SCREEN_MENU = (600,600)
SCREEN_LEVEL = (600,600)
TITLE_STATE = "Loading"
clock = pygame.time.Clock()

BUTTON = (270,50)
ARROW = (50,50)

max_level = 3
 
def render_level(map_level): 
    
    map_size = pygame.font.SysFont("sans",60)
    map_number = map_size.render("Lv." + str(map_level), True, white)
    map_rect = map_number.get_rect(center=(320, 120))
    screen.blit(map_number, map_rect)
map_level=1
maze = load_maze(f'{map_level}.txt')
goal_state = load_goal_state(f'{map_level}.txt')


def level_zone(map_level,maze):
    screen.fill((0,0,0))
    scale_image(SCREEN_SIZE[0]/(2*len(maze[0])),SCREEN_SIZE[0]/(2*len(maze)))
   
    screen.blit(background_menu,(0,0))

    global arrow_left_menu 
    arrow_left_menu = screen.blit(arrow_left,(0,SCREEN_LEVEL[1]/2-ARROW[0]/2))
    global arrow_right_menu
    arrow_right_menu= screen.blit(arrow_right,(SCREEN_LEVEL[0]-ARROW[0],SCREEN_LEVEL[1]/2-ARROW[0]/2))
    render_level(map_level)
    render_map(maze,screen, SCREEN_SIZE[0]/(2*len(maze[0])), SCREEN_SIZE[0]/(2*len(maze)), SCREEN_SIZE[0]/4, SCREEN_SIZE[1]/4)
    #print(SCREEN_SIZE[0]/(2*len(maze[0])), SCREEN_SIZE[0]/(2*len(maze)))
    if TITLE_STATE == "Not found":
        screen.blit(title_notFound, title_rect)

   
def menu_zone():
    button_pos = SCREEN_MENU[0]/2-BUTTON[0]/2
    
    screen.blit(background_menu,(0,0))
    global start_button
    start_button = screen.blit(button_start,(button_pos,200))
    global exit_button
    exit_button = screen.blit(quit_button,(button_pos,280))      
    screen.blit(title_content, title_rect)
    
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

def end_zone(dy):
    screen.blit(end_background,(0,0))
    screen.blit(car,(SCREEN_SIZE[0]/2-car.get_width()/2,dy))
    clock.tick(15)

    if dy==SCREEN_SIZE[0]-140:
        global return_home 
        return_home = screen.blit(return_button,(SCREEN_SIZE[0]-return_button.get_width(),0))
    # global start_button
    # start_button = screen.blit(button_start,(button_pos,200))
    # global exit_button
    # exit_button = screen.blit(quit_button,(button_pos,280)) 

def load_resource():
    global screen
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption ('SOKOBAN')
    icon = pygame.image.load ('./assets/icon.jpg')
    pygame.display.set_icon(icon)
    
    global floor1
    floor1 = pygame.image.load ('./assets/background.png')
    
    global wall1
    wall1 = pygame.image.load ('./assets/wall.png')
   

    global car1
    car1 = pygame.image.load ('./assets/mushroomGreen.png')
    

    global box1
    box1 = pygame.image.load ('./assets/box.png')
    

    global goal1
    goal1 = pygame.image.load ('./assets/goal.png')
    

    global white
    white = (255,255,255)

    global black
    black = (0,0,0)

    title_size = pygame.font.SysFont("sans",60)

    global title_content
    title_content = title_size.render('Mario SOKOBAN', True, white)

    global title_load
    title_load = title_size.render("      Loading...", True, white)

    global title_notFound
    title_notFound = title_size.render("      Not found", True, white)

    global title_rect
    title_rect = title_content.get_rect(center=(320, 60))

    global arrow_left
    arrow_left =  pygame.image.load ('./assets/arrowLeft.jpg')
    arrow_left =  pygame.transform.scale(arrow_left, ARROW)

    global arrow_right
    arrow_right =  pygame.image.load ('./assets/arrowRight.jpg')
    arrow_right =  pygame.transform.scale(arrow_right, ARROW)


    global background_menu 
    background_menu =  pygame.image.load ('./assets/loadMenu.png')
    background_menu = pygame.transform.scale(background_menu, SCREEN_MENU)

    global end_background
    end_background =  pygame.image.load ('./assets/endGame.jpg')
    end_background = pygame.transform.scale(end_background, SCREEN_MENU)

    global return_button
    return_button =  pygame.image.load ('./assets/returnHome.png')
    return_button = pygame.transform.scale(return_button, (150,50)) 

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

    global dark_red
    dark_red = (136,0,21)

    global title_end
    title_end = title_size.render('Press Enter to continue', True, white)
    
def scale_image(width,height):

    global floor
    floor = pygame.transform.scale(floor1, (width, height))
    global wall
    wall = pygame.transform.scale(wall1,(width, height))
    global car
    car = pygame.transform.scale(car1, (width, height))
    global box
    box = pygame.transform.scale(box1, (width, height))
    global goal 
    goal = pygame.transform.scale(goal1, (width, height))

def game_init(k,maze,curr_state):
    clock.tick(15)
    board = k[curr_state]
    render_map(board,screen,SCREEN_SIZE[0]/len(maze[0]),SCREEN_SIZE[0]/len(maze))

def game_zone():
    map_level=1
    maze = load_maze(f'{map_level}.txt')
    goal_state = load_goal_state(f'{map_level}.txt')

    curr_state = 0
    GAME_STATE="Menu"
    running = True

    show_messagebox = True
    dy=0

    while running:
        
        mouse_pos = pygame.mouse.get_pos()
        if GAME_STATE=="Menu":
            menu_zone()
        if GAME_STATE=="Level":
            maze = load_maze(f'{map_level}.txt')
            goal_state = load_goal_state(f'{map_level}.txt')
            level_zone(map_level,maze)
        if GAME_STATE == "Not found":
            global TITLE_STATE 
            TITLE_STATE = "Not found"
            level_zone(map_level, maze)
            GAME_STATE = "Level"
        if GAME_STATE=="Solve":
            curr_state=0
            problem = SokobanProblem(maze,goal_state)
            dy = 0
            res = BFS(problem)
            if res == False:
                GAME_STATE = "Not found"
            else:
                global k 
                k = res.solution()
                print(k)
                GAME_STATE="Run game"
        if GAME_STATE=="Run game":
            end_game = False
            scale_image(SCREEN_SIZE[0]/len(maze[0]),SCREEN_SIZE[0]/len(maze))
            if curr_state >= len(k):
                clock.tick(1)
                end_game = True 
                    # GAME_STATE="End game"
                    # end_zone(dy)
                curr_state=len(k)-1
            game_init(k,maze,curr_state)
            if end_game:
                screen.blit(title_end,(SCREEN_LEVEL[0]/2-(title_end.get_width())/2 , SCREEN_LEVEL[1]-title_end.get_height()))
            curr_state += 1
        if GAME_STATE=="End game":
            end_zone(dy)
            dy+=15
            if dy>=SCREEN_SIZE[0]-140:
                dy=SCREEN_SIZE[0]-140  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if GAME_STATE == "Run game":
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            GAME_STATE="End game"

            if GAME_STATE == "End game":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if return_home.collidepoint(mouse_pos):
                            GAME_STATE="Level"     

       
            if GAME_STATE=="Level":
                if event.type == pygame.MOUSEBUTTONDOWN  or event.type == pygame.KEYDOWN:
                    if event.button == 1:
                        if arrow_left_menu.collidepoint(mouse_pos) or event.key == pygame.K_LEFT:
                            map_level-=1
                            TITLE_STATE = "Level"
                            if map_level == 0:
                                map_level = 1
                        if arrow_right_menu.collidepoint(mouse_pos) or event.key == pygame.K_RIGHT:
                            map_level+=1
                            TITLE_STATE = "Level"
                            if map_level > max_level:
                                map_level = max_level

                                
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            screen.blit(title_load, title_rect)
                            GAME_STATE="Solve"

            if GAME_STATE=="Menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if start_button.collidepoint(mouse_pos):
                            GAME_STATE="Level"
                        if exit_button.collidepoint(mouse_pos):
                            running = False
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
   

if __name__ == '__main__':
    load_resource()
    # print(res.solution())
    #game_zone()
    #menu_zone()
    game_zone()
    



