import pygame

pygame.init() #initilize Pygame

height = 600
width = 1000

screen = pygame.display.set_mode((width, height)) #Making the Screen

#game loop
run = True
while run: #while game is running
    for event in pygame.event.get(): #Retrives events
        if event.type == pygame.QUIT: #if the X at the top right is clicked
            run = False #turns off game


