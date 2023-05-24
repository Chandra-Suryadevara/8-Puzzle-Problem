# 8 Puzzle Solver using Iterative Deepening Algorithm

This project is a Python implementation of an 8 Puzzle Solver using the Iterative Deepening Algorithm. The 8 Puzzle is a sliding puzzle consisting of a 3x3 grid with 8 numbered tiles and an empty space. The goal is to rearrange the tiles from an initial configuration to a goal configuration.

## How to Use

1. Clone or download the project repository to your local machine.
2. Ensure that you have Python installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the `main.py` file using the following command: `python main.py`.
5. The program will prompt you to input the initial configuration of the puzzle. You can either provide your own input by entering the numbers separated by spaces, or you can press Enter to use the default puzzle configuration.
6. If you choose to enter your own input, make sure to follow the correct format with 9 numbers separated by spaces. For example: `1 2 3 4 5 6 7 8 0`.
7. The program will then apply the Iterative Deepening Algorithm to solve the puzzle and display the steps taken to reach the goal configuration.
8. If a solution is found, the program will display the solution path, the number of steps taken, and the total number of nodes expanded during the search process.
9. If a solution cannot be found within a reasonable amount of time or memory, the program will display an appropriate message.

## Requirements

- Python 3.x

## Files

- `main.py`: The main Python script that implements the 8 Puzzle Solver using the Iterative Deepening Algorithm.

## References

- [Iterative Deepening Depth-First Search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
- [8 Puzzle Problem](https://en.wikipedia.org/wiki/15_puzzle)
