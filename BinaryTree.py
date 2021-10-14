# File for implementing Bianry Tree and LCA method

#This is my attempt at trying out a new programming langaugae --> I chose python 

#To build a tree : 
## tree =  Tree()
## tree.add(6)
## tree.add(4)
## ree.add(10)

# Class for nodes
class Node:
    # Constructor
    def __init__(self, value):
        self.left= None
        self.right = None
        self.v = value

# Class for building a tree
class Tree:
            
    # Constructor
    def __init__(self):
        self.root = None

    #Find the root
    def findRoot(self):
        return self.root
    
    # Function for adding elements to the tree
    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.addRecursive(value, self.root)

    # Recursive function for adding elements to the tree
    def addRecursive(self, value, node):
        if value < node.v:
            if node.left is not None:
                self.addRecursive(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self.addRecursive(value, node.right)
            else:
                node.right = Node(value)

    #Find if an element exists in the tree
    def find(self, value):
        if self.root is not None:
            return self.findRecursive(value, self.root)
        else:
            return None

    # Recursive function for seeing if element exists in the tree
    def findRecursive(self, value, node):
        if value == node.v:
            return node
        elif (value < node.v and node.left is not None):
            return self.findRecursive(value, node.left)
        elif (value > node.v and node.right is not None):
            return self.findRecursive(value, node.right)

    def deleteTree(self):
        self.root = None

    
    #Attempt at implementing the same printing method as I did in java
    def printTreeInOrder(self):
        if self.root is None:
            print('()')
        else :
            self._printTreeInOrder(self.root)

    def _printTreeInOrder(self, node):
        if node is None :
            print('()')
        else :
            print("(" + self._printTreeInOrder(node.left) + node.value + self._printTreeInOrder(node.right) + ")")	

    
def findPath( root, path, k):
    # Base Case
    if root is None:
        return False

    # Store this node is path vector. The node will be
    # removed if not in path from root to k
    path.append(root.v)

    # See if the k is same as root's v
    if root.v == k :
        return True

    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False


# Returns LCA if node A , B are present in the given
# binary tre otherwise return -1
def findLCA(root, A, B):

    # To store paths to A and B fromthe root
    pathA = []
    pathB = []

    # Find paths from root to A and root to B.
    # If either A or B is not present , return -1
    if (not findPath(root, pathA, A) or not findPath(root, pathB, B)):
        # If elements don't exist return -1
        return -1

    # Compare the paths to get the first different value
    counter= 0
    while(counter< len(pathA) and counter < len(pathB)):
        if pathA[counter] != pathB[counter]:
            break
        counter+= 1
    return pathA[counter-1]




#------------------------------------------------------------------
#Check if structure it is working : 
tree = Tree()
tree.add(6)
tree.add(4)
tree.add(10)
tree.add(2)
tree.add(5)
tree.add(6)
tree.add(3)
#tree.printTree()
print(findLCA(tree.root, 4, 10))