def bomber_man(n, grid):
    r, c = len(grid), len(grid[0])
    if n == 1:
        return grid

    # All cells filled with bombs
    if n % 2 == 0:
        return ['O' * c for i in range(r)]

    # Alternate states
    n //= 2
    for q in range((n + 1) % 2 + 1):
        newgrid = [['O'] * c for i in range(r)]

        # Function for detonation
        def set(x, y):
            if 0 <= x < r and 0 <= y < c:
                newgrid[x][y] = '.'

        xi = [0, 0, 0, 1, -1]
        yi = [0, -1, 1, 0, 0]

        for x in range(r):
            for y in range(c):
                if grid[x][y] == 'O':
                    for i, j in zip(xi, yi):
                        set(x + i, y + j)

        grid = newgrid

    # Convert result back to strings
    return ["".join(x) for x in grid]

