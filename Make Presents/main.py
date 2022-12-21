import pygame

pygame.init()
SCREEN = pygame.display.set_mode((500, 750))

# Caption and Icon
pygame.display.set_caption("santa's workshop")
icon = pygame.image.load('santa-claus.png').convert_alpha()
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('santa.png').convert_alpha()
playerX = 226
playerY = 240
playerX_change = 0

# machine
machineImg = pygame.image.load('machine.png').convert_alpha()
machineX = -10
machineY = 140

# Backround
background_Img = pygame.image.load('santas-workshop.png').convert()

# font
font = pygame.font.Font('freesansbold.ttf', 17)
font2 = pygame.font.Font('freesansbold.ttf', 12)

# machine prompt
machineDisplay = font.render(f"Press E to Make Presents", True, (255, 255, 255))
outline = font.render(f"Press E to Make Presents", True, (0, 0, 0))

# hiring icon
hiring_Img = pygame.image.load('hiring.png').convert_alpha()

# hiring prompt
hiringDisplay = font.render(f"Press Q to Hire Elves", True, (255, 255, 255))
hiringOutline = font.render(f"Press Q to Hire Elves", True, (0, 0, 0))

# list of elves
listOfElves_Img = pygame.image.load('list.png').convert_alpha()
listX = 2000
listY = -20
listTitle = font.render(f"Santa's Elves", True, (255, 255, 255))

elf1_1 = font2.render(f"Dave: Press Z", True, (255, 255, 255))
elf1_2 = font2.render(f"At 10 Presents For 1", True, (255, 255, 255))
elf1_3 = font2.render(f"Extra Present Per Click", True, (255, 255, 255))

elf2_1 = font2.render(f"Timmy: Press X", True, (255, 255, 255))
elf2_2 = font2.render(f"At 30 Presents For 2", True, (255, 255, 255))
elf2_3 = font2.render(f"Extra Presents Per Click", True, (255, 255, 255))

elf3_1 = font2.render(f"John: Press C", True, (255, 255, 255))
elf3_2 = font2.render(f"At 70 Presents For 3", True, (255, 255, 255))
elf3_3 = font2.render(f"Extra Presents Per Click", True, (255, 255, 255))

elf4_1 = font2.render(f"Richard: Press V", True, (255, 255, 255))
elf4_2 = font2.render(f"At 140 Presents For 4", True, (255, 255, 255))
elf4_3 = font2.render(f"Extra Presents Per Click", True, (255, 255, 255))

exit = font2.render(f"Press R To Exit", True, (255, 255, 255))

pressOnce1 = False
pressOnce2 = False
pressOnce3 = False
pressOnce4 = False

# Score
score_value = 0
score_increase = 1
scorefont = pygame.font.Font('freesansbold.ttf', 17)
textX = 0
testY = 0

# End screen
End_Img = pygame.image.load('Good-job.png').convert_alpha()

# starting prompt
startfont = pygame.font.Font('freesansbold.ttf', 25)
startX = 0
startY = 100
startY2 = 120

def player(x, y):
    SCREEN.blit(playerImg, (x, y))


def machine(x, y):
    SCREEN.blit(machineImg, (x, y))


def hiring(x, y):
    SCREEN.blit(hiring_Img, (x, y))


def elflist(x, y):
    SCREEN.blit(listOfElves_Img, (x, y))


def show_score(x, y):
    score = scorefont.render("Presents : " + str(score_value), True, (255, 255, 255))
    SCREEN.blit(score, (x, y))

def start(x, y):
    start = startfont.render(f"Press Arrow Keys Left and Right To Move", True, (0, 0, 0))
    SCREEN.blit(start, (x, y))
  
def start2(x, y):
    start = startfont.render(f"Make 250 Presents To Win (kinda laggy)", True, (0, 0, 0))
    SCREEN.blit(start, (x, y))
  
# Game Loop
running = True
while running:
  
    # RGB
    SCREEN.fill((0, 0, 0))
    # Background Image
    SCREEN.blit(background_Img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
            # player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
                startX += 2000
            if event.key == pygame.K_RIGHT:
                playerX_change = 2
                startX += 2000
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 436:
        playerX = 436

    # interacting with machine
    machine(machineX, machineY)
    if 20 <= playerX <= 126:
        SCREEN.blit(outline, (10, 178))
        SCREEN.blit(outline, (10, 182))
        SCREEN.blit(outline, (8, 180))
        SCREEN.blit(outline, (12, 180))
        SCREEN.blit(machineDisplay, (10, 180))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    score_value += score_increase

        # list of elves
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    listX = 150
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    listX = 2000

            # elf buffs
    if score_value >= 10:
        if pressOnce1 != True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        score_increase += 1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_z:
                        pressOnce1 = True

    if score_value >= 30:
        if pressOnce2 != True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        score_increase += 2
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_x:
                        pressOnce2 = True

    if score_value >= 70:
        if pressOnce3 != True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        score_increase += 3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_c:
                        pressOnce3 = True

    if score_value >= 140:
        if pressOnce4 != True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_v:
                        score_increase += 4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_v:
                        pressOnce4 = True

    # hiring elves (prompt)
    if 1 <= score_value <= 4:
        SCREEN.blit(hiringOutline, (260, 28))
        SCREEN.blit(hiringOutline, (260, 32))
        SCREEN.blit(hiringOutline, (258, 30))
        SCREEN.blit(hiringOutline, (262, 30))
        SCREEN.blit(hiringDisplay, (260, 30))

        # hiring elves (icon)
    if score_value >= 1:
        SCREEN.blit(hiring_Img, (440, 10))
                      
    start2(startX, startY2)
    start(startX,startY)
    show_score(textX, testY)
    player(playerX, playerY)
    elflist(listX, listY)
    # list of elves (text)
    if listX == 150:
        SCREEN.blit(listTitle, (250, 20))

        SCREEN.blit(elf1_1, (250, 45))
        SCREEN.blit(elf1_2, (250, 60))
        SCREEN.blit(elf1_3, (250, 75))

        SCREEN.blit(elf2_1, (250, 105))
        SCREEN.blit(elf2_2, (250, 120))
        SCREEN.blit(elf2_3, (250, 135))

        SCREEN.blit(elf3_1, (250, 165))
        SCREEN.blit(elf3_2, (250, 180))
        SCREEN.blit(elf3_3, (250, 195))

        SCREEN.blit(elf4_1, (250, 225))
        SCREEN.blit(elf4_2, (250, 240))
        SCREEN.blit(elf4_3, (250, 255))

        SCREEN.blit(exit, (250, 285))
    if score_value >= 250:
        SCREEN.blit(End_Img, (0, 0))
    pygame.display.update()
