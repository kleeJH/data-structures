""" Unit test for ArrayBasedSet, implemented via inheritance from TestSet. """
from test_set import *
from array_based_set import *

class TestArrayBasedSet(TestSet):

    @classmethod
    def setUpClass(cls):
        cls.SetType = ArrayBasedSet

    def test_is_full(self):
        " Check if the set is full after reaching full capacity in fixed sized array. "
        capacity = 10
        s = self.SetType(capacity)
        for i in range(capacity):
            self.assertFalse(s.is_full())
            s.add(i)
        self.assertTrue(s.is_full())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestArrayBasedSet)
    unittest.TextTestRunner(verbosity=2).run(suite)
