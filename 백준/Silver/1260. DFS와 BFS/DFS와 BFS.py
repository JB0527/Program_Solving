import sys


class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(0)
        else:
            return None

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.s)

    def print(self):
        print(self.s)


class Queue:
    def __init__(self):
        self.q = []

    def enQueue(self, item):
        self.q.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop(0)

    def size(self):
        return len(self.q)

    def isEmpty(self):
        if len(self.q) > 0:
            return False
        else:
            return True

    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")


class Graph:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.s = Stack()
        self.visit = []

    def dfs(self):
        self.s.push(self.start)
        while self.s.isEmpty() == False:
            curNode = self.s.pop()
            if curNode not in self.visit:
                self.visit.append(curNode)

                my_node = [
                    node
                    for node in sorted(list(set(self.graph[curNode]) - set(self.visit)))
                ]
                self.s.s = my_node + self.s.s
        return self.visit

    def bfs(self):
        visit = [self.start]
        queue = Queue()
        for item in self.graph[self.start]:
            queue.enQueue(item)

        while queue.isEmpty() == False:
            item = queue.deQueue()
            if not item in visit:  # 현재 아이템이 가본 곳이 아니면 ...
                for _item in self.graph[item]:
                    queue.enQueue(_item)
                visit.append(item)
        return visit


input = lambda: sys.stdin.readline().rstrip()
my_input = input()
v, e, start = [int(i) for i in my_input.split(" ")]
edge = [[False for i in range(v)] for i in range(v)]
for i in range(e):
    x, y = input().split(" ")
    edge[int(x) - 1][int(y) - 1] = True
    edge[int(y) - 1][int(x) - 1] = True

my_dict = {}
for idx, value in enumerate(edge):
    my_dict[idx] = [i for i, j in enumerate(value) if j]

g = Graph(my_dict, start - 1)

print(" ".join([f"{i + 1}" for i in g.dfs()]))
print(" ".join([f"{i + 1}" for i in g.bfs()]))
