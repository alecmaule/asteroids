import pygame
from constants import *
from player import *

def main():
    pygame.init()
    
    # set up games clock/fps
    
    game_clock = pygame.time.Clock()
    dt = 0
    
    
    # setting up screen size based on constants
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #instantiate player object
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
   # print game info 
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # main game loop, sets quit control, fills screen, and double buffers
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = game_clock.tick(60) / 1000
        
        screen.fill((0, 0, 0))
        player.draw(screen)
        player.update(dt)
        
        pygame.display.flip()
        

        


if __name__ == "__main__":
    main()  