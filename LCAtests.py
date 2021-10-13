#File for runnign tests 
print("Hello World")

from BinaryTree import Tree
from BinaryTree import Node
import unittest   # The test framework

class LCAtests(unittest.TestCase):
    def test_tree(self):
        tree =  Tree()
        tree.add(6)
        tree.add(4)
        tree.add(10)
        tree.add(2)
        tree.add(5)
        tree.add(6)
        tree.add(3)
        #tree.printTree()
        self.assertEqual(Tree.findLCA(tree.root, 2, 5), 6)
