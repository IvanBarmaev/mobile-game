import pygame
from settings import *
from enemy import Enemy
from joystic import Joystic
from player import Player

class Game:
	def __init__(self, player_speed, enemy_speed, enemy_count):
		self.gameSurf = pygame.Surface((WIDTH, int(HEIGHT * 0.75)))
		self.joysticSurf = pygame.Surface((720, HEIGHT - int(HEIGHT * 0.25)))
		self.joysticSurf.fill((10, 10, 10))
		self.joystic = Joystic(self.joysticSurf, 360, (HEIGHT - int(HEIGHT * 0.75)) // 2, int(HEIGHT * 0.12))
		self.gameSurf.fill((100, 100, 100))
		self.enemy = []
		for i in range(enemy_count):
			self.enemy.append(Enemy(self.gameSurf, 50, (10, 0), enemy_speed))
		self.player = Player(self.gameSurf, 335, 475, player_speed, 50)
		self.task = self.wait
	
	def wait(self, x, y):
		return (0, 0)
	
	def collide(self, obj1, obj2):
		if ((obj1.x > obj2.x and obj1.x < obj2.x + obj2.size) or (obj1.x + obj1.size > obj2.x and obj1.x < obj2.x + obj2.size)) and ((obj1.y > obj2.y and obj1.y < obj2.y + obj2.size) or (obj1.y + obj1.size > obj2.y and obj1.y + obj1.size < obj2.y + obj2.size)):
			return True
		return False
	
	def play(self):
		while True:
			for i in pygame.event.get():
				if i.type == pygame.MOUSEBUTTONDOWN:
					self.task = self.joystic.touch
				elif i.type == pygame.MOUSEBUTTONUP:
					self.joystic.reset()
					self.task = self.wait
			mouse = pygame.mouse.get_pos()
			self.joystic.render()
			self.player.update(*self.task(mouse[0], mouse[1] - int(HEIGHT * 0.75)))
			for i in self.enemy:
				i.update((self.player.x, self.player.y))
				if self.collide(self.player, i):
					return True
			sc.blit(self.joysticSurf, (0, HEIGHT - int(HEIGHT * 0.25)))
			sc.blit(self.gameSurf, (0, 0))
			pygame.display.update()
			clock.tick(60)
