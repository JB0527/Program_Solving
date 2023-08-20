class Queue:
    def __init__(self):
        self.q = []
    def isEmpty(self):
        return len(self.q) == 0
    def enQueue(self, item):
        self.q.append(item) #반닫힘 구조
    def deQueue(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)
    def peek(self): #pop 과 같다.
        return self.q[0]
    def size(self):
        return len(self.q)
    def top(self):
        return self.q[-1]
    def front(self):
        return self.q[0]
        
        
import sys
input = lambda  :sys.stdin.readline().rstrip()

if __name__ == "__main__":
    q = Queue()
    N = input()
    for i in range(int(N)): 
        command = input().split()
        if command[0] == 'push': 
            q.enQueue(command[1])
        elif command[0] == 'front':
            if q.size() == 0:
                print(-1)
            else:
                print(q.front())
        elif command[0] == 'back':
            if q.size() == 0:
                print(-1)
            else:
                print(q.top())
        elif command[0] == 'pop':
            if q.size() == 0:
                print(-1)
            else:
                print(q.deQueue())
        elif command[0] == 'empty':
            if q.isEmpty() == True:
                print(1)
            else: print(0)
        elif command[0] == 'size':
            print(q.size())