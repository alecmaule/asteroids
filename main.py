import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    
    # set up games clock/fps
    
    game_clock = pygame.time.Clock()
    dt = 0
    
    
    # setting up screen size based on constants
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #instantiate player object
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroidfield = AsteroidField()
    
    Player.containers = (updatable, drawable)    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    Shot.containers = (shots, updatable, drawable)
    
   # print game info 
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # main game loop, sets quit control, fills screen, and double buffers
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        # update game objects
        for obj in updatable:
            obj.update(dt)        
            
        for asteroid in asteroids:
            if asteroid.check_for_collision(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.check_for_collision(shot):
                    shot.kill()
                    asteroid.kill()
            
        # draw game objects
        screen.fill((0, 0, 0))  
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()  
        
        dt = game_clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()  