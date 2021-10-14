# ----------------------------------------------------------------------------------------
# CSU33012 ASSIGNMENT 1 : LOWEST COMMON ANCESTOR
# IMPLEMENTING SOLUTION IN PROGRAMMING LANGUAGE NOT USED BEFORE
# 
# This class was used to test out using python
# I used it to learn how to import another python class 
# I also used it to test if the tree would run okay 
# 
# @author : Rian Spillane
# @Date : 14/10/21
# @PythonVersion : Python 2.7.16
# ----------------------------------------------------------------------------------------

print("Hello World")
print(1)


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