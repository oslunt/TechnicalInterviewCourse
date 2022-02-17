# Write code for a search function for a binary tree
# Write code for a node and an insert function to create a binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def __init__(self):
        self.root = None
    
    def recInsert(self, current, data):
        if data < current.data:
            if current.left:
                self.recInsert(current.left, data)
            else:
                current.left = Node(data)
        else:
            if current.right:
                self.recInsert(current.right, data)
            else:
                current.right = Node(data)

    def insert(self, data):
        if(self.root):
            self.recInsert(self.root, data)
        else:
            self.root = Node(data)

    def recSearch(self, current, data):
        if current is None:
            return False
        elif current.data == data:
            return True
        elif data < current.data:
            return self.recSearch(current.left, data)
        else:
            return self.recSearch(current.right, data)

    def search(self, data):
        return self.recSearch(self.root, data)
    
def BSTprint(root):
    if root:
        BSTprint(root.left)
        print(root.data)
        BSTprint(root.right)

bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(4) 
bst.insert(7) 
bst.insert(8) 
bst.insert(6)
BSTprint(bst.root) 
print(bst.search(3))
print(bst.search(10))