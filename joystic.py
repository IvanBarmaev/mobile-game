import pygame
from math import sqrt

class Joystic:
	def __init__(self, surf, x, y, radius):
		self.surf = surf
		self.x, self.y = x, y #центр стика
		self.curX, self.curY = x, y
		self.radius = radius
		self.activated = False
	
	def reset(self):
		self.curX, self.curY = self.x, self.y
		self.activated = False
	
	def touch(self, x, y):
		try:
			self.gip = (sqrt((x - self.x) ** 2 + (y - self.y) ** 2))
			self.cos, self.sin = 0, 0
			if  self.gip <= self.radius:
				self.curX = x
				self.curY = y
				self.activated = True
				self.sin = (self.y - self.curY) / self.gip * (self.gip / self.radius)
				self.cos = (self.x - self.curX) / self.gip * (self.gip / self.radius)
			if self.gip > self.radius and self.activated:
				self.cos = (self.x - x) / self.gip
				self.curX = self.x - self.radius * self.cos
				self.sin = (self.y - y) / self.gip
				self.curY = self.y - self.radius * self.sin
			return (self.cos, self.sin)
		except ZeroDivisionError:
			self.curX = self.x
			self.curY = self.y
	
	def render(self):
		pygame.draw.rect(self.surf, (10, 10, 10), (self.x - self.radius * 1.5, self.y - self.radius * 1.5, self.radius * 3, self.radius * 3))
		pygame.draw.circle(self.surf, (250, 250, 250), (self.x, self.y), self.radius, 3)
		pygame.draw.circle(self.surf, (250, 250, 250), (self.curX, self.curY), self.radius // 2)