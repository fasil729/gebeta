# Gebeta(Ethipoan traditional board game)

## Table of Contents
- [Introduction](#introduction)
- [Technologies](#technologies)
- [What's Improved from Existing Solutions](#whats-improved-from-existing-solutions)
- [Future Considerations](#future-considerations)
- [How to Use](#how-to-use)

## Introduction
This project is an implementation of the Ethiopian traditional game called Gebeta, also known as Gabata (view the game [here](http://www.cyningstan.com/game/147/gabata)). It is similar to Mancala but with differences in the game principle. The game is implemented using Python and 2D graphics with Pygame. The project includes the following functionalities:
- Board screen and hole displays in 2D
- Interactive display of the number of pits
- Score display
- Game logic for the players
- Medium efficiency AI player using the Min-Max algorithm (medium efficiency is preferred to make the game more interactive between the player and the AI)

## Technologies
- Python
- Pygame

Algorithm:
- Medium efficiency Min-Max algorithm (preferred for increased interactivity)

## What's Improved from Existing Solutions
- Addition of an AI player that plays with a human using the Min-Max algorithm with a modified tree depth, enhancing interactivity in the game.

## Future Considerations
- Implement the game with 3D graphics.
- Add more graphical effects using OpenGL.
- Create easy, medium, and hard versions of the AI game.

## How to Use
1. Clone this repository to your local machine.
2. Open the cloned repository in an IDE like VS Code, Sublime Text, etc.
3. Run the `main.py` file to start the game
