from binary_search_tree import BinarySearchTree, TraversalType
import unittest

class TestBinarySearchTree(unittest.TestCase):
    """ Tests for the above class. """

    def setUp(self):
        """
                        30 (root)
                    /               \
                    20              40
                /       \       /       \
                15      25      35      50
            /       \                 /     \
            5       18              45      60

            Ref: https://iq.opengenus.org/binary-tree-traversals-inorder-preorder-postorder/
        """

        self.tree = BinarySearchTree()
        self.tree[30] = 30
        self.tree[20] = 20
        self.tree[40] = 40
        self.tree[15] = 15
        self.tree[25] = 25
        self.tree[35] = 35
        self.tree[50] = 50
        self.tree[5] = 5
        self.tree[18] = 18
        self.tree[45] = 45
        self.tree[60] = 60
        

    def tearDown(self):
        self.tree.root = None

    def test_preorder_traversal_iterator(self):
        self.tree.traversal_type = TraversalType.PRE_ORDER
        self.assertEqual(str([i for i in self.tree]), "[30, 20, 15, 5, 18, 25, 40, 35, 50, 45, 60]")

    def test_inorder_traversal_iterator(self):
        self.tree.traversal_type = TraversalType.IN_ORDER
        self.assertEqual(str([i for i in self.tree]), "[5, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60]")

    def test_postorder_traversal_iterator(self):
        self.tree.traversal_type = TraversalType.POST_ORDER
        self.assertEqual(str([i for i in self.tree]), "[5, 18, 15, 25, 20, 35, 45, 60, 50, 40, 30]")

    def test_preorder_traversal_recursive(self):
        self.res = []
        self.tree.preorder(lambda item: self.res.append(item))
        self.assertEqual(str(self.res), "[30, 20, 15, 5, 18, 25, 40, 35, 50, 45, 60]")

    def test_inorder_traversal_recursive(self):
        self.res = []
        self.tree.inorder(lambda item: self.res.append(item))
        self.assertEqual(str(self.res), "[5, 15, 18, 20, 25, 30, 35, 40, 45, 50, 60]")

    def test_postorder_traversal_recursive(self):
        self.res = []
        self.tree.postorder(lambda item: self.res.append(item))
        self.assertEqual(str(self.res), "[5, 18, 15, 25, 20, 35, 45, 60, 50, 40, 30]")

    def test_get_leaves(self):
        self.assertEqual(str(self.tree.get_leaves()), "[5, 18, 25, 35, 45, 60]")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBinarySearchTree)
    unittest.TextTestRunner(verbosity=2).run(suite)