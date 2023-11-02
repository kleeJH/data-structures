from enum import Enum
import unittest
from stack import ArrayStack, LinkStack

class DataStructure(Enum):
    ARRAY = 1
    LINK = 2

class TestStack(unittest.TestCase):
    """ Tests for the above class. """
    EMPTY = 0
    ROOMY = 5
    LARGE = 10
    CAPACITY = 20

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]

        if test_list == DataStructure.ARRAY:
            self.stacks = [ArrayStack(self.CAPACITY) for i in range(len(self.lengths))]
        else:
            self.stacks = [LinkStack() for _ in range(len(self.lengths))]

        for stack, length in zip(self.stacks, self.lengths):
            for i in range(length):
                stack.push(i)
        
        self.empty_stack = self.stacks[0]
        self.roomy_stack = self.stacks[1]
        self.large_stack = self.stacks[2]
        self.clear_stack = self.stacks[3]
        self.clear_stack.clear()
        self.lengths[3] = 0
        self.stacks[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.stacks:
            s.clear()

    def test_init(self):
        self.assertTrue(self.empty_stack.is_empty())
        self.assertEqual(len(self.empty_stack), 0)
            
    def test_len(self):
        """ Tests the length of all stacks created during setup. """
        for stack, length in zip(self.stacks, self.lengths):
            self.assertEqual(len(stack), length)
            
    def test_is_empty_add(self):
        """ Tests stacks that have been created empty/non-empty. """
        self.assertTrue(self.empty_stack.is_empty())
        self.assertFalse(self.roomy_stack.is_empty())
        self.assertFalse(self.large_stack.is_empty())
    
    def test_is_empty_clear(self):
        """ Tests stacks that have been cleared. """
        for stack in self.stacks:
            stack.clear()
            self.assertTrue(stack.is_empty())
            
    def test_is_empty_pop(self):
        """ Tests stacks that have been popped completely. """
        for stack in self.stacks:
            try:
                while True:
                    was_empty = stack.is_empty()
                    stack.pop()
                    self.assertFalse(was_empty)
            except:
                self.assertTrue(stack.is_empty())
            
    def test_is_full_add(self):
        """ Tests stacks that have been created not full. """
        self.assertFalse(self.empty_stack.is_full())
        self.assertFalse(self.roomy_stack.is_full())
        self.assertFalse(self.large_stack.is_full())
        
    def test_push_and_pop(self):
        for stack in self.stacks:
            nitems = self.ROOMY
            for i in range(nitems):
                stack.push(i)
            for i in range(nitems-1, -1, -1):
                self.assertEqual(stack.pop(), i)
                
    def test_clear(self):
        for stack in self.stacks:
            stack.clear()
            self.assertEqual(len(stack), 0)
            self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    # ArrayStack
    test_list = DataStructure.ARRAY
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStack)
    unittest.TextTestRunner().run(suite)

    # LinkStack
    test_list = DataStructure.LINK
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStack)
    unittest.TextTestRunner().run(suite)