import pygame
import random

class Ball:
	def __init__(self, size, x, y, speed_x, speed_y, width, height):
		self.rect = pygame.Rect(width // 2 - size // 2, height // 2 - size // 2, size, size)
		self.size = size
		self.speed_x = speed_x
		self.speed_y = speed_y
		self.initial_x = x
		self.initial_y = y
		self.initial_speed_x = speed_x
		self.initial_speed_y = speed_y
		self.width = width
		self.height = height
		self.x = x
		self.y = y

	def movement(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y

	def collision(self, player1, player2):
		if self.rect.top <= 0 or self.rect.bottom >= self.height:
			self.speed_y *= -1
		if self.rect.left <= 0:
			player2.score += 1
			self.reset_position()
		if self.rect.right >= self.width:
			player1.score += 1
			self.reset_position()
		if self.rect.colliderect(player1.rect) or self.rect.colliderect(player2.rect):
			self.speed_x *= -1

	def reset_position(self):
		self.rect.x = self.initial_x
		self.rect.y = random.randint(50, 550)
		self.speed_x = self.initial_speed_x * random.choice([-1, 1])
		self.speed_y = self.initial_speed_y * random.choice([-1, 1])

