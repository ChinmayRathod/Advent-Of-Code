
def compute(num, n):
    sum = 0
    on = num[-n:]
    for i in range(len(num) - n - 1, -1, -1):
        for j in range(len(on)):
            if num[i] >= on[j]:
                num[i], on[j] = on[j], num[i]
            else: 
                break
    for i in range(len(on)):
        sum = sum * 10 + on[i]
    return sum

def day3():
    part1 = 0
    part2 = 0
    for line in open('input.txt').readlines():
        line = line.strip()
        num = [int(x) for x in line]
        num2 = num.copy()
        part1 += compute(num, 2)
        part2 += compute(num2, 12)
    return part1, part2


if __name__ == '__main__':
    print(day3())   