class Node:

    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Traversing
    # 2 conditions: empty and not empty
    # empty?
    def print_LL(self):
        if self.head is None:
            print("LL is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    # not empty


node1 = Node(10)
