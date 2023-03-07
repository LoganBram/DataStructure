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

    def inorder(self):
        self.inorderhelp(self.root)

    def inorderhelp(self, node):
        # class slides helped with this as well sorta
        if node != None:
            self.inorderhelp(node.left)
            print(node.val)
            self.inorderhelp(node.right)

    def delete(self, target):
        self.root = self.delete_helper(self.root, target)

    def delete_helper(self, curr, target):
        # iterate through BST
        if curr == None:
            return None
        if curr.val < target:
            curr.right = self.delete_helper(curr.right, target)
        elif curr.val > target:
            curr.left = self.delete_helper(curr.left, target)
        else:
            # value found
            # node has no children
            if curr.left is None and curr.right is None:
                curr = None
            # Node has one child
            elif curr.left is None:
                curr = curr.right
            elif curr.right is None:
                curr = curr.left
            # node has two children
            else:
                temp = curr.right
                while temp.left is not None:
                    temp = temp.left
                # replace value of current node with value of the min node
                curr.val = temp.val
                # delete minimum node in the right subtree
                curr.right = self.delete_helper(curr.right, temp.val)

        return curr

    # incomplete total height obtain

    def _find_min_node(self, curr):
        while curr.left != None:
            curr = curr.left
        return curr

    def save(self):
        list = self._savehelp(self.root, [])
        # turns returned list from savehelp, into a string
        seperate = ','
        string = seperate.join(str(x) for x in list)
        self.restore(string)

    def _savehelp(self, curr, list):
        # makes tree into list recursively
        if curr == None:
            return curr
        list.append(curr.val)
        self._savehelp(curr.left, list)
        self._savehelp(curr.right, list)

        return list

    def restore(self, input_string):
        # splits values in string into list via ,
        vals = input_string.split(',')
        # changes strings to ints
        for i in range(len(vals)):
            vals[i] = int(vals[i])
        self.root = None
        # inserts values into tree to restore
        for i in vals:
            self.insert(i)


# create a new BST instance
bst = BST()

# insert some nodes
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(13)

# total_height = bst.get_total_height()
# print(total_height)

print("after insertion, printing in-order: ")
bst.inorder()

print("tree after deleting two child (5): ")
bst.delete(5)
bst.inorder()

print("tree after deleting one child node(15): ")
bst.delete(15)
bst.inorder()

print("tree after deleting no child node (3):")
bst.delete(3)
bst.inorder()

print("tree after save and restoration, inserted more nodes, restore is ran within save: ")

bst.insert(5)
bst.insert(12)
bst.insert(8)
bst.save()
bst.inorder()

print(" ")
