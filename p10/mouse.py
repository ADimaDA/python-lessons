import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()

def main():
    is_draw = false
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                if event.button == 1:
                    is_draw = True
                if event.button == 3:
                    screen.fill((0, 0, 0))
                    pygame.display.flip()









