def day11(part1, key):
    if key in mp:
        return mp[key]
    count = 0
    for val in graph[key]:
        count += day11(part1, val)
    mp[key] = count
    return count

graph = {}
mp = {}
with open("input.txt", "r") as f:
    for line in f:
        if ":" not in line:
            continue
        
        key, value = line.split(":")
        key = key.strip()
        values = value.strip().split()
        graph[key] = values
part1 = 0
mp['out'] = 1 
print(day11(part1, "you"))
