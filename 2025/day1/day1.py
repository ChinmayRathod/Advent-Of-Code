def day1():
    part1 = 0
    part2 = 0
    curr_pos = 50
    with open('input.txt', 'r') as file:
        for line in file:
            # direction of moving
            dir = line[0]   
            num = int(line[1:])
            # circles made
            part2 += num // 100
            num = num % 100
            if dir == 'L':
                num = num*(-1)
            # crossed the boundary or not
            if curr_pos+num >= 100 or curr_pos+num <= 0:
                # if the position was zero no need to count
                if curr_pos != 0:
                    part2 += 1
            curr_pos += num
            curr_pos %= 100
            if curr_pos == 0:
                part1 += 1
    return part1, part2


if __name__ == '__main__':
    print(day1())