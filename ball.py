import pygame
from player import Player


class Ball:
	def __init__(self, size, speed_x, speed_y, width, height):
		self.rect = pygame.Rect(width // 2 - size // 2, height // 2 - size // 2, size, size)
		self.size = size
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.width = width
		self.height = height
		self.x = 0
		self.y = 0

	def movement(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

	def collision(self, player1, player2):
		if self.rect.top <= 0 or self.rect.bottom >= self.height:
			self.speed_y *= -1
		if self.rect.left <= 0 or self.rect.right >= self.width:
			self.speed_x *= -1
		if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
			self.speed_x *= -1

