
from enum import Enum
import unittest
from queue import LinearQueue, CircularQueue, LinkQueue


class DataStructure(Enum):
    LINEAR = 1
    CIRCULAR = 2
    LINK = 3


class TestQueue(unittest.TestCase):
    """ Tests for the above class."""
    EMPTY = 0
    ROOMY = 5
    LARGE = 10
    CAPACITY = 20

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY, self.LARGE, self.ROOMY, self.LARGE]

        if test_list == DataStructure.LINEAR:
            self.queues = [LinearQueue(self.CAPACITY) for i in range(len(self.lengths))]
        elif test_list == DataStructure.CIRCULAR:
            self.queues = [CircularQueue(self.CAPACITY) for i in range(len(self.lengths))]
        else:
            self.queues = [LinkQueue() for i in range(len(self.lengths))]

        for queue, length in zip(self.queues, self.lengths):
            for i in range(length):
                queue.append(i)
        self.empty_queue = self.queues[0]
        self.roomy_queue = self.queues[1]
        self.large_queue = self.queues[2]
        self.clear_queue = self.queues[3]
        self.clear_queue.clear()
        self.lengths[3] = 0
        self.queues[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.queues:
            s.clear()

    def test_init(self):
        self.assertTrue(self.empty_queue.is_empty())
        self.assertEqual(len(self.empty_queue), 0)
            
    def test_len(self):
        """ Tests the length of all queues created during setup. """
        for queue, length in zip(self.queues, self.lengths):
            self.assertEqual(len(queue), length)
            
    def test_is_empty_add(self):
        """ Tests queues that have been created empty/non-empty. """
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.roomy_queue.is_empty())
        self.assertFalse(self.large_queue.is_empty())
    
    def test_is_empty_clear(self):
        """ Tests queues that have been cleared. """
        for queue in self.queues:
            queue.clear()
            self.assertTrue(queue.is_empty())
            
    def test_is_empty_serve(self):
        """ Tests queues that have been served completely. """
        for queue in self.queues:
            try:
                while True:
                    was_empty = queue.is_empty()
                    queue.serve()
                    self.assertFalse(was_empty)
            except:
                self.assertTrue(queue.is_empty())
            
    def test_is_full_add(self):
        """ Tests queues that have been created not full. """
        self.assertFalse(self.empty_queue.is_full())
        self.assertFalse(self.roomy_queue.is_full())
        self.assertFalse(self.large_queue.is_full())
        
    def test_append_and_serve(self):
        for queue in self.queues:
            nitems = self.ROOMY
            for i in range(nitems):
                queue.append(i)
            for i in range(nitems):
                self.assertEqual(queue.serve(), i)
                
    def test_clear(self):
        for queue in self.queues:
            queue.clear()
            self.assertEqual(len(queue), 0)
            self.assertTrue(queue.is_empty())


if __name__ == '__main__':
    test_list = DataStructure.LINEAR
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)

    test_list = DataStructure.CIRCULAR
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)

    test_list = DataStructure.LINK
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueue)
    unittest.TextTestRunner(verbosity=2).run(suite)