def day5():
    part1 = 0
    part2 = 0
    ranges = []
    numbers = []
    merged_ranges = []

    with open("input.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    blank_index = lines.index('')
    range_lines = lines[:blank_index]
    number_lines = lines[blank_index+1:]

    for line in range_lines:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))
    ranges.sort(key=lambda x: x[0])

    start = ranges[0][0]
    end = ranges[0][1]
    for current_start, current_end in ranges[1:]:
        if current_start <= end:
            end = max(end, current_end)
        else:
            merged_ranges.append((start, end))
            start, end = current_start, current_end
    merged_ranges.append((start, end))

    numbers = [int(x) for x in number_lines]
    part1 = sum(any(1 for r in merged_ranges if r[0] <= num <= r[1]) for num in numbers)

    part2 = sum((r[1]-r[0]+1) for r in merged_ranges)
    return part1, part2

if __name__ == '__main__':
    print(day5())      

# crispier solution
def alternate_day5():
    with open("input.txt") as f:
        lines = [line.strip() for line in f]

    blank = lines.index('')
    ranges = sorted((tuple(map(int, line.split('-'))) for line in lines[:blank]), key=lambda x: x[0])
    numbers = list(map(int, lines[blank+1:]))

    # merge intervals
    merged = []
    start, end = ranges[0]
    for cs, ce in ranges[1:]:
        if cs <= end:
            end = max(end, ce)
        else:
            merged.append((start, end))
            start, end = cs, ce
    merged.append((start, end))

    part1 = sum(any(s <= num <= e for s, e in merged) for num in numbers)
    part2 = sum(e - s + 1 for s, e in merged)

    return part1, part2