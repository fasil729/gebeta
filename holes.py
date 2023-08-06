import pygame
PIT_WIDTH = 100
PADDING = 20
computer=(250, 246, 246)
palyer=(105, 53, 63)
def create_holes(screen):
    pygame.draw.ellipse(screen, computer, (PADDING, 160, 100, 2*PIT_WIDTH + 40))
    pygame.draw.rect(screen, computer, [PIT_WIDTH + 2*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, computer, [2*PIT_WIDTH + 3*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, computer, [3*PIT_WIDTH + 4*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, computer, [4*PIT_WIDTH + 5*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, computer, [5*PIT_WIDTH + 6*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, computer, [6*PIT_WIDTH + 7*PADDING, 160, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [PIT_WIDTH + 2*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [2*PIT_WIDTH + 3*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [3*PIT_WIDTH + 4*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [4*PIT_WIDTH + 5*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [5*PIT_WIDTH + 6*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.rect(screen, palyer, [6*PIT_WIDTH + 7*PADDING, 300, PIT_WIDTH, PIT_WIDTH], border_radius=40)
    pygame.draw.ellipse(screen, palyer, (7*PIT_WIDTH + 8*PADDING, 160, 100, 2*PIT_WIDTH + 40))

    return screen
