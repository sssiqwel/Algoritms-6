import heapq

k = 3
words = ["ba", "bc", "ca"]

graph = [set() for _ in range(k)]
indegree = [0] * k
impossible = False
for i in range(len(words) - 1):
    left = words[i]
    right = words[i + 1]
    limit = min(len(left), len(right))
    found_difference = False
    for position in range(limit):
        if left[position] != right[position]:
            earlier = ord(left[position]) - 97
            later = ord(right[position]) - 97
            if later not in graph[earlier]:
                graph[earlier].add(later)
                indegree[later] += 1
            found_difference = True
            break
    if not found_difference and len(left) > len(right):
        impossible = True

available = [letter for letter in range(k) if indegree[letter] == 0]
heapq.heapify(available)
order = []
while available and not impossible:
    letter = heapq.heappop(available)
    order.append(letter)
    for nxt in graph[letter]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(available, nxt)

if impossible or len(order) != k:
    print("IMPOSSIBLE")
else:
    print("".join(chr(97 + letter) for letter in order))
