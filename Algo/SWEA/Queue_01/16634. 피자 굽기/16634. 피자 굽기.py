class CQ:
    def __init__(self, Qsize):
        self.front = 0
        self.rear = 0
        self.items = [None] * Qsize

    def enqueue(self, item):
        if (self.rear + 1) % len(self.items) == self.front:
            return "Queue is full"
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % len(self.items)

    def dequeue(self):
        if self.front == self.rear:
            return "Queue is empty"
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % len(self.items)
        return item

T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))

    cq = CQ(N)

    for c in Ci:
        result = cq.enqueue(c)
        if result == "Queue is full":
            break

    print(f"#{t}", end=" ")
    for _ in range(M):
        print(cq.dequeue(), end=" ")
    print()
