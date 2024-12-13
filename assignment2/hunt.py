# GEO1000 - Assignment 2
# Authors: Xinya Bi, Xu Wang
# Studentnumbers:6195350, 6235379

def read_grid(filenm):
    """
        Make a fruitful function read grid that returns a datastructure that can be used by the visit function.
        The datastructure has to be a list of lists.
        Every sublist represents a row in the table and contains for every cell a tuple with (row, col)-indexes, where the indexes are integers.
    """
    with open(filenm, 'r') as f:
        # drop redundant decorative lines
        lines = [line.strip() for line in f if '+----+----+----+----+----+' not in line]


    # extract numbers
    grid = []
    for line in lines:
        rows = line.lstrip('| ').rstrip(' |').split(' | ')
        # transform into tuples
        row_tuples = []
        for num in rows:
            num = int(num)
            row = num // 10
            col = num % 10
            row_tuples.append((row, col))
        grid.append(row_tuples)


    return grid


def visit(table, steps_allowed, path):
    """
        Make an iterative fruitful function visit that takes table (the nested list returned by read grid), steps allowed, and path as input.
        This function appends the cells, i.e. the (row, col)-tuples, it traverses throughout to the path list. Note that this works because lists are mutable objects.
        The parameter steps allowed gives the maximum steps for the search.
        The function should return a boolean value based on whether-or-not the treasure was found.
    """
    # set initial start point
    current_pos = (0, 0)
    path.append(current_pos)

    for i in range(steps_allowed):
        # search for next pos and append it to the path
        row, col = current_pos
        next_pos = table[row][col]

        # find treasure
        if (row, col) == next_pos:
            return True

        # append the next position to path
        path.append(next_pos)

        # reset the current pos
        current_pos = next_pos


    # return false if steps allowed = 0 and failed to find treasure
    return False



def hunt(filenm, max_steps):
    # read the input file and store the content into a nested list
    grid_table = read_grid(filenm)

    # find treasure
    path_exp = []
    visit_result = visit(grid_table, max_steps, path_exp)

    # output result
    if visit_result:
        treasure_pos = path_exp[-1]
        total_step = len(path_exp)
        return f"The treasure was found at row: {treasure_pos[0]}, column: {treasure_pos[1]}; it took {total_step} steps to find the treasure."
    else:
        return f"Could not find a treasure in {max_steps} steps"


if __name__ == "__main__":
    print(hunt('finite.txt', 20))
