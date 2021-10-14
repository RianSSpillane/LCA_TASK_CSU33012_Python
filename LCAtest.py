#File for runnign tests 

#Import the binary tree structure 
from BinaryTree import *
import unittest   # The test framework

class LCAtests(unittest.TestCase):
        
    def testBaicLCA(self):
    # most basic case tree with two children
    #    10
    #   / \
    #  6   20
        tree = Tree()
        tree.add(10)
        tree.add(6)
        tree.add(20)
        self.assertEqual(findLCA(tree.root, 20, 6), 10)
    
    def testLongTreeTest(self):
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        tree = Tree()
        tree.add(1)
        tree.add(3)
        tree.add(6)
        tree.add(9)
        tree.add(12)
        tree.add(15)
        self.assertEqual(findLCA(tree.root, 12, 15), 12)

    def testEmptyTree(self):
        # when root is not defined in BST
        tree = Tree()
        self.assertEqual((tree.root),None)

        self.assertEqual(findLCA(tree.root, 11, 33), -1)

    def testRoot(self):
        # when only root exist
        tree = Tree()
        tree.add(10)
        self.assertEqual(findLCA(tree.root, 1, 1), -1)

    def testWideTree(self):
        #     10
        #   /    \
        #  5     15
        # /  \   /
        # 2   7 13
        # non balanced tree
        tree =  Tree()
        tree.add(10)
        tree.add(5)
        tree.add(15)
        tree.add(2)
        tree.add(7)
        tree.add(13)
        self.assertEqual(findLCA(tree.root, 2, 13), 10)