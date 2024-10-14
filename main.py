import pygame
from constants import *
import player

clock = pygame.time.Clock()
dt = 0
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = player.Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        p1.update(dt)
        p1.draw(screen)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
