#File for implementing Bianry Tree and LCA method
class Node:
    def __init__(self, val):
        self.left= None
        self.right = None
        self.v = val

class Tree:
            
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


# Returns LCA if node n1 , n2 are present in the given
# binary tre otherwise return -1
def findLCA(root, n1, n2):

    # To store paths to n1 and n2 fromthe root
    path1 = []
    path2 = []

    # Find paths from root to n1 and root to n2.
    # If either n1 or n2 is not present , return -1
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    # Compare the paths to get the first different value
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]





#Check if it is working : 
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