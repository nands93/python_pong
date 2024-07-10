import pygame


class Button:
	def __init__(self, font, text, color, width, height):
		self.render = font.render(text, True, color)
		self.rect = self.render.get_rect(center=(width, height))
		self.font = font
		self.text = text
		self.color = color

	def mouse_collider(self, mouse_pos, font, text, color1, color2):
		if self.rect.collidepoint(mouse_pos):
			self.render = font.render(text, True, color1)
		else:
			self.render = font.render(text, True, color2)

	def screen_blit(self, screen):
		screen.blit(self.render, self.rect)
