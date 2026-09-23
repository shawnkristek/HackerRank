from timeit import timeit

class Queue:
    def __init__(self):
        self.reversed = False
        self.first = None
        self.stack1 = []
        self.stack2 = []

    def ops(self, op: int, val=None):
        if op == 1:
            self.__enqueue(val)
        if op == 2:
            self.__dequeue()
        if op == 3:
            self.__print()
        
        # print(self.stack1, self.stack2, self.first, self.reversed)

    def __enqueue(self, val: int):
        if self.reversed:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            self.reversed = False

        if not self.stack1:
            self.first = val

        self.stack1.append(val)

    def __dequeue(self):
        if self.reversed:
            self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

            self.stack2.pop()

        if self.stack2:
            self.first = self.stack2[-1]
        else:
            self.first = None
        self.reversed = True
        
    def __print(self):
        print(self.first)

# run tests

q = Queue()
q.ops(1, 42)
q.ops(2)
q.ops(1, 14)
q.ops(3)
q.ops(1, 28)
q.ops(3)
q.ops(1, 60)
q.ops(1, 78)
q.ops(2)
q.ops(2)

q = Queue()
q.ops(1, 76)
q.ops(1, 33)
q.ops(2)
q.ops(1, 23)
q.ops(1, 97)
q.ops(1, 21)
q.ops(3)
q.ops(3)
q.ops(1, 74)
q.ops(3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = 