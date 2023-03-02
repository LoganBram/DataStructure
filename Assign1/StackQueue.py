from collections import deque

#


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        index = len(self.items)
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        Queue.enqueue(self, item)

    def pop(self):
        for i in range(len(self.items)-1):
            moving = Queue.dequeue(self)
            Queue.enqueue(self, moving)
        final = Queue.dequeue(self)
        return final

    def peek(self):
        for i in range(len(self.items)-1):
            moving = Queue.dequeue(self)
            Queue.enqueue(self, moving)
        final = Queue.dequeue(self)
        Queue.enqueue(self, final)
        return final

    def search(self, search):
        index = None
        counter = (len(self.items))
        for i in range(len(self.items)):
            x = Queue.dequeue(self)
            if x == search:
                position = counter
                Queue.enqueue(self, x)
            else:
                counter -= 1
                Queue.enqueue(self, x)

        return ("position of element where top of stack is 1:", position)

    def empty(self):
        return Queue.is_empty(self)


t = Stack()
t.push(1)
t.push(2)
t.push(3)
t.push(4)
print(t.items)
t.pop()
print(t.items)
print(t.peek(), "peeked")
print(t.items)
print(t.search(1))
print(t.empty())
