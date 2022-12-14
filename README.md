# cse210-06

Conway's Game of Life.
Version 1.3

## Overview

The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.
[https://en.wikipedia.org/wiki/Conway's_Game_of_Life]

## Rules

The Rules for the Game of Life are defined here [https://en.wikipedia.org/wiki/Conway's_Game_of_Life].

This implementation starts off with an inital pattern and runs. The player can press the 'p' key to pause the game and make changes. The player can use the arrow keys to move the cursor left, down, right, and up respectively. Pressing the 'j', 'k', 'l', and 'i' keys will move the cursor one cell at a time. Pressing the 's' key will set a cell and pressing the 'x' key will clear a cell. Pressing the 'c' key will clear all cells. When the player is ready for the game to start, they can hit the 'Enter' key. Generations will then proceed, calculating new worlds based on the rules of the Game of Life as oulined above. At any time, the player can pause the game by hitting the 'p' key and then use the cursor control keys to make any additional changes to the current world. The player can resume by hitting the 'Enter' key again. Pressing the 'h' key will display help text.

## Getting Started

Make sure you have Python 3.8 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.

```
python3 -m pip install raylib
```

After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.

```
python3 life
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the life folder and click the "run" icon.

## Project Structure

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- life               (source code for game)
  +-- game              (specific game classes)
  +-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Design

* Director is created with video and keyboard services.
  * Game starts up, creates actors and actions. 
  * LIfe and Player classes are added to Cast.
  * Actions are added to Script
  * Initialize actions are executed before main loop.
    * ResetWorldAction: initializes all of the variables. This action is executed before the primary loop is executed.
    * DrawWorldAction is executed to setup the primary screen.
  * Main loop is started.
    * ControlCursorAction: Gets the cursor and other input from player.
    * MoveCursorAction: Moves the cursor and perform other player directed input.
    * GenerateNewWorld: Scans the world grid and generates the new world.
    * DrawWorldAction: Draws the world to video.


## Required Technologies

* Python 3.8
* Raylib Python CFFI 3.7

## Authors

* M. Scott Reynolds rey22006 at byui.edu

## FAQ

Q. What is polymorphism and why is it important?   
A. Polymorphism in programming is the ability to have a method's behavior change depending on the programming context. A parent class can define a method that behaves in a certain or default way. Child classes of that parent class can override that same method, by defining a method with the same name and parameters and changing its behavior. This is important because it allows placing common methods and attributes in a single parent class and then having the child classes only implement the different behavior of a particular method. This can greatly simplify programming by reducing the need to define identical methods in multiple child classes.

Q. How did you apply polymorphism in your program's design?   
A. Polymorphism is used in the Action class and its child classes. The execute_action() method doesn't do anything in the base Action class and must be further defined in each child class. The child class will override the execute_action() method to perform whatever it is the child class is designed to do. For example, a child class could be designed to draw the current state of the game. Another child class can get the users input. And another class can take the users input and update the state and scores of the game.

Q. How did you ensure maintainability in your program's design?  
A. Polymorphism is used at the director level so the director only knows the type of action that needs to be executed, not the specific action itself. Actions listed by type will be called and then execute the actuall code specific to the game. Having actions called by type of function also allows for easier modification to the game later on. Parts of the game compoments are encapsulated in class, a World class that contains the cell grids, and a Player class that contains player specific information and actions. Comments are liberally applied to make sure it is easy to understand logic in later years for maintainability. 
