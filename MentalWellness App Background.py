import pygame

pygame.init()

#colors
black = [0, 0, 0]
white = [255, 255, 255]
fadedBlueGreen = (118, 207, 223)
blueGreen = (96,181,196)
yellow = (255,222,89)
light_orange = (255,189,89)
orange = (255,145,77)
red = (255,87,87)
pink = (255,102,196)
light_purple = (80,42,90)
purple = (140, 82, 255)
dark_blue = (82, 113, 255)
blue = (56, 182, 255)
light_blue = (92, 225, 230)
dark_green = (126, 217, 87)
light_green = (201, 226, 101)
grey = (217, 217, 217)


global white_button
white_button = pygame.Rect (50,490,60,60)
global yellow_button
yellow_button = pygame.Rect (120,490,60,60)
global lorange_button
lorange_button = pygame.Rect (190,490,60,60)
global orange_button
orange_button = pygame.Rect (260,490,60,60)
global red_button
red_button = pygame.Rect (330,490,60,60)
global pink_button
pink_button = pygame.Rect (50,560,60,60)
global light_purple_button
light_purple_button = pygame.Rect (120,560,60,60)
global purple_button
purple_button = pygame.Rect (190,560,60,60)
global dark_blue_button
dark_blue_button = pygame.Rect (260,560,60,60)
global blue_button
blue_button = pygame.Rect (330,560,60,60)

global accessory_button
accessory_button = pygame.Rect (50,725,50,50)
global background_button
background_button = pygame.Rect (350,725,50,50)


size = (443,788)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("ElleHacks 2020")

clock = pygame.time.Clock()
player_icon = pygame.image.load("cactus.png")
player_icon = pygame.transform.scale (player_icon, [100,156])

background = pygame.image.load("PERSONALIZED THING.png")
background = pygame.transform.scale (background, size)

accessory_background = pygame.image.load("image.png")
accessory_background = pygame.transform.scale (accessory_background, size)

background_Original = True
accessory_Original = False

def changetoWhiteBackground():
    global color
    color = white
    pygame.draw.rect(screen, color, [0, 0, 443, 460])

def changetoYellowBackground():
    global color
    color = yellow
    pygame.draw.rect(screen, color, [0, 0, 443, 460])

def changetoLOrangeBackground():
    global color
    color = light_orange
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoOrangeBackground():
    global color
    color = orange
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoRedBackground():
    global color
    color = red
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoPinkBackground():
    global color
    color = pink
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoLightPurpleBackground():
    global color
    color = light_purple
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoPurpleBackground():
    global color
    color = purple
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoDarkBlueBackground():
    global color
    color = dark_blue
    pygame.draw.rect(screen, color, [0, 0, 443, 460])
def changetoBlueBackground():
    global color
    color = blue
    pygame.draw.rect(screen, color, [0, 0, 443, 460])

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                background_Original = False
                if white_button.collidepoint(event.pos):
                    changetoWhiteBackground()
                if yellow_button.collidepoint(event.pos):
                    changetoYellowBackground()
                if lorange_button.collidepoint(event.pos):
                    changetoLOrangeBackground()
                if orange_button.collidepoint(event.pos):
                    changetoOrangeBackground()
                if red_button.collidepoint(event.pos):
                    changetoRedBackground()
                if pink_button.collidepoint(event.pos):
                    changetoPinkBackground()
                if light_purple_button.collidepoint(event.pos):
                    changetoLightPurpleBackground()
                if purple_button.collidepoint(event.pos):
                    changetoPurpleBackground()
                if dark_blue_button.collidepoint(event.pos):
                    changetoDarkBlueBackground()
                if blue_button.collidepoint(event.pos):
                    changetoBlueBackground()

                if accessory_button.collidepoint(event.pos):
                    background_Original = False
                    accessory_Original = True
                if background_button.collidepoint(event.pos):
                    background_Original = True
                    accessory_Original = False

    # Set the screen background
    if background_Original == True:
        screen.fill(white)
        screen.blit(background, [0, 0])
        pygame.draw.rect (screen, white, [0, 0, 443, 460])

    if accessory_Original ==True:
        screen.fill(black)
        screen.blit(accessory_background, [0, 0])
        pygame.draw.rect(screen, color, [0, 0, 443, 460])

    screen.blit (player_icon, [180,150])
    pygame.display.flip()
    clock.tick(20)

pygame.quit()