class Node:

    def __init__(self, d):
        self.data = d
        self.next = None


class LL:

    def __init__(self):
        self.head = None
        self.tail = None

    def FrontAdd(self, d):
        if self.head == None:
            new_node = Node(d)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = Node(d)
            new_node.next = self.head
            self.head = new_node

    def BackAdd(self, d):
        new_node = Node(d)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node
            self.tail = new_node

    def Print(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next

    def CompareLists(self, headB: 'LL'):
        A = self.head
        B = headB.head
        A = A.next
        B = B.next


# test cases
B = LL()
A = LL()
A.FrontAdd(1)
A.FrontAdd(2)
A.FrontAdd(3)
B.FrontAdd(1)
B.FrontAdd(2)
B.FrontAdd(4)

A.CompareLists(B)
