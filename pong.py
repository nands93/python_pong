import pygame
from player import Player, AutoPlayer
from ball import Ball
from button import Button
import sys

FONT = "assets/font.ttf"
GOLDEN = "#b68f40"
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = "#d7fcd4"
game_score = 0
game_rounds = 0


def render_text(font, string, size, color):
	text = pygame.font.Font(font, size)
	rendered = text.render(string, True, color)
	return rendered


def draw_on_screen(screen, color1, color2, width, height, ball, p1, p2, font1, font2):
	screen.fill(color1)  # screen color
	screen.blit(p1.image, p1.rect)  # player1
	screen.blit(p2.image, p2.rect)  # player2
	pygame.draw.aaline(screen, color2, (width // 2, 0), (width // 2, height))  # midfield
	screen.blit(ball.image, ball.rect)
	# score
	score_player1 = font1.render(f"{p1.score}", True, color2)
	score_player2 = font1.render(f"{p2.score} ", True, color2)
	rounds_player1 = font2.render(f"{p1.rounds}", True, color2)
	rounds_player2 = font2.render(f"{p2.rounds} ", True, color2)
	screen.blit(score_player1, (200, 30))
	screen.blit(score_player2, (600, 30))
	screen.blit(rounds_player1, (220, 120))
	screen.blit(rounds_player2, (620, 120))


def key_movements(p1, p2, ball, screen_width, screen_height, mode):
	keys = pygame.key.get_pressed()
	# player1
	if keys[pygame.K_w]:
		p1.move_up()
	if keys[pygame.K_s]:
		p1.move_down()
	# player2
	if mode == 1:
		if keys[pygame.K_UP]:
			p2.move_up()
		if keys[pygame.K_DOWN]:
			p2.move_down()
	else:
		p2.movement(ball, screen_width, screen_height)


def menu(screen, width, height, color1, color2, color3):
	pygame.display.set_caption("Menu")
	title = render_text(FONT, "PONG", 100, GOLDEN)
	bg = pygame.image.load('assets/background.png')
	sound = pygame.mixer.Sound("../django_project/pong/static/pong/sound/button.ogg")

	one_player_button = Button(FONT, 25, "1 PLAYER MODE", color2, color3, width // 2, height // 2, sound)
	two_players_button = Button(FONT, 25, "2 PLAYERS MODE", color2, color3, width // 2, height // 1.7, sound)
	exit_button = Button(FONT, 25, "EXIT", color2, color3, width // 2, height // 1.35, sound)

	while True:
		screen.blit(bg, (0, 0))
		menu_rect = title.get_rect(center=(width // 2, height // 4))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				click_pos = pygame.mouse.get_pos()
				if one_player_button.rect.collidepoint(click_pos):
					configuration_menu(screen, bg, color1, color2, color3, width, height, sound, 0)
				if two_players_button.rect.collidepoint(click_pos):
					configuration_menu(screen, bg, color1, color2, color3, width, height, sound, 1)
				if exit_button.rect.collidepoint(click_pos):
					exit()
		screen.blit(title, menu_rect)
		one_player_button.button_loop(screen, mouse)
		two_players_button.button_loop(screen, mouse)
		exit_button.button_loop(screen, mouse)
		pygame.display.update()


def configuration_menu(screen, background, color1, color2, color3, width, height, sound, mode):
	global game_score, game_rounds
	pygame.display.set_caption("Configuration Menu")
	# title, back button and legend
	screen_title = render_text(FONT, "CONFIGURATION", 40, GOLDEN)
	leg_rounds = render_text(FONT, "ROUNDS", 30, GOLDEN)
	leg_points = render_text(FONT, "POINTS", 30, GOLDEN)
	font_loop = pygame.font.Font(FONT, 40)

	# numbers
	round_num = [1, 3, 5, 7, 9]
	score_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

	# buttons
	back_button = Button(FONT, 20, "< BACK", color2, color3, width // 10, height // 15, sound)
	add_button1 = Button(FONT, 20, "+", color2, color3, width // 1.7, height // 2.8, sound)
	sub_button1 = Button(FONT, 20, "-", color2, color3, width // 2.5, height // 2.8, sound)
	add_button2 = Button(FONT, 20, "+", color2, color3, width // 1.7, height // 1.8, sound)
	sub_button2 = Button(FONT, 20, "-", color2, color3, width // 2.5, height // 1.8, sound)
	save_button = Button(FONT, 40, "START", color2, color3, width // 2, height // 1.2, sound)

	# screen loop
	round_pos = 0
	score_pos = 0
	while True:
		screen.blit(background, (0, 0))
		config_rect = screen_title.get_rect(center=(width // 2, height // 6))  # title
		leg_rect1 = leg_rounds.get_rect(center=(width // 4.5, height // 2.8))  # leg_rounds
		leg_rect2 = leg_points.get_rect(center=(width // 4.5, height // 1.8))  # leg_points
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				click_pos = pygame.mouse.get_pos()
				if back_button.rect.collidepoint(click_pos):
					menu(screen, width, height, color1, color2, color3)
				if add_button1.rect.collidepoint(click_pos):
					round_pos = min(round_pos + 1, len(round_num) - 1)
				if sub_button1.rect.collidepoint(click_pos):
					round_pos = max(round_pos - 1, 0)
				if add_button2.rect.collidepoint(click_pos):
					score_pos = min(score_pos + 1, len(score_num) - 1)
				if sub_button2.rect.collidepoint(click_pos):
					score_pos = max(score_pos - 1, 0)
				if save_button.rect.collidepoint(click_pos):
					game_rounds = round_num[round_pos]
					game_score = score_num[score_pos]
					main_game(screen, width, height, color1, color2, mode)

		rounds = font_loop.render(str(round_num[round_pos]), True, GOLDEN)
		round_rect = rounds.get_rect(center=(width // 2, height // 2.8))
		score = font_loop.render(str(score_num[score_pos]), True, GOLDEN)
		points_rect = score.get_rect(center=(width // 2, height // 1.8))

		screen.blit(screen_title, config_rect)
		screen.blit(leg_rounds, leg_rect1)
		screen.blit(leg_points, leg_rect2)
		screen.blit(rounds, round_rect)
		screen.blit(score, points_rect)

		for button in [back_button, add_button1, sub_button1, add_button2, sub_button2, save_button]:
			button.button_loop(screen, mouse)

		pygame.display.update()


def main_game(screen, screen_width, screen_height, black, white, mode):
	global game_rounds, game_score
	# players
	speed = 10
	x_p1 = 40
	x_p2 = screen_width - 80
	y_player = (screen_height - 100) // 2
	w_player = 25
	h_player = 100
	p1_img = "assets/player1.png"
	p2_img = "assets/player2.png"
	player1 = Player(p1_img, x_p1, y_player, speed, w_player, h_player)
	if mode == 0:
		player2 = AutoPlayer(p2_img, x_p2, y_player, speed, w_player, h_player)
	else:
		player2 = Player(p2_img, x_p2, y_player, speed, w_player, h_player)

	# ball
	b_radius = 15
	b_x_speed = 5.0
	b_y_speed = 5.0
	ball_x = screen_width // 2 - b_radius
	ball_y = screen_height // 2 - b_radius
	ball = Ball(b_radius, ball_x, ball_y, b_x_speed, b_y_speed, screen_width, screen_height)

	frames_per_second = pygame.time.Clock()
	score_font = pygame.font.Font(FONT, 72)
	round_font = pygame.font.Font(FONT, 25)
	player_collision = pygame.mixer.Sound("assets/player_collision.mp3")
	wall_collision = pygame.mixer.Sound("assets/wall_collision.mp3")
	score_sound = pygame.mixer.Sound("assets/score.mp3")
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		draw_on_screen(screen, black, white, screen_width, screen_height, ball, player1, player2, score_font, round_font)
		key_movements(player1, player2, ball, screen_width, screen_height, mode)
		ball.movement()
		ball.collision(player1, player2, wall_collision, player_collision, score_sound, game_score)
		if player1.rounds == game_rounds or player2.rounds == game_rounds:
			main()
		pygame.display.update()
		frames_per_second.tick(60)


def main():
	global game_rounds, game_score
	pygame.init()
	pygame.font.init()
	pygame.mixer.init()
	game_score = 0
	game_rounds = 0

	screen_width = 800
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Pong')
	menu(screen, screen_width, screen_height, BLACK, WHITE, GREEN)


if __name__ == "__main__":
	main()
