import Sudoku_solver

def main():
    main_grid = [[[5, 3, 0], [6, 0, 0], [0, 9, 8]], [[0, 7, 0], [1, 9, 5], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 6, 0]],
                       [[8, 0, 0], [4, 0, 0], [7, 0, 0]], [[0, 6, 0], [8, 0, 3], [0, 2, 0]],[[0, 0, 3], [0, 0, 1], [0, 0, 6]],
                       [[0, 6, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [4, 1, 9], [0, 8, 0]],[[2, 8, 0], [0, 0, 5], [0, 7, 9]]]

    grids_with_used_numbers = Sudoku_solver.get_used_numbers_from_multiple_mini_grids(main_grid)
    set_of_number_choices = Sudoku_solver.get_list_of_number_choices(grids_with_used_numbers)
    final_grid = Sudoku_solver.choose_remove_numbers_in_multiple_grids(grids_with_used_numbers)
    Sudoku_solver.display_grid_in_sudoku_format(final_grid)
    return final_grid

main()