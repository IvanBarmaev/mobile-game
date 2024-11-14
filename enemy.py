import pygame
from random import randint, choice
from math import sqrt

class Enemy:
	def __init__(self, surf, size, point, speed):
		self.surf = surf
		self.surf_rect = surf.get_rect()
		self.x, self.y = 0, 0
		self.size = size
		self.moveTo = point
		self.speed = speed
		self.speedx, self.speedy = 0, 0
		self.set_point(point)
		self.set_XY()
	
	def set_XY(self):
		if randint(0, 1):
			self.x = choice([0 - self.size, self.surf_rect.width])
			self.y = randint(0, self.surf_rect.height)
		else:
			self.x = randint(0, self.surf_rect.width)
			self.y = choice([0 - self.size, self.surf_rect.height])
	
	def set_point(self, point):
		self.moveTo = point
		self.gip = sqrt((self.x - point[0]) ** 2 + (self.y - point[1]) ** 2)
		self.speedx = (self.x - point[0]) / self.gip * self.speed
		self.speedy = (self.y - point[1] ) /self.gip * self.speed
	
	def hide(self):
		pygame.draw.rect(self.surf, (100, 100, 100), (self.x, self.y, self.size, self.size))
		
	def render(self):
		pygame.draw.rect(self.surf, (250, 10, 10), (int(self.x), int(self.y), self.size, self.size))
	
	def update(self, point):
		self.hide()
		self.x -= self.speedx
		self.y -= self.speedy
		if self.x > self.surf_rect.width:
			self.set_XY()
			self.set_point(point)
		elif self.x < 0 - self.size:
			self.set_XY()
			self.set_point(point)
		if self.y > self.surf_rect.height:
			self.set_XY()
			self.set_point(point)
		elif self.y < 0 - self.size:
			self.set_XY()
			self.set_point(point)
		self.render()
		