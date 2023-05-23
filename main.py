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

frame_0 = sprite_sheet.get_image(0, 16, 16, 3, COLOUR)
frame_1 = sprite_sheet.get_image(1, 16, 16, 3, COLOUR)
frame_2 = sprite_sheet.get_image(2, 16, 16, 3, COLOUR)
frame_3 = sprite_sheet.get_image(3, 16, 16, 3, COLOUR)
frame_4 = sprite_sheet.get_image(4, 16, 16, 3, COLOUR)
frame_5 = sprite_sheet.get_image(5, 16, 16, 3, COLOUR)
frame_6 = sprite_sheet.get_image(6, 16, 16, 3, COLOUR)
frame_7 = sprite_sheet.get_image(7, 16, 16, 3, COLOUR)

run = True
while run:

    screen.fill(BG)

    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (50, 0))
    screen.blit(frame_2, (100, 0))
    screen.blit(frame_3, (150, 0))
    screen.blit(frame_4, (200, 0))
    screen.blit(frame_5, (250, 0))
    screen.blit(frame_6, (300, 0))
    screen.blit(frame_7, (350, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

