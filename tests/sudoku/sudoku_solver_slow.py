from copy import deepcopy
from datetime import datetime
from typing import List, Tuple, Optional, Set
from typing import *
import math
from pprint import pprint


# Generic Sudoku Solver
# ******************************
# A sudoku puzzle is one such that given a set of unique characters, each row, column, and 
# square grid can only have 1 each character. See https://masteringsudoku.com/sudoku-rules-beginners/
# for more information on how to play.
#
# Your job is to write a solver that takes a sudoku puzzle and fills in all the characters correctly.
# Puzzles for this assignment use any characters, not just traditional numbers 1-9, and the
# size can vary/is not always 9x9 (side length will always be a square number). Spots that are not
# filled in have None in them.
#
# Tips:
# - Sets are your friend!
# - solve is a wrapper; you will need a recursive version of the solve function
# - It is worthwhile to consider what you should initialize before starting your recursive algorithm
# - If you are not sure where to start, use previous backtracking exercises for inspiration
# 
# Extensions: 
# 1) If you are backtracking in empty cell order, try optimizing the solver by finding more optimal empty 
#    cells to use for your subsequent recursive calls. See how fast you can get the 16x16 test to finish!:)
#    Uncomment the 16x16 advanced test to put things to the test (see if you can get it to run in under 10 min)
# 2) Use tkinter to put a UI around the solver, where you can type in your own puzzles to solve!
# 3) Write a Sudoku puzzle creator

class SudokuSolver:

    # Constructor
    # ************************
    # cell_options param might look like ["W", "L", "F", "S", "T", "R", "N", "G", "P"]
    # The size of the grid will always be the length of cell_options  
    def __init__(self, cell_options: List[str]) -> None:
        self.cell_options = set(cell_options) # convert cell options to a set just to have it be easier to access
        self.length = len(self.cell_options)
        self.sqrt = int(math.sqrt(self.length)) # get the square root of the length of the options - this determines the size of each smaller square inside

    
    def sort_this_dict(self, dictionary) -> List[Tuple[Any, Any]]:
        return sorted(dictionary.items(), key=lambda tup: len(tup[1]))
        

    # solve
    # *************************
    # Takes a sudoku grid with some values filled in (2D array) and returns a solution grid 
    # with all cells filled in (also a 2D array).  Empty cell values are None.
    def solve(self, grid: List[List[str]]) -> List[List[str]]:
        unused = set((y, x) for y in range(self.length) for x in range(self.length) if not grid[y][x])
        chunked = [
            [
                set( # generates a set 
                    grid[ny * self.sqrt + y][nx * self.sqrt + x] # iterates through all individual squares in a smaller square
                    for y in range(self.sqrt) # for each row in the small grid
                    for x in range(self.sqrt) # for each column in the row
                    if (ny * self.sqrt + y, nx * self.sqrt + x) not in unused
                )
                for nx in range(self.sqrt) # for each small square in a row
            ]
            for ny in range(self.sqrt) # for each row in the whole grid
        ]

        cols = [set(grid[y][x] for y in range(self.length) if (y, x) not in unused) for x in range(self.length)] # turns each column into a set
        rows = [set(grid[y][x] for x in range(self.length) if (y, x) not in unused) for y in range(self.length)] # turns each row into a set

        empty = self.sort_this_dict({
            (y, x): self.cell_options - (rows[y] | cols[x] | chunked[y // self.sqrt][x // self.sqrt])
            for y, x in unused
        })

        
        return self.solve_from(grid, empty, cols, rows, chunked, unused) # starts the recursion

    def solve_from(self, grid: List[List[str]], empty: List[Tuple[Tuple[int, int], Set[str]]], cols: List[Set[str]], rows: List[Set[str]], chunked, unused) -> Optional[List[List[str]]]:
        if not empty: # if there are no empty spots left
            return grid # return the grid
        else:
            (y, x), valid = empty[0]
            sy, sx = y // self.sqrt, x // self.sqrt
            unused.remove((y, x))
            for item in valid:
                cols[x].add(item)
                rows[y].add(item)
                
                chunked[sy][sx].add(item)
                newempty = self.sort_this_dict({
                    (ny, nx): self.cell_options - (rows[ny] | cols[nx] | chunked[ny // self.sqrt][nx // self.sqrt])
                    for ny, nx in unused
                })
                solved = self.solve_from(grid, newempty, cols, rows, chunked, unused)
                del newempty
                if solved: 
                    grid[y][x] = item
                    return solved 
                cols[x].remove(item)
                rows[y].remove(item)
                chunked[sy][sx].remove(item)
            unused.add((y, x))
            return None
