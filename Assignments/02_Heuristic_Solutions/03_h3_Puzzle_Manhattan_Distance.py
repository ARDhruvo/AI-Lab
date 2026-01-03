# KB - Goal Positions (piece, y, x)
gtp = {
    1: (1, 1),
    2: (1, 2),
    3: (1, 3),
    4: (2, 3),
    5: (3, 3),
    6: (3, 2),
    7: (3, 1),
    8: (2, 1),
}
gblnk = (2, 2)  # Blank position

# Current Positions
tp = {
    1: (1, 2),
    2: (1, 3),
    3: (2, 1),
    4: (2, 3),
    5: (3, 3),
    6: (2, 2),
    7: (3, 2),
    8: (1, 1),
}
blnk = (3, 1)  # Blank position


def dist(t):
    """Calculate Manhattan distance for tile t"""
    a, b = tp[t]  # current position
    c, d = gtp[t]  # goal position
    return abs(a - c) + abs(b - d)


def sum_list(lst):
    """Sum elements in list"""
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


def calc_h(start, result):
    """Calculate distances for tiles start through 8"""
    if start > 8:
        return result
    d = dist(start)
    result.append(d)
    return calc_h(start + 1, result)


def go():
    """Main function"""
    distances = calc_h(1, [])
    v = sum_list(distances)
    print(f"Heuristics: {v}")
    return v


# Alternative iterative version (easier to understand)
def manhattan_distance():
    """Calculate total Manhattan distance for all tiles"""
    total = 0
    for tile in range(1, 9):
        curr_y, curr_x = tp[tile]
        goal_y, goal_x = gtp[tile]
        total += abs(curr_y - goal_y) + abs(curr_x - goal_x)
    return total


# Run the program
if __name__ == "__main__":
    print("Method 1 (recursive like Prolog):")
    result1 = go()

    print("\nMethod 2 (iterative):")
    result2 = manhattan_distance()
    print(f"Heuristics: {result2}")

    # Test with user input (optional)
    print("\nWould you like to test with custom positions? (y/n)")
    if input().lower() == "y":
        print("Enter tile positions as: tile_num y x (one per line, 'done' to finish)")
        custom_tp = tp.copy()
        while True:
            line = input().strip()
            if line.lower() == "done":
                break
            try:
                tile, y, x = map(int, line.split())
                custom_tp[tile] = (y, x)
            except:
                print("Invalid input. Use: tile_num y x")

        # Calculate for custom positions
        total = 0
        for tile in range(1, 9):
            curr_y, curr_x = custom_tp[tile]
            goal_y, goal_x = gtp[tile]
            total += abs(curr_y - goal_y) + abs(curr_x - goal_x)
        print(f"Custom heuristic: {total}")
