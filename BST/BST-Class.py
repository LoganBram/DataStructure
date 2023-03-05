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

    def _insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.val:
            root.left = self._insert(root.left, key)
        elif key > root.val:
            root.right = self._insert(root.right, key)
        return root

    def get_total_height(self):
        self._get_total_height(self.root)

    def _get_total_height(self, node):
        temp = None
        queue = []
        queue.append(node)
        while len(queue) != 0:
            temp = queue.pop(0)

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
            self._delete_helper(value, self.root)

    def _delete_helper(self, value, current_node):
        if current_node is None:
            return current_node
        elif value < current_node.val:
            self._delete_helper(value, current_node.left)
        elif value > current_node.val:
            self._delete_helper(value, current_node.right)
        else:
            # Case 1: Node has no children
            if current_node.left is None and current_node.right is None:
                current_node = None
            # Case 2: Node has one child
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            # Case 3: Node has two children
            else:
                temp = self._find_min_node(current_node.right)
                current_node.val = temp.value
                current_node.right = self._delete_helper(
                    temp.value, current_node.right)
        return current_node


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

# get the total height of the tree
bst.print_inorder()
bst.delete(17)
print("")
bst.print_inorder()

"""root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Function call

root.get_total_height()"""
