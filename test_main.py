import unittest
from io import StringIO
from unittest.mock import patch
from main import findSolution, createChessboard


class EulerovKonTest(unittest.TestCase):

    def test_create_chessboard(self):
        chessboard_size_5 = 5
        expected_chessboard_5 = [[0] * chessboard_size_5 for _ in range(chessboard_size_5)]
        self.assertEqual(createChessboard(chessboard_size_5), expected_chessboard_5)

        chessboard_size_6 = 6
        expected_chessboard_6 = [[0] * chessboard_size_6 for _ in range(chessboard_size_6)]
        self.assertEqual(createChessboard(chessboard_size_6), expected_chessboard_6)

    def test_find_solution_outputs(self):
        test_cases = [
            (4, 0, 5, 10),
            (2, 2, 5, 10),
            (3, 2, 5, 15),
            (2, 1, 6, 15),
        ]

        for starting_row, starting_column, chessboard_size, max_time in test_cases:
            with self.subTest(starting_row=starting_row, starting_column=starting_column,
                              chessboard_size=chessboard_size, max_time=max_time):
                with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    findSolution(starting_row, starting_column, chessboard_size, max_time)
                    output = mock_stdout.getvalue().strip()

                expected_output = f"Velkost: {chessboard_size} Zaciatocny riadok: {starting_row + 1} Zaciatocny stlpec: {starting_column + 1}"
                self.assertIn(expected_output, output)

    def test_final_matrix(self):
        specific_test_case = (4, 0, 5, 10)
        expected_output_for_specific_case = [
            [3, 16, 7, 22, 5],
            [8, 21, 4, 17, 12],
            [15, 2, 11, 6, 23],
            [20, 9, 24, 13, 18],
            [1, 14, 19, 10, 25]
        ]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            findSolution(*specific_test_case)
            output = mock_stdout.getvalue().strip()

        for row, expected_row in zip((output.split('\n')[1:-1]), expected_output_for_specific_case):
            row_values = [int(value) for value in row.strip()[1:-1].split(',')]
            self.assertListEqual(row_values, expected_row)