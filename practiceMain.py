print("Hello World")


#Import class :
from BinaryTree import *

#Testing to see how importing classes works in Python
tree = Tree()
tree.add(6)
tree.add(4)
tree.add(10)
tree.add(2)
tree.add(5)
tree.add(6)
tree.add(3)
#tree.printTree()
findLCA(tree.root, 2, 5)
#print(Tree.findLCA(tree.root, 4, 10))