import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	pygame.display.set_caption("TEMU Asteroids")
	background = pygame.image.load("space.jpg")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, drawable, updatable)
	
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2,)
	asteroidfield = AsteroidField()
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		for obj in updatable:
			obj.update(dt)

		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game Over!")
				sys.exit()
			
			for bullet in shots:
				if asteroid.collision(bullet):
					bullet.kill()
					asteroid.split()
		
		screen.blit(background, (0,0))
		
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		
		dt = clock.tick(60) / 1000




if __name__ == "__main__":
	main()
