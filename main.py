""" Snake+ by Dontobasso
A remade version of the well-known classic Snake game.
For license, read license file in snake_plus folder."""

#* Imports
import pygame
import time
import random


#* Inits
pygame.init()
game_quit = False


#* Generic variables
display_width = 500     #* display
display_height = 500

red = (232, 45, 12)       #* Colours
green = (39, 214, 111)
blue = (6, 0, 94)
cyan = (46, 177, 230)
purple = (132, 13, 212)
lavender = (193, 187, 250)
turquoise = (49, 224, 181)
white = (255, 255, 255)
black = (0, 0, 0)

snake_block = 10      #* Snake
snake_speed = 6.0

small_font = pygame.font.SysFont("bahnschrift", 30)     #* UI 
medium_font = pygame.font.SysFont("bahnschrift", 22)
big_font = pygame.font.SysFont("bahnschrift", 40)
score_font = pygame.font.SysFont("bahnschrift", 15)
copyright_font = pygame.font.SysFont("bahnschrift", 18)

clock = pygame.time.Clock()     #* Time


#* Display
dis = pygame.display.set_mode((display_width, display_height))

pygame.display.update()
pygame.display.set_caption("Snake+")


#* Score
def score(score):
    points = score_font.render("Score: " + str(score) + "   [M - Menu]", True, blue)
    dis.blit(points, [0, 0])


#* Snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, purple, [x[0], x[1], snake_block, snake_block])


#* Text
def message1(msg, color):
    message1 = big_font.render(msg, True, color)
    dis.blit(message1, [10, 50])

def message2(msg, color):
    message2 = small_font.render(msg, True, color)
    dis.blit(message2, [10, 120])

def message3(msg, color):
    message3 = small_font.render(msg, True, color)
    dis.blit(message3, [10, 190])

def message4(msg, color):
    message4 = medium_font.render(msg, True, color)
    dis.blit(message4, [10, 300])

def message5(msg, color):
    message5 = medium_font.render(msg, True, color)
    dis.blit(message5, [10, 350])

def message6(msg, color):
    message6 = medium_font.render(msg, True, color)
    dis.blit(message6, [10, 400])

def message7(msg, color):
    message7 = copyright_font.render(msg, True, color)
    dis.blit(message7, [300, 470])

#* Game
def game():
    game_quit = False       #* Starting and ending the game 
    game_over = False
    menu = False

    snakex = display_width / 2      #* Coordinates / movement
    snakey = display_height / 2

    snakex_change = 0
    snakey_change = 0

    snake_list = []      #* Snake length
    snake_length = 1

    score_value = snake_length - 1      #* Score to be on game over screen

    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0        #* Food
    foody = round(random.randrange(display_width - snake_block) / 10.0) * 10.0

    while not game_quit:

        while game_over == True:       #* Game ending
            dis.fill(turquoise)
            message1("Game over!", blue)
            message2("[P- Play] [Q - Quit]", blue)
            message3("Score: " + str(score_value), blue)
            message4("Navigate snake with arrow keys.", blue)
            message5("Eat apples to increase score.", blue)
            message6("Snake will also become longer and faster.", blue)
            message7("© 2021 Dontobasso", red)

            score(snake_length - 1)     #* Score
            score_value = snake_length - 1

            pygame.display.update()     #* Update display

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:     #* After game end menu
                    if event.key == pygame.K_q:     #* Button Q quits
                        game_quit = True
                        game_over = False 
                    elif event.key == pygame.K_p:     #* Button P plays again
                        game()

        while menu == True:     #* Menu
            dis.fill(turquoise)
            message1("Menu", blue)
            message2("[P- Play] [Q - Quit]", blue)
            message3("Score: " + str(score_value), blue)
            message4("Navigate snake with arrow keys.", blue)
            message5("Eat apples to increase score.", blue)
            message6("Snake will also become longer and faster.", blue)
            message7("© 2021 Dontobasso", red)

            pygame.display.update()

            for event in pygame.event.get():        #* Key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.QUIT()
                        quit()
                    elif event.key == pygame.K_p:
                        menu = False
            
        for event in pygame.event.get():        #* Events
            if event.type == pygame.QUIT:       #* Pressing X in corner of window closes window
                game_quit = True
            print(event)        #* Prints all actions in output

            if event.type == pygame.KEYDOWN:        #* Key presses
                if event.key == pygame.K_LEFT:      #* Left arrow press
                    snakex_change = -snake_block
                    snakey_change = 0
                elif event.key == pygame.K_RIGHT:       #* Right arrow press
                    snakex_change = snake_block
                    snakey_change = 0
                elif event.key == pygame.K_UP:      #* Up arrow press
                    snakex_change = 0
                    snakey_change = -snake_block
                elif event.key == pygame.K_DOWN:        #* Down arrow press
                    snakex_change = 0
                    snakey_change = snake_block
                elif event.key == pygame.K_m:       #* Open menu
                    menu = True

        if snakex >= display_width or snakex < 0 or snakey >= display_height or snakey < 0:
            game_over = True

        snakex += snakex_change    #* Coordinates
        snakey += snakey_change

        dis.fill(green)     #* Draws

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])        #* Food

        snake_head = []      #* Snake
        snake_head.append(snakex)
        snake_head.append(snakey)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True

        snake(snake_block, snake_list)

        snake_speed = snake_length / 2 + 6

        score(snake_length - 1)

        pygame.display.update()     #* Update display

        if snakex == foodx and snakey == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0        #* Food
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            
            snake_length += 1       #* Increase snake length

        clock.tick(snake_speed)      #* Time

    pygame.quit()       #* Quit
    quit() 

game()      #* Runs game
