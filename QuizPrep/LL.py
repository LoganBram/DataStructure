class Node:

    def __init__(self, d):
        self.data = d
        self.next = None


class LL:

    def __init__(self):
        self.head = None
        self.tail = None

    def FrontAdd(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def BackAdd(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def FrontDelete(self):
        if self.head is None:
            pass
        else:
            self.head = self.head.next

    def BackDelete(self):
        if self.head is None:
            pass
        else:
            n = self.head
            while n.next != self.tail:
                n = n.next
            n.next = None
            self.tail = n

    def Print(self):
        if self.head is None:
            pass
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.next


# test cases
B = LL()
A = LL()
A.FrontAdd(1)
A.FrontAdd(2)
A.FrontAdd(3)
B.BackAdd(1)
B.BackAdd(2)
B.BackAdd(4)

A.BackDelete()
B.BackDelete()

A.Print()
B.Print()
