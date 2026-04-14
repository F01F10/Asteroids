import pygame
from logger import log_state
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
import sys


def main():
    #Initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    drawable= pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    a_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    #GAME LOOP
    while 1>0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt/100)
        #Colision detection-----
        for rock in asteroids:
            if rock.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for rock in asteroids:
            for bullet in shots:
                    if rock.collides_with(bullet):
                        log_event("asteroid_shot")
                        rock.kill()
                        bullet.kill()
        #-----------------------
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt=pygame.time.get_ticks()/1000
    
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
