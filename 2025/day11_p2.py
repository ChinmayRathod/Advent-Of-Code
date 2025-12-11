def part2(key, visitDAC, visitFFT):
    global ans
    visitDAC = visitDAC or (key == "dac")
    visitFFT = visitFFT or (key == "fft")
    mpkey = (key, visitDAC, visitFFT)
    if mpkey in mp:
        return mp[mpkey]
    if key == "out":
        mp[mpkey] = 1 if (visitDAC and visitFFT) else 0
        return mp[mpkey]
    count = 0
    for val in graph[key]:
        count += part2(val, visitDAC, visitFFT)
    mp[mpkey] = count
    return count

graph = {}
with open("input.txt","r") as f:
    for line in f:
        if ":" in line:
            k,v = line.split(":")
            graph[k.strip()] = v.strip().split()

mp = {}
ans = part2("svr", False, False)
print(ans)
