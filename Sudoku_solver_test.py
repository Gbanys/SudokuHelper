import unittest
import Sudoku_solver

class MyTestCase(unittest.TestCase):


    def test_get_used_numbers_from_mini_grid(self):
        test_grid = [[5, 3, 0], [6, 0, 0], [0, 9, 8]]
        result_set = Sudoku_solver.get_used_numbers_from_mini_grid(test_grid)
        test_result_set = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])]
        assert result_set == test_result_set


    def test_get_used_numbers_from_multiple_mini_grids(self):
        test_mini_grids = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], [[0, 7, 0], [1, 9, 5], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 6, 0]],
                           [[8, 0, 0], [4, 0, 0], [7, 0, 0]], [[0, 6, 0], [8, 0, 3], [0, 2, 0]], [[0, 0, 3], [0, 0, 1], [0, 0, 6]],
                           [[0, 6, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [4, 1, 9], [0, 8, 0]], [[2, 8, 0], [0, 0, 5], [0, 7, 9]]]

        test_result_mini_grids = [[[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])],
                                  [[[0, 7, 0], [1, 9, 5], [0, 0, 0]], set([0, 1, 5, 7, 9])],
                                  [[[0, 0, 0], [0, 0, 0], [0, 6, 0]], set([0, 6])],
                                  [[[8, 0, 0], [4, 0, 0], [7, 0, 0]], set([0, 4, 7, 8])],
                                  [[[0, 6, 0], [8, 0, 3], [0, 2, 0]], set([0, 2, 3, 6, 8])],
                                  [[[0, 0, 3], [0, 0, 1], [0, 0, 6]], set([0, 1, 3, 6])],
                                  [[[0, 6, 0], [0, 0, 0], [0, 0, 0]], set([0, 6])],
                                  [[[0, 0, 0], [4, 1, 9], [0, 8, 0]], set([0, 1, 4, 8, 9])],
                                  [[[2, 8, 0], [0, 0, 5], [0, 7, 9]], set([0, 2, 5, 7, 8, 9])]]

        result_mini_grids = Sudoku_solver.get_used_numbers_from_multiple_mini_grids(test_mini_grids)
        assert test_result_mini_grids == result_mini_grids

    def test_get_list_of_number_choices(self):
        test_mini_grid = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])]
        test_result_set = set([1, 2, 4, 7])
        assert test_result_set == Sudoku_solver.get_list_of_number_choices(test_mini_grid)

    def test_choose_remove_number_in_set(self):
        test_mini_grid = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])]
        number_choice = 1
        result_mini_grid = [[[5, 3, 1], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9, 1])]
        number_choices = Sudoku_solver.choose_remove_number_in_set(test_mini_grid)
        assert result_mini_grid == number_choices[0]
        assert number_choice == number_choices[1]

    def test_choose_remove_multiple_numbers_in_grid(self):
        test_mini_grid = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])]
        test_result_mini_grid = [[[5, 3, 1], [6, 2, 4], [7, 9, 8]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]
        result_grid = Sudoku_solver.choose_remove_multiple_numbers_in_grid(test_mini_grid)
        assert 0 not in result_grid[0]
        assert len(result_grid[1]) == 10
        assert result_grid == test_result_mini_grid

    def test_choose_remove_numbers_in_multiple_grids(self):
        test_mini_grids = [[[[5, 3, 0], [6, 0, 0], [0, 9, 8]], set([0, 3, 5, 6, 8, 9])],
                                  [[[0, 7, 0], [1, 9, 5], [0, 0, 0]], set([0, 1, 5, 7, 9])],
                                  [[[0, 0, 0], [0, 0, 0], [0, 6, 0]], set([0, 6])],
                                  [[[8, 0, 0], [4, 0, 0], [7, 0, 0]], set([0, 4, 7, 8])],
                                  [[[0, 6, 0], [8, 0, 3], [0, 2, 0]], set([0, 2, 3, 6, 8])],
                                  [[[0, 0, 3], [0, 0, 1], [0, 0, 6]], set([0, 1, 3, 6])],
                                  [[[0, 6, 0], [0, 0, 0], [0, 0, 0]], set([0, 6])],
                                  [[[0, 0, 0], [4, 1, 9], [0, 8, 0]], set([0, 1, 4, 8, 9])],
                                  [[[2, 8, 0], [0, 0, 5], [0, 7, 9]], set([0, 2, 5, 7, 8, 9])]]

        test_result_mini_grids = [[[[5, 3, 1], [6, 2, 4], [7, 9, 8]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[2, 7, 3], [1, 9, 5], [4, 6, 8]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[1, 2, 3], [4, 5, 7], [8, 6, 9]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[8, 1, 2], [4, 3, 5], [7, 6, 9]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[1, 6, 4], [8, 5, 3], [7, 2, 9]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[2, 4, 3], [5, 7, 1], [8, 9, 6]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[1, 6, 2], [3, 4, 5], [7, 8, 9]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[2, 3, 5], [4, 1, 9], [6, 8, 7]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])],
                                  [[[2, 8, 1], [3, 4, 5], [6, 7, 9]], set([0, 1, 2 ,3, 4, 5, 6, 7, 8, 9])]]

        result_mini_grids = Sudoku_solver.choose_remove_numbers_in_multiple_grids(test_mini_grids)
        assert test_result_mini_grids == result_mini_grids

    def test_main(self):
        test_result_mini_grids = [[[[5, 3, 1], [6, 2, 4], [7, 9, 8]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[2, 7, 3], [1, 9, 5], [4, 6, 8]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[1, 2, 3], [4, 5, 7], [8, 6, 9]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[8, 1, 2], [4, 3, 5], [7, 6, 9]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[1, 6, 4], [8, 5, 3], [7, 2, 9]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[2, 4, 3], [5, 7, 1], [8, 9, 6]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[1, 6, 2], [3, 4, 5], [7, 8, 9]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[2, 3, 5], [4, 1, 9], [6, 8, 7]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])],
                                    [[[2, 8, 1], [3, 4, 5], [6, 7, 9]], set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])]]

        actual_mini_grids = Sudoku_solver.main()
        assert test_result_mini_grids == actual_mini_grids

if __name__ == '__main__':
    unittest.main()
