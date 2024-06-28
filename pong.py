import pygame
from player import Player
import sys


def main():
	pygame.init()
	width = 800
	height = 600
	white = (255, 255, 255)
	black = (0, 0, 0)
	screen = pygame.display.set_mode((width, height))
	pygame.display.set_caption('Pong')
	player1 = Player(10, (height - 100) // 2, 10, 10, 100)
	player2 = Player(width - 20, (height - 100) // 2, 10, 10, 100)
	pong_game = True
	while pong_game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		screen.fill(black)
		pygame.draw.rect(screen, white, player1.rect)
		pygame.draw.rect(screen, white, player2.rect)
		pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))
		pygame.display.flip()


if __name__ == "__main__":
	main()
