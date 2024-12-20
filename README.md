# Minesweeper Automation Project

This project aims to create an automated solution for the classic Minesweeper game. The program captures the screen, analyzes the game board, and makes optimal moves to solve the game as efficiently as possible.

## Features
- **Screen Capture**: Captures the Minesweeper game screen to extract cell information.
- **Game Analysis**: Analyzes the game board and determines which cells are mines and which are safe.
- **Automated Clicks**: Simulates mouse clicks to interact with the game board and make decisions in real-time.

## Installation
To run this project, you need Python installed along with a few necessary packages. You can install the required packages using:

```sh
pip install -r requirements.txt
```

## Usage
1. Start the Minesweeper game.
2. Run the program:
   ```sh
   python main.py
   ```
3. Watch as the program automatically plays Minesweeper for you!

## Project Structure
- **minesweeper/screen.py**: Handles screen capture and image processing.
- **minesweeper/strategy.py**: Contains the game logic and decision-making algorithms.
- **minesweeper/play.py**: Interacts with the game by simulating mouse clicks.
- **main.py**: Entry point of the program.

## To-Do
- Improve image recognition for better accuracy.
- Implement different difficulty strategies.

## Contributions
Feel free to open issues or pull requests if you want to contribute!

## License
This project is open-source and licensed under the MIT License.

