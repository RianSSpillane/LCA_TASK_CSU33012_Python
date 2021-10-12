#File for implementing Bianry Tree and LCA method
# class Node:
#     def __init__(self, val):
#         self.left= None
#         self.right = None
#         self.v = val
            

class Tree:

    class Node:
        def __init__(self, val):
            self.left= None
            self.right = None
            self.v = val
            
    # Constructor
    def __init__(self):
        self.root = None

    def findRoot(self):
        return self.root
    
    # Function for adding elements to the tree
    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    # Recursive function for adding elements to the tree
    def _add(self, val, node):
        if val < node.v:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    #Find if an element exists in the tree
    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    # Recursive function for seeing if element exists in the tree
    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.left is not None):
            return self._find(val, node.left)
        elif (val > node.v and node.right is not None):
            return self._find(val, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.v) + ' ')
            self._printTree(node.right)



    

 
# Driver program to test above function
# Let's create the Binary Tree shown in above diagram
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)


 
# print "tree.LCA(4, 5) = %d" %(findLCA(root, 4, 5,))

# print "LCA(4, 6) = %d" %(findLCA(root, 4, 6))
# print "LCA(3, 4) = %d" %(findLCA(root,3,4))
# print "LCA(2, 4) = %d" %(findLCA(root,2, 4))

tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
#tree.findLCA(4,2)