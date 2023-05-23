import pygame
import animation_functions

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
pygame.display.set_caption('Animation Practice')

sprite_sheet_image = pygame.image.load('vampire_spritesheet.png').convert_alpha()
sprite_sheet = animation_functions.SpriteSheet(sprite_sheet_image)

BG = (50, 50, 50)
COLOUR = (0, 0, 0)

#create animation list
animation_list = []
animation_steps = [2, 2, 2, 2]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 600 #milliseconds
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_image_list = []
    for _ in range(animation):
        temp_image_list.append(sprite_sheet.get_image(step_counter, 16, 16, 3, COLOUR))
        step_counter += 1
    animation_list.append(temp_image_list)

run = True
while run:

    #Update screen background
    screen.fill(BG)

    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    #show image frames
    screen.blit(animation_list[action][frame], (0, 0))


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0


    pygame.display.update()

pygame.quit()

