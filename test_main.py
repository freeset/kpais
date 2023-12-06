import unittest
from io import StringIO
from unittest.mock import patch
from main import findSolution, createChessboard, Node, main, profile_code


class TestChessboardKnight(unittest.TestCase):

    def setUp(self):
        self.held_output = StringIO()

    def tearDown(self):
        self.held_output.close()

    def test_create_chessboard(self):
        chessboard_size = 5
        expected_chessboard = [[0] * chessboard_size for _ in range(chessboard_size)]
        self.assertEqual(createChessboard(chessboard_size), expected_chessboard)

    def test_find_solution(self):
        starting_row, starting_column, chessboard_size, max_time = 2, 2, 5, 5
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            findSolution(starting_row, starting_column, chessboard_size, max_time)
            output = mock_stdout.getvalue().strip()
        self.assertIn(f"Velkost: {chessboard_size} Zaciatocny riadok: {starting_row + 1} Zaciatocny stlpec: {starting_column + 1}", output)

    def test_profile_code(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            profile_code()
            output = mock_stdout.getvalue().strip()
        # Ensure that the output contains expected information for each call to findSolution
        self.assertIn("Velkost: 5 Zaciatocny riadok: 3 Zaciatocny stlpec: 3", output)
        self.assertIn("Velkost: 6 Zaciatocny riadok: 6 Zaciatocny stlpec: 1", output)
        # Add more assertions based on the expected output

    def test_main(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue().strip()
        # Add assertions based on the expected output

if __name__ == '__main__':
    unittest.main()
