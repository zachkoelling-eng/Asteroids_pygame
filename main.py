import pygame
import sys
from shot import Shot
from constants import *
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    
    # define our groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # configure containers 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    field = AsteroidField()
    player1 = Player(x = SCREEN_WIDTH/2, y= SCREEN_HEIGHT/2)

    # main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        for stat in updatable:
            stat.update(dt)

        for rock in asteroids:
            # check if any asteroid has hit the player
            if rock.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            # check if any shot has hit an asteroid
            for shot in shots:
                if shot.collides_with(rock):
                    log_event("asteroid_shot")
                    rock.kill()
                    shot.kill()
        
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()
        dt = ( clock.tick(60) ) / 1000


if __name__ == "__main__":
    main()
