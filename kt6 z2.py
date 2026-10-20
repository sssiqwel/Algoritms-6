n = 5
operations = [
    (1, 1, 2),
    (2, 1, 2),
    (2, 1, 3),
    (1, 2, 3),
    (2, 1, 3),
    (2, 4, 5),
    (2, 4, 4),
]

parent = list(range(n + 1))


def find(station):
    while parent[station] != station:
        parent[station] = parent[parent[station]]
        station = parent[station]
    return station


for operation_type, u, v in operations:
    if operation_type == 1:
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_v] = root_u
    else:
        if find(u) == find(v):
            print("YES")
        else:
            print("NO")
