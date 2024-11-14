import pygame

class Player:
	def __init__(self, surf, x, y, speed, size):
		self.surf = surf
		self.surf_rect = surf.get_rect()
		self.x, self.y = x, y
		self.speed = speed
		self.size = size
	
	def update(self, cos, sin):
		pygame.draw.rect(self.surf, (100, 100, 100), (self.x, self.y, self.size, self.size))
		self.x -= self.speed * cos
		self.y -= self.speed * sin
		if self.x >= self.surf_rect.width - self.size:
			self.x = self.surf_rect.width - self.size
		elif self.x < 0:
			self.x = 0
		if self.y > self.surf_rect.height - self.size:
			self.y = self.surf_rect.height - self.size
		elif self.y < 0:
			self.y = 0
		pygame.draw.rect(self.surf, (0, 255, 0), (self.x, self.y, self.size, self.size))