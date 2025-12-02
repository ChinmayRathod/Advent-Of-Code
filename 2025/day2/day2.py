data =""
def day2():
    ranges = [
    tuple(map(int, part.split("-")))
    for part in data.split(",")
    ]

    part1 = 0
    part2 = 0
    for nums in ranges:
        start = nums[0]
        end = nums[1]
        for i in range(start , end+1):
            s = str(i)
            n = len(s)
            for size in range(n//2, 0, -1):
                pattern = s[:size]
                if pattern*(n//size) == s:
                    part2 += i
                    if n%2 == 0 and size == n//2:
                        part1 += i
                    break
    return part1, part2   
  
if __name__ == '__main__':
    print(day2())         