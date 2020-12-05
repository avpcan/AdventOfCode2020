def count_trees_in_path(filename, delta_x, delta_y):
    """Counts how many trees a sledder would hit for a given slope on a given map.

    Args:
        filename (str): The file from which to read the terrain map
        delta_x (int): The x-component of the slope of the sled's path
        delta_y (int): The y-component of the slope of the sled's path

    Returns:
        int: The number of trees that a sledder would encounter on the given run
    """
    terrain_file = open(filename, "r")
    x_pos = 0
    y_pos = 0
    num_trees = 0
    first = True

    for terrain_slice in terrain_file:
        terrain_slice = terrain_slice.rstrip("\n")
        if first:
            # We don't check for trees at the starting location,
            # but let's take this time to determine the length of the terrain.
            map_length = len(terrain_slice)
            first = False
            y_pos += 1
            continue
        if y_pos % delta_y == 0:
            # Count any trees that we "hit" along the way
            x_pos = (x_pos + delta_x) % map_length
            if terrain_slice[x_pos] == "#":
                num_trees += 1
        y_pos += 1

    return num_trees


if __name__ == "__main__":
    terrain_filename = "terrain.txt"
    # terrain_filename = "test-terrain.txt"

    # Part 1
    # Slope = right 3, down 1
    num_trees_3_1 = count_trees_in_path(terrain_filename, 3, 1)
    print(f"You would hit {num_trees_3_1} trees if you took a 3 right, 1 down slope")

    # Part 2
    # Slope = right 1, down 1
    num_trees_1_1 = count_trees_in_path(terrain_filename, 1, 1)
    print(f"You would hit {num_trees_1_1} trees if you took a 1 right, 1 down slope")

    # Slope = right 5, down 1
    num_trees_5_1 = count_trees_in_path(terrain_filename, 5, 1)
    print(f"You would hit {num_trees_5_1} trees if you took a 5 right, 1 down slope")

    # Slope = right 7, down 1
    num_trees_7_1 = count_trees_in_path(terrain_filename, 7, 1)
    print(f"You would hit {num_trees_7_1} trees if you took a 7 right, 1 down slope")

    # Slope = right 1, down 2
    num_trees_1_2 = count_trees_in_path(terrain_filename, 1, 2)
    print(f"You would hit {num_trees_1_2} trees if you took a 1 right, 2 down slope")

    # Final puzzle answer
    puzzle_answer = (
        num_trees_3_1 * num_trees_1_1 * num_trees_5_1 * num_trees_7_1 * num_trees_1_2
    )
    print(f"The product of these values is {puzzle_answer}.")
