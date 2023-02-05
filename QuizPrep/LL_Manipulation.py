from LL import LL as LL

# doesnt work


def Swap(self, value1, value2):
    n = self.head
    prevNode1 = None
    prevNode2 = None
    node1 = self.head
    node2 = self.head

    while (node1 != None and node1.data != value1):
        prevNode1 = node1
        node1 = node1.next
    while (node2 != None and node1.data != value1):
        prevNode2 = node2
        node2 = node2.next
        if (node1 != None and node2 != None):
            if (prevNode1 != None):
                prevNode1.next = node2
            else:
                self.head = node2

            if (prevNode2 != None):
                prevNode2.next = node1
            else:
                self.head = node1

            temp = node1.next
            node1.next = node2.next
            node2.next = temp


# dummy version


class LLStack:
    def __init__(self):
        self.stack = LL()

    def push(self, d):
        self.stack.FrontAdd(d)

    def pop(self):
        return self.stack.FrontDelete()

    def display(self):
        return self.stack.Print()

# real version


class Node:
    def __init__(self, d):
        self.data = d
        self.next = None


class LLStackV2:

    def __init__(self):
        self.top = None

    def push(self, d):
        new_node = Node(d)
        if self.top == None:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        x = self.top.data
        self.top = self.top.next

    def print(self):
        n = self.top
        while n != None:
            print(n.data)
            n = n.next


class QueueStack:
    def __init__(self):
        self.bottom = None


class Manipulation(LL):
    # works
    def Reverse(self):
        prev = None
        current = self.head
        next = None
        print(current.data)
        while current.next is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = current

    # merges & sorts 2 LL of same size
    # identified numbers properly but issues with assigning numers to proper node in new LL
    # issue is in while loop
    def Merge(self, L1=LL(), L2=LL()):
        L1current = L1.head
        L2current = L2.head
        L3current = None
        if self.head == None:
            if L1current.data <= L2current.data:
                self.head = L1current
                L1current = L1current.next
            else:
                self.head = L2current
                L2current = L2current.next

        print(self.head.data, "here")
        while (L1current != None or L2current != None):

            if (L1current != None and L2current != None):
                if L1current.data <= L2current.data:
                    self.next = L1current
                    L1current = L1current.next
                    print(self.next.data, "here")
                    pass
                if L2current.data <= L1current.data:
                    self.next = L2current
                    L2current = L2current.next
                    print(self.next.data, "here")
                    pass

            if (L1current == None and L2current == None):
                return
            if (L1current != None and L2current == None):
                self.next = L1current
                L1current = L1current.next
                print(self.next.data, "here")

            if (L2current != None and L1current == None):
                self.next = L2current
                L2current = L2current.next
                print(self.next.data, "here")


q = Manipulation()
L1 = Manipulation()
L2 = Manipulation()
L1.FrontAdd(1)
L1.BackAdd(3)
L1.BackAdd(10)
L2.FrontAdd(5)
L2.BackAdd(6)
L2.BackAdd(9)
q.Merge(L1, L2)
print("\n")
q.Print()
