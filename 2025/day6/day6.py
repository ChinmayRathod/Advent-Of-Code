def day6():
    part1 = 0
    part2 = 0
    rows = []

    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            parsed = [str(p) if p.isdigit() else p for p in parts]
            rows.append(parsed)
    for i in range(len(rows[0])):
        sum = 0
        if(rows[len(rows)-1][i] == "*"):
            sum = 1
        for j in range(len(rows)-1):
            num = int(rows[j][i])
            if(rows[len(rows)-1][i] == "+"):
                sum += num
            elif(rows[len(rows)-1][i] == "*"):
                sum *= num
        part1 += sum
    return part1, part2


def part2(filename="input.txt"):
    # Read & normalize input
    with open(filename) as f:
        lines = [line.rstrip("\n") for line in f]

    max_w = max(len(line) for line in lines)
    grid = [line.ljust(max_w) for line in lines]

    h = len(grid)
    w = max_w

    problems = []
    current = []

    def finish():
        nonlocal current
        if current:
            problems.append(current)
            current = []

    # Scan columns from right to left
    for col in reversed(range(w)):
        col_vals = [grid[row][col] for row in range(h)]

        # Separator column = all spaces
        if all(c == " " for c in col_vals):
            finish()
        else:
            current.append(col_vals)

    finish()

    total = 0

    for prob in problems:
        # Extract operator from bottom row of any column
        op = None
        for col in prob:
            if col[-1] in "+*":
                op = col[-1]
                break

        # Build numbers from each column except operator row
        numbers = []
        for col in prob:
            digits = "".join(c for c in col[:-1] if c.isdigit())
            if digits:
                numbers.append(int(digits))

        # Apply operator
        if op == "+":
            result = sum(numbers)
        else:
            result = 1
            for n in numbers:
                result *= n

        total += result

    return total


if __name__ == '__main__':
    print(day6()) 
    print(part2())

