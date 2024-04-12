from unittest import TestCase
from sudoku_solver import SudokuSolver
import math

class SudokuSolverStudentTests(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def _assert_puzzle(self, result, answer):
        for i in range(len(answer)):
            for j in range(len(answer)):
                self.assertEqual(result[i][j],  answer[i][j])

    def test_solve1(self):
        puzzle = [["A", "B", "C", None],
                 ["C", None, "A", "B"],
                 [None, "A", "D", None],
                 ["D", None, None, "A"]]

        answer = [["A", "B", "C", "D"],
                 ["C", "D", "A", "B"],
                 ["B", "A", "D", "C"],
                 ["D", "C", "B", "A"]]

        solver = SudokuSolver(["A", "B", "C", "D"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)
    
    def test_solve2(self):
        puzzle = [["N","F","G","R","P","W","L","T","S"],
             ["L","W","S","N","T","F","R","P","G"],
             ["P","T","R","S","G","L","F","N","W"],
             ["T","S","W","F","R","G","N","L","P"],
             ["R","G","P","L","N","S","T","W","F"],
             ["F","L","N","T","W","P","S","G","R"],
             ["G",None,None,None,"L","T","P",None,None],
             [None,None,None,"P",None,None,None,"F","L"],
             [None,"P","L",None,None,None,"W",None,"T"]]

        answer = [['N', 'F', 'G', 'R', 'P', 'W', 'L', 'T', 'S'], 
            ['L', 'W', 'S', 'N', 'T', 'F', 'R', 'P', 'G'], 
            ['P', 'T', 'R', 'S', 'G', 'L', 'F', 'N', 'W'], 
            ['T', 'S', 'W', 'F', 'R', 'G', 'N', 'L', 'P'], 
            ['R', 'G', 'P', 'L', 'N', 'S', 'T', 'W', 'F'], 
            ['F', 'L', 'N', 'T', 'W', 'P', 'S', 'G', 'R'], 
            ['G', 'R', 'F', 'W', 'L', 'T', 'P', 'S', 'N'], 
            ['W', 'N', 'T', 'P', 'S', 'R', 'G', 'F', 'L'], 
            ['S', 'P', 'L', 'G', 'F', 'N', 'W', 'R', 'T']]
        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        result = solver.solve(puzzle)
        self._assert_puzzle(result, answer)
        
    def test_find_lowest1(self):
        solver = SudokuSolver(["W", "L", "F", "S", "T", "R", "N", "G", "P"])
        exdict = {(0, 0): ["W", "L", "F"], (1, 1): ["W", "L"]}
        self.assertEqual(
            solver.find_lowest_cell(exdict),

        ((1, 1), ["W", "L"]))