class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


values = [1, 2, 3, 4, 5]

head = None
tail = None
for value in values:
    node = Node(value)
    if head is None:
        head = tail = node
    else:
        tail.next = node
        tail = node

previous = None
current = head
while current is not None:
    nxt = current.next
    current.next = previous
    previous = current
    current = nxt
head = previous

while head is not None:
    print(head.value)
    head = head.next
