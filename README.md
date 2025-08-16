# Python Pong (Pygame)

A simple Pong game built with Pygame. It features a main menu, configuration screen, single-player (AI) and two-player modes, score/round tracking, and sound effects.

- Entry point: [`pong.py`](pong.py)
- Core classes: [`player.Player`](player.py), [`player.AutoPlayer`](player.py), [`ball.Ball`](ball.py), [`button.Button`](button.py)

## Features

- Single-player mode (play against an AI) and two-player mode
- Menu and configuration screens
- Configurable match: points per round and rounds to win
- Sound effects and basic visuals

## Requirements

- Python 3.8+
- Pygame (`pip install pygame`)

## Setup

```bash
# Optional: create and activate a virtual environment
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# Install dependency
pip install pygame
```

## Run

```bash
python pong.py
```

This starts the app and opens the main menu from [`pong.menu`](pong.py). Use the mouse to select options.

## Gameplay

- 1 Player Mode: You control the left paddle; the right paddle is AI (see [`player.AutoPlayer`](player.py)).
- 2 Players Mode: Both paddles are controlled by players.

Controls:
- Player 1 (left): W (up), S (down)
- Player 2 (right): Up Arrow (up), Down Arrow (down)

## Configuration

From the configuration menu (opened via main menu), you can set:
- ROUNDS: Number of rounds needed to win the match
- POINTS: Points needed to win a round

A player wins a round upon reaching the selected points. The match ends when a player wins the selected number of rounds and the game returns to the main menu via [`pong.main`](pong.py).

## Code Overview

- Game entry and loop orchestration:
  - [`pong.main`](pong.py): Initializes Pygame, window, mixer, and opens the menu.
  - [`pong.menu`](pong.py): Main menu UI using [`button.Button`](button.py).
  - [`pong.configuration_menu`](pong.py): Lets you select ROUNDS and POINTS, then starts the game.
  - [`pong.main_game`](pong.py): Sets up paddles and ball, runs the gameplay loop.
  - [`pong.draw_on_screen`](pong.py): Renders paddles, ball, scores, rounds, and midfield line.
  - [`pong.key_movements`](pong.py): Handles keyboard input and AI movement.
  - [`pong.render_text`](pong.py): Utility to render text.

- Game objects:
  - [`player.Player`](player.py): Paddle controlled by keyboard.
  - [`player.AutoPlayer`](player.py): AI-controlled paddle with simple ball prediction.
  - [`ball.Ball`](ball.py): Ball physics and collisions:
    - [`ball.Ball.movement`](ball.py)
    - [`ball.Ball.collision`](ball.py)
    - [`ball.Ball.reset_position`](ball.py)

- UI:
  - [`button.Button`](button.py): Reusable text-button with hover sound and state.

## Assets

All assets live under [`assets/`](assets):
- Images: [`player1.png`](assets/player1.png), [`player2.png`](assets/player2.png), [`background.png`](assets/background.png), [`moon.png`](assets/moon.png)
- Fonts: [`font.ttf`](assets/font.ttf)
- Sounds: [`button.ogg`](assets/button.ogg), [`player_collision.mp3`](assets/player_collision.mp3), [`wall_collision.mp3`](assets/wall_collision.mp3), [`score.mp3`](assets/score.mp3)

Note: On case-sensitive filesystems the game uses the lowercase background file: [`assets/background.png`](assets/background.png).

## Window & Performance

- Default window size: 800x600 (see [`pong.main`](pong.py)).
- The main loop targets 60 FPS via `pygame.time.Clock()` in [`pong.main_game`](pong.py).

## Troubleshooting

- If audio initialization fails (e.g., no audio device), Pygame mixer may raise errors. As a workaround on headless systems:
  - Set an SDL audio driver (e.g., `SDL_AUDIODRIVER=dummy`) before running.
- Ensure all files in the [`assets/`](assets) directory are present and readable.

## License

No license specified.