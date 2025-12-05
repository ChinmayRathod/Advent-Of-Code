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