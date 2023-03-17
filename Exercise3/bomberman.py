def bomber_man(n, grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def detonate(bombs):
        for pos in bombs:
            r, c = pos
            grid[r][c] = '.'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 'O':
                    grid[nr][nc] = '.'
                    
    def plant_bombs():
        bombs = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    grid[r][c] = 'O'
                    bombs.append((r, c))
        return bombs
    
    if n == 1:
        return grid
    
    if n % 2 == 0:
        grid = [['O'] * cols for _ in range(rows)]
        return grid
    
    bombs = plant_bombs()
    detonate(bombs)
    
    bombs = plant_bombs()
    detonate(bombs)
    
    for i in range(5, n + 1, 2):
        bombs = plant_bombs()
        detonate(bombs)
        
        bombs = plant_bombs()
        detonate(bombs)
    
    return grid