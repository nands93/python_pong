import pygame


class Player:
	def __init__(self, x_pos, y_pos, speed, width, height):
		self.rect = pygame.Rect(x_pos, y_pos, width, height)
		self.speed = speed
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.speed = speed
		self.width = width
		self.height = height
		self.score = 0

	def move_up(self):
		if self.rect.top > 0:
			self.rect.y -= self.speed

	def move_down(self):
		if self.rect.bottom < pygame.display.get_surface().get_height():
			self.rect.y += self.speed

	def reset_position(self, y_position):
		self.rect.y = y_position
