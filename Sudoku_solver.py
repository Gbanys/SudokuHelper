

def get_used_numbers_from_mini_grid(mini_grid: list):
    numbers_already_used = set()
    for row in mini_grid:
        for number in row:
            numbers_already_used.add(number)
    new_list = [mini_grid, numbers_already_used]
    return new_list


def get_used_numbers_from_multiple_mini_grids(mini_grids: list):
    new_list = []
    for mini_grid in mini_grids:
        new_list.append(get_used_numbers_from_mini_grid(mini_grid))
    return new_list


def get_list_of_number_choices(mini_grid: list):
    set_of_number_choices = set()
    for number in range(0, 10):
        if number not in mini_grid[1]:
            set_of_number_choices.add(number)
    return set_of_number_choices


def choose_remove_number_in_set(mini_grid: list):
    number_choice = 0
    for number in range(0, 10):
        if number not in mini_grid[1]:
            number_choice = number
            mini_grid[1].add(number)
            break
    for row in range(0, 3):
        for column in range(0, 3):
            if mini_grid[0][row][column] == 0:
                mini_grid[0][row][column] = number
                break
        break
    return [mini_grid, number_choice]


def choose_remove_multiple_numbers_in_grid(mini_grid: list):
    for row_index in range(0, 3):
        for number_index in range(0, 3):
            if mini_grid[0][row_index][number_index] == 0:
                [mini_grid, chosen_number] = choose_remove_number_in_set(mini_grid)
                mini_grid[0][row_index][number_index] = chosen_number
    return mini_grid


def choose_remove_numbers_in_multiple_grids(mini_grids: list):
    for grid_number in range(0, len(mini_grids)):
        mini_grids[grid_number] = choose_remove_multiple_numbers_in_grid(mini_grids[grid_number])
    return mini_grids


def display_grid_in_sudoku_format(grid: list):
    mini_grid_row = 0
    for large_grid_row in range(0, 3):
        mini_grid_row = mini_grid_row + 3
        for column_number in range(0, 3):
            row = []
            for row_number in range(mini_grid_row - 3, mini_grid_row):
                row.append(list(grid[row_number][0][column_number]))
            print(row)
        print("")
    return

