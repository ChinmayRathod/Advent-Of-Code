def day9():
    data = []
    part2 = 0

    with open("input.txt") as f:
        data = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]
    
    def valid_points(points):
        valid_x = set()
        valid_y = set()
        points_x = set()
        points_y = set()
        for x, y in points:
            if x in valid_x:
                continue
            elif x in points_x:
                valid_x.add(x)
            else:
                points_x.add(x)
            if y in valid_y:
                continue
            elif y in points_y:
                valid_y.add(y)
            else:
                points_y.add(y)
        return valid_x, valid_y
    
    def fill_red_grid(points, valid_x, valid_y):
        max_x = max(x for x in valid_x)
        max_y = max(y for y in valid_y)
        grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        red_points = []
        for x, y in points:
            if x in valid_x and y in valid_y:
                grid[y][x] = 'R'
                red_points.append((x, y))
        return red_points, grid
    
    def fill_green(grid):
        for x in range(len(grid[0])):
            found_red = False
            red_index = -1
            for y in range(len(grid)):
                if grid[y][x] == 'R':
                    if found_red:
                        for fill_y in range(red_index + 1, y):
                            grid[fill_y][x] = 'G'
                        found_red = False
                    else:
                        found_red = True
                    red_index = y
                elif found_red:
                    grid[y][x] = 'G'
        for y in range(len(grid)):
            found_red = False
            red_index = -1
            for x in range(len(grid[0])):
                if grid[y][x] == 'R':
                    if found_red:
                        for fill_x in range(red_index + 1, x):
                            grid[y][fill_x] = 'G'
                        found_red = False
                    else:
                        found_red = True
                    red_index = x
                elif found_red:
                    grid[y][x] = 'G'
        for x in range(len(grid[0])):
            found_green = False
            green_index = -1
            for y in range(len(grid)):
                if grid[y][x] == 'R':
                    continue
                elif grid[y][x] == 'G':
                    if found_green:
                        for fill_y in range(green_index + 1, y):
                            if(grid[fill_y][x] == 'R'):
                                continue
                            else:
                                grid[fill_y][x] = 'G'
                        found_green = False
                    else:
                        found_green = True
                    green_index = y
        return grid

    def calculate_area(grid, red_points):
        max_area = 0
        for x1, y1 in red_points:
            for x2, y2 in red_points:
                if x2 < x1 or y2 < y1:
                    continue
                area = 0
                valid = True
                for fill_y in range(y1, y2 + 1):
                    for fill_x in range(x1, x2 + 1):
                        if grid[fill_y][fill_x] == '.':
                            valid = False
                            break
                        area += 1
                    if not valid:
                        break
                if valid:
                    max_area = max(max_area, area)
        return max_area
    
    def compute(points):
        valid_x, valid_y = valid_points(points)
        red_points, grid = fill_red_grid(points, valid_x, valid_y)
        fill_green(grid)
        return calculate_area(grid, red_points)

    part2 = compute(data)
    return part1, part2


if __name__ == "__main__":
    data = []
    part1 = 0  
    part2 = 0

    with open("input.txt") as f:
        data = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]
    for x1,y1 in data:
        for x2,y2 in data:
            area = abs(x1 - x2 + 1)*abs(y1 - y2 + 1)
            part1 = max(part1, area)
    print("Part 1:", part1)
    print(day9())
