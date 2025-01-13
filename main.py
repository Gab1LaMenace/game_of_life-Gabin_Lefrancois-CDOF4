import os  # For clearing the console
import numpy as np
import random as random
import time

# Values that determine if the cell is alive or not
vals = [0, 1]

def create_grid(rows, cols):
    return np.random.choice(vals, rows * cols, p=[0.3, 0.8]).reshape(rows, cols)

def print_grid(rows, cols, grid, generation):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear console
    output_str = ""
    for row in range(rows):
        for col in range(cols):
            output_str += "⬛ " if grid[row][col] == 0 else "⬜ "
        output_str += "\n"  # Move to the next line after each row
    print(output_str)

def create_next_grid(rows, cols, grid, next_grid):
    for row in range(rows):
        for col in range(cols):
            live_neighbors = get_live_neighbors(row, col, rows, cols, grid)
            if live_neighbors < 2 or live_neighbors > 3:
                next_grid[row][col] = 0
            elif live_neighbors == 3 and grid[row][col] == 0:
                next_grid[row][col] = 1
            else:
                next_grid[row][col] = grid[row][col]

def get_live_neighbors(row, col, rows, cols, grid):
    life_sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life_sum += grid[(row + i) % rows][(col + j) % cols]
    return life_sum

def run_game():
    # Allow user to choose the dimensions of the grid
    rows = int(input("Enter the number of rows for the grid: "))
    cols = int(input("Enter the number of columns for the grid: "))

    current_generation = create_grid(rows, cols)
    next_generation = create_grid(rows, cols)

    generations = 100  # Limit the number of generations
    for gen in range(1, generations + 1):
        print_grid(rows, cols, current_generation, gen)
        create_next_grid(rows, cols, current_generation, next_generation)
        time.sleep(2)  # Adjust speed for readability
        current_generation, next_generation = next_generation, current_generation

    print_grid(rows, cols, current_generation, generations)
    return input("<Enter> to exit or r to run again: ")


run = "r"
while run == "r":
    out = run_game()
    run = out