# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 11:58:48 2021

@author: theod
"""

import pygame
# import time
import random
import sys
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
red_dark = (255, 20, 20)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 190, 0)
green_dark = (142, 204, 57)
green_light = (167, 217, 72)
 
dis_width = 800
dis_height = 800
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 20
snake_speed = 10
default_speed = snake_speed

 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def display_title(score, multiplier):
    # value = score_font.render("Your Score: " + str(score), True, yellow)
    # dis.blit(value, [0, 0])
    pygame.display.set_caption("Score: " + str(score) + " - " + "Multiplicateur: " + str(multiplier))

def display_board():
    dis.fill(blue)
 
def our_snake(snake_block, snake_list):
    # print(snake_list)
    for x in snake_list:
        if x == snake_list[-1]:
            pygame.draw.rect(dis, orange, [x[0], x[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop(snake_speed):
    game_over = False
    game_close = False
 
    x1 = int(int(dis_width / snake_block) * snake_block / 2)
    y1 = int(int(dis_height / snake_block) * snake_block / 2)
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    snakeLen = 1
    snake_speed = 10
 
    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
    
    score_multiplier = 1
    score = 0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            display_title(score, score_multiplier)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(snake_speed)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT) and (x1_change != snake_block):
                    x1_change = -snake_block
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT) and (x1_change != -snake_block):
                    x1_change = snake_block
                    y1_change = 0
                elif (event.key == pygame.K_UP) and (y1_change != snake_block):
                    y1_change = -snake_block
                    x1_change = 0
                elif (event.key == pygame.K_DOWN) and (y1_change != -snake_block):
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_SPACE:
                    snake_speed += default_speed
                    score_multiplier = int(snake_speed/default_speed)

        x1 += x1_change
        y1 += y1_change
        
        # print(x1, y1)
        
        if x1 > dis_width or x1 < 0 or y1 > dis_height or y1 < 0:
            game_close = True
            
        # dis.fill(blue)
        display_board()
        pygame.draw.rect(dis, red_dark, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snakeLen:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        display_title(score, score_multiplier)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            snakeLen += 1
            score += score_multiplier * 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    # quit()
    sys.exit()
 
 
gameLoop(snake_speed)