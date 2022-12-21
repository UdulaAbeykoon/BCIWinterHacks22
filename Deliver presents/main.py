import pygame
import random

pygame.init()

SCREEN = pygame.display.set_mode((500, 750))  # display size

pygame.display.set_caption("Deliver The Presents")
icon = pygame.image.load('images/rudolph.png')
pygame.display.set_icon(icon)


BACKGROUND_IMAGE = pygame.image.load('images/background.jpg')


santa_IMAGE = pygame.image.load('images/santa1.png')
santa_x = 50
santa_y = 300
santa_y_change = 0

def display_santa(x, y):
    SCREEN.blit(santa_IMAGE, (x, y))


OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(150,450)
OBSTACLE_COLOR = (211, 211, 211)
OBSTACE_X_CHANGE = -4
obstacle_x = 500

def display_obstacle(height):
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 635 - height - 150
    pygame.draw.rect(SCREEN, OBSTACLE_COLOR, (obstacle_x, 635, OBSTACLE_WIDTH, -bottom_obstacle_height))


def collision_detection (obstacle_x, obstacle_height, santa_y, bottom_obstacle_height):
    if obstacle_x >= 50 and obstacle_x <= (50 + 64):
        if santa_y <= obstacle_height or santa_y >= (bottom_obstacle_height - 64):
            return True
    return False


score = 0
SCORE_FONT = pygame.font.Font('freesansbold.ttf', 32)

def score_display(score):
    display = SCORE_FONT.render(f"Presents Delivered: {score}", True, (255,255,255))
    SCREEN.blit(display, (10, 10))


startFont = pygame.font.Font('freesansbold.ttf', 32)
startFont1 = pygame.font.Font('freesansbold.ttf', 25)
def start():
   
    display = startFont.render(f"PRESS SPACE BAR TO START ", True, (255, 255, 255))
    display1 = startFont1.render(f"*STAY CLOSE TO THE OBSTACLE*", True, (250,250,250))
    SCREEN.blit(display, (20, 200))
    SCREEN.blit(display1, (50, 250))
    pygame.display.update()


score_list = [0]

game_over_font1 = pygame.font.Font('freesansbold.ttf', 64)
game_over_font2 = pygame.font.Font('freesansbold.ttf', 32)

def game_over():
   
    maximum = max(score_list)
    
    display1 = game_over_font1.render(f"GAME OVER", True, (200,35,35))
    SCREEN.blit(display1, (50, 300))
    
    display2 = game_over_font2.render(f"SCORE: {score} MAX SCORE: {maximum}", True, (255, 255, 255))
    SCREEN.blit(display2, (50, 400))
   
    if score == maximum:
        display3 = game_over_font2.render(f"NEW HIGH SCORE!", True, (200,35,35))
        SCREEN.blit(display3, (80, 100))

running = True

waiting = True
collision = False

while running:

    SCREEN.fill((0, 0, 0))

   
    SCREEN.blit(BACKGROUND_IMAGE, (0, 0))

   
    while waiting:
        if collision:
            
            game_over()
            start()
        else:
           
            start()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                  
                    score = 0
                    santa_y = 300
                    obstacle_x = 500
                   
                    waiting = False

            if event.type == pygame.QUIT:
               
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               
                santa_y_change = -6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
             
                santa_y_change = 3

   
    santa_y += santa_y_change
  
    if santa_y <= 0:
        santa_y = 0
    if santa_y >= 571:
        santa_y = 571

   
    obstacle_x += OBSTACE_X_CHANGE

   
    collision = collision_detection(obstacle_x, OBSTACLE_HEIGHT, santa_y, OBSTACLE_HEIGHT + 150)

    if collision:
     
        score_list.append(score)
        waiting = True

  
    if obstacle_x <= -10:
        obstacle_x = 500
        OBSTACLE_HEIGHT = random.randint(200, 400)
        score += 1

    display_obstacle(OBSTACLE_HEIGHT)

    display_santa(santa_x, santa_y)

   
    score_display(score)

   
    pygame.display.update()


pygame.quit()
  
