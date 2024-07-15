import pygame


class Button:
	def __init__(self, font, text, color1, color2, width, height, sound):
		self.font = font
		self.text = text
		self.color1 = color1
		self.color2 = color2
		self.hovered = False
		self.sound = sound
		self.render = font.render(text, True, color1)
		self.rect = self.render.get_rect(center=(width, height))
		# self.mouse_collider(mouse_pos, font, text, color1, color2, sound)

	def mouse_collider(self, mouse_pos, font, text, color1, color2, sound):
		if self.rect.collidepoint(mouse_pos):
			if not self.hovered:
				sound.play()
				self.hovered = True
			self.render = font.render(text, True, color1)
		else:
			self.render = font.render(text, True, color2)
			self.hovered = False

	def button_loop(self, screen, mouse_pos, font, text, color1, color2, sound):
		self.mouse_collider(mouse_pos, font, text, color1, color2, sound)
		screen.blit(self.render, self.rect)
