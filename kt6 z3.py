import heapq

n = 4
requirements = [
    (1, 2),
    (1, 3),
    (3, 4),
]

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
used = set()
impossible = False
for before, after in requirements:
    if before == after:
        impossible = True
    if (before, after) in used:
        continue
    used.add((before, after))
    graph[before].append(after)
    indegree[after] += 1

available = [stage for stage in range(1, n + 1) if indegree[stage] == 0]
heapq.heapify(available)
order = []
while available and not impossible:
    stage = heapq.heappop(available)
    order.append(stage)
    for nxt in graph[stage]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(available, nxt)

if impossible or len(order) != n:
    print(-1)
else:
    print(*order)
