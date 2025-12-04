def addToMatrix( i, j, matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
            matrix[ni][nj] += 1

def subFromMatrix( i, j, matrix):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        if 0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]):
            matrix[ni][nj] -= 1

def part1Def(matrix, data):
    [addToMatrix(i, j, matrix) for i, row in enumerate(data) for j, val in enumerate(row) if val == '@']
    return sum(1 for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] < 4 and data[i][j] == '@')

def part2Def(matrix, data):
    part2 = 0
    i = 0
    while i < len(data):
        j = 0
        while j < len(data[0]):
            if data[i][j] == '@' and matrix[i][j] < 4:
                subFromMatrix(i, j, matrix)
                part2 += 1
                data[i][j] = '.'
                i = max(i - 2, 0)
                j = max(j - 2, 0)
            else:
                j += 1
        i += 1
    return part2

def day4():
    part1 = 0
    part2 = 0
    data = []
    with open('input.txt', 'r') as f:
        for line in f:
            row_str = line.strip()
            data.append([str(item) for item in row_str])
    matrix = [[0 for _ in range(len(data))] for _ in range(len(data[0]))]
    part1 = part1Def(matrix, data)
    part2 = part2Def(matrix, data)
    return part1, part2


if __name__ == '__main__':
    print(day4())   