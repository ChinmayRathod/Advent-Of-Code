# The following code is made with the help of ChatGPT.# It solves a problem involving 3D points and DSU (Disjoint Set Union) operations.
# The code reads 3D points from an input file, processes them to form components using DSU,
# and computes two results based on the components formed.


def day8():
    # Read points
    with open("input.txt") as f:
        data = [tuple(map(int, line.strip().split(","))) for line in f if line.strip()]

    n = len(data)

    # DSU helpers
    parent = list(range(n))
    size = [1] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if size[ra] < size[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        size[ra] += size[rb]
        return True

    # Build sorted edge list (squared Euclidean distances)
    edges = []
    for i in range(n):
        x1, y1, z1 = data[i]
        for j in range(i + 1, n):
            x2, y2, z2 = data[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            edges.append((dist, i, j))
    edges.sort()

    # ----- Part 1: attempt first 10 shortest edges (call union for each) -----
    # Use a fresh DSU for part1
    parent1 = list(range(n))
    size1 = [1] * n

    def find1(x):
        while parent1[x] != x:
            parent1[x] = parent1[parent1[x]]
            x = parent1[x]
        return x

    def union1(a, b):
        ra, rb = find1(a), find1(b)
        if ra == rb:
            return False
        if size1[ra] < size1[rb]:
            ra, rb = rb, ra
        parent1[rb] = ra
        size1[ra] += size1[rb]
        return True

    # Attempt the first 10 edges (must attempt even if they don't merge)
    for k in range(min(1000, len(edges))):
        _, a, b = edges[k]
        union1(a, b)

    # compute component sizes for part1
    comp_sizes = {}
    for i in range(n):
        r = find1(i)
        comp_sizes[r] = comp_sizes.get(r, 0) + 1
    sizes_sorted = sorted(comp_sizes.values(), reverse=True)

    # product of three largest (if fewer than 3 components, treat missing as 1)
    top3 = sizes_sorted[:3] + [1] * max(0, 3 - len(sizes_sorted))
    part1 = top3[0] * top3[1] * top3[2]

    # ----- Part 2: Kruskal until single component -----
    # Reset DSU
    parent = list(range(n))
    size = [1] * n
    components = n
    last_pair = None

    for dist, a, b in edges:
        if union(a, b):
            components -= 1
            last_pair = (a, b)
            if components == 1:
                break

    if last_pair is None:
        part2 = 0
    else:
        ax = data[last_pair[0]][0]
        bx = data[last_pair[1]][0]
        part2 = ax * bx

    return part1, part2


if __name__ == "__main__":
    p1, p2 = day8()
    print("Part 1:", p1)
    print("Part 2:", p2)
