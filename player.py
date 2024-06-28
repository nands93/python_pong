import pygame


class Player:
	def __init__(self, x_pos, y_pos, speed, width, height):
		self.rect = pygame.Rect(x_pos, y_pos, width, height)
		self.speed = speed
		self.score = 0
