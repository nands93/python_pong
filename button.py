import pygame


class Button:
	def __init__(self, font, text, color1, color2, width, height, mouse_pos):
		self.render = font.render(text, True, color1)
		self.rect = self.render.get_rect(center=(width, height))
		self.mouse_collider(mouse_pos, font, text, color1, color2)
		self.font = font
		self.text = text
		self.color1 = color1
		self.color2 = color2

	def mouse_collider(self, mouse_pos, font, text, color1, color2):
		if self.rect.collidepoint(mouse_pos):
			self.render = font.render(text, True, color1)
		else:
			self.render = font.render(text, True, color2)

	def screen_blit(self, screen):
		screen.blit(self.render, self.rect)
