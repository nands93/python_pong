import pygame
from player import Player
from ball import Ball
import sys


def draw_on_screen(screen, color1, color2, width, height, ball, p1, p2):
	screen.fill(color1)
	pygame.draw.rect(screen, color2, p1.rect)
	pygame.draw.rect(screen, color2, p2.rect)
	pygame.draw.rect(screen, color2, pygame.Rect(10, 10, width - 20, height - 20), 10)
	pygame.draw.aaline(screen, color2, (width // 2, 10), (width // 2, height - 15))
	pygame.draw.ellipse(screen, color2, ball)


def key_movements(p1, p2):
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		p1.move_up()
	if keys[pygame.K_s]:
		p1.move_down()
	if keys[pygame.K_UP]:
		p2.move_up()
	if keys[pygame.K_DOWN]:
		p2.move_down()


def main():
	pygame.init()
	screen_width = 800
	screen_height = 600
	screen = pygame.display.set_mode((screen_width, screen_height))
	pygame.display.set_caption('Pong')

	white = (255, 255, 255)
	black = (0, 0, 0)

	# players
	speed = 10
	x_p1 = 30
	x_p2 = screen_width - 40
	y_player = (screen_height - 100) // 2
	w_player = 10
	h_player = 100
	player1 = Player(x_p1, y_player, speed, w_player, h_player)
	player2 = Player(x_p2, y_player, speed, w_player, h_player)

	# ball
	b_size = 10
	b_x_speed = 7.5
	b_y_speed = 7.5
	ball = Ball(b_size, b_x_speed, b_y_speed, screen_width, screen_height)

	frames_per_second = pygame.time.Clock()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		draw_on_screen(screen, black, white, screen_width, screen_height, ball, player1, player2)
		key_movements(player1, player2)
		ball.movement()
		ball.collision(player1, player2)
		pygame.display.update()
		frames_per_second.tick(60)


if __name__ == "__main__":
	main()
