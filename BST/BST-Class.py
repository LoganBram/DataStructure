from queue import Queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0


class BST(Node):

    def __init__(self):
        self.root = None

    # used class slides code to help with this
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        elif key > node.val:
            node.right = self._insert(node.right, key)
        return node

    def print_inorder(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.val)
            self._print_inorder(node.right)

    def delete(self, value):
        if self.root is None:
            return self.root
        else:
            self.root = self._delete_helper(value, self.root)

    def _delete_helper(self, value, curr):
        if curr is None:
            return curr
        elif value > curr.val:
            curr.right = self._delete_helper(value, curr.right)
        elif value < curr.val:
            curr.left = self._delete_helper(value, curr.left)
        else:
            # Case 1: Node has no children
            if curr.left is None and curr.right is None:
                curr = None
            # Case 2: Node has one child
            elif curr.right is None:
                curr = curr.left
            elif curr.left is None:
                curr = curr.right
            # Case 3: Node has two children
            else:
                temp = self._find_min_node(curr.right)
                curr.val = temp.val
                curr.right = self._delete_helper(temp.val, curr.right)
        return curr

    def save(self):
        list = self._savehelp(self.root, [])
        # turns returned list into a string
        seperate = ','
        string = seperate.join(str(x) for x in list)
        self.restore(string)

    def _savehelp(self, curr, list):
        if curr is None:
            return curr

        list.append(curr.val)
        self._savehelp(curr.left, list)
        self._savehelp(curr.right, list)
        return list

    def restore(self, input_string):
        values = input_string.split(',')
        for i in range(len(values)):
            values[i] = int(values[i])
        self.root = None
        for value in values:
            self.insert(value)


        # create a new BST instance
bst = BST()

# insert some nodes
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)
bst.insert(17)

bst.print_inorder()

# get the total height of the tree
# bst.print_inorder()
# bst.delete(17)
# print("")
# bst.print_inorder()

bst.save()

print("")
bst.print_inorder()
print("")
print(bst.get_total_height())


"""root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Function call

root.get_total_height()"""
