import pygame
from player import Player
from ball import Ball
import sys


def draw_on_screen(screen, color1, color2, width, height, ball, p1, p2, font):
	screen.fill(color1)  # screen color
	pygame.draw.rect(screen, color2, p1.rect)  # player1
	pygame.draw.rect(screen, color2, p2.rect)  # player2
	pygame.draw.aaline(screen, color2, (width // 2, 0), (width // 2, height))  # midfield
	pygame.draw.ellipse(screen, color2, ball)  # ball
	# score
	score_player1 = font.render(f"{p1.score}", True, color2)
	score_player2 = font.render(f"{p2.score} ", True, color2)
	screen.blit(score_player1, (200, 30))
	screen.blit(score_player2, (600, 30))


def key_movements(p1, p2):
	keys = pygame.key.get_pressed()
	# player1
	if keys[pygame.K_w]:
		p1.move_up()
	if keys[pygame.K_s]:
		p1.move_down()
	# player2
	if keys[pygame.K_UP]:
		p2.move_up()
	if keys[pygame.K_DOWN]:
		p2.move_down()


def menu(screen, width, height, color1, color2):
	pygame.display.set_caption("Menu")

	menu_title = pygame.font.Font('assets/font.ttf', 100)
	title = menu_title.render("PONG", True, "#b68f40")
	background = pygame.image.load('assets/background.png')
	menu_button = pygame.font.Font('assets/font.ttf', 30)
	button = pygame.image.load("assets/button.png").convert_alpha()

	while True:
		screen.blit(background, (0, 0))
		menu_rect = title.get_rect(center=(width // 2, height // 4))
		mouse_pos = pygame.mouse.get_pos()
		# 1 PLAYER MODE BUTTON
		button1 = menu_button.render("1 PLAYER MODE", True, "#d7fcd4")
		button1_rect = button1.get_rect(center=(width // 2, height // 1.7))
		if button1_rect.collidepoint(mouse_pos):
			button1 = menu_button.render("1 PLAYER MODE", True, color2)
		else:
			button1 = menu_button.render("1 PLAYER MODE", True, "#d7fcd4")
		# 2 PLAYERS MODE BUTTON
		button2 = menu_button.render("2 PLAYERS MODE", True, "#d7fcd4")
		button2_rect = button2.get_rect(center=(width // 2, height // 1.3))
		if button2_rect.collidepoint(mouse_pos):
			button2 = menu_button.render("2 PLAYERS MODE", True, color2)
		else:
			button2 = menu_button.render("2 PLAYERS MODE", True, "#d7fcd4")

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				click_pos = pygame.mouse.get_pos()
				if button1_rect.collidepoint(click_pos):
					main_game(screen, width, height, color1, color2)

		screen.blit(title, menu_rect)
		screen.blit(button1, button1_rect)
		screen.blit(button2, button2_rect)
		pygame.display.update()


def main_game(screen, screen_width, screen_height, black, white):
	# players
	speed = 10
	x_p1 = 50
	x_p2 = screen_width - 60
	y_player = (screen_height - 100) // 2
	w_player = 10
	h_player = 70
	player1 = Player(x_p1, y_player, speed, w_player, h_player)
	player2 = Player(x_p2, y_player, speed, w_player, h_player)

	# ball
	b_radius = 15
	b_x_speed = 5.0
	b_y_speed = 5.0
	ball_x = screen_width // 2 - b_radius
	ball_y = screen_height // 2 - b_radius
	ball = Ball(b_radius, ball_x, ball_y, b_x_speed, b_y_speed, screen_width, screen_height)

	frames_per_second = pygame.time.Clock()
	font = pygame.font.Font('assets/font.ttf', 72)
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		draw_on_screen(screen, black, white, screen_width, screen_height, ball, player1, player2, font)
		key_movements(player1, player2)
		ball.movement()
		ball.collision(player1, player2)
		pygame.display.flip()
		frames_per_second.tick(60)


def main():
	pygame.init()
	screen_width = 800
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Pong')
	white = (255, 255, 255)
	black = (0, 0, 0)
	menu(screen, screen_width, screen_height, black, white)


if __name__ == "__main__":
	main()
