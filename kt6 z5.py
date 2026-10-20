n = 3
statements = [
    (1, 2, 1),
    (2, 3, 1),
    (1, 3, 0),
    (1, 3, 1),
    (1, 2, 0),
]

parent = list(range(2 * n + 1))
impossible = False


def find(person):
    while parent[person] != person:
        parent[person] = parent[parent[person]]
        person = parent[person]
    return person


def unite(first, second):
    first = find(first)
    second = find(second)
    if first != second:
        parent[second] = first


for u, v, relation in statements:
    if impossible:
        print("NO")
        continue
    if relation == 0:
        if find(u) == find(v + n):
            impossible = True
            print("NO")
            continue
        unite(u, v)
        unite(u + n, v + n)
    else:
        if find(u) == find(v):
            impossible = True
            print("NO")
            continue
        unite(u, v + n)
        unite(u + n, v)
    print("YES")
