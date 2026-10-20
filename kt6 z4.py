class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


values = [1, 2, 3, 4, 5]
k = 2

head = None
tail = None
for value in values:
    node = Node(value)
    if head is None:
        head = tail = node
    else:
        tail.next = node
        tail = node

new_head = None
previous_tail = None
group_start = head
while group_start is not None:
    node = group_start
    count = 0
    while node is not None and count < k:
        node = node.next
        count += 1
    if count < k:
        if previous_tail is not None:
            previous_tail.next = group_start
        if new_head is None:
            new_head = group_start
        break

    rest = node
    previous = rest
    current = group_start
    for _ in range(k):
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt

    if new_head is None:
        new_head = previous
    if previous_tail is not None:
        previous_tail.next = previous
    previous_tail = group_start
    group_start = rest

while new_head is not None:
    print(new_head.value)
    new_head = new_head.next
