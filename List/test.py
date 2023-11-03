from enum import Enum
import unittest
from list import ArrayList, LinkList


class DataStructure(Enum):
    ARRAY = 1
    LINK = 2


class TestList(unittest.TestCase):
    EMPTY = 0
    ROOMY = 5
    LARGE = 10

    def setUp(self):
        self.lengths = [self.EMPTY, self.ROOMY,
                        self.LARGE, self.ROOMY, self.LARGE]
        if test_list == DataStructure.ARRAY:
            self.lists = [ArrayList(self.LARGE)
                          for i in range(len(self.lengths))]
        else:
            self.lists = [LinkList() for i in range(len(self.lengths))]
        for list, length in zip(self.lists, self.lengths):
            for i in range(length):
                list.append(i)
        self.empty_list = self.lists[0]
        self.roomy_list = self.lists[1]
        self.large_list = self.lists[2]
        self.clear_list = self.lists[3]
        self.clear_list.clear()
        self.lengths[3] = 0
        self.lists[4].clear()
        self.lengths[4] = 0

    def tearDown(self):
        for s in self.lists:
            s.clear()

    def test_init(self) -> None:
        self.assertTrue(self.empty_list.is_empty())
        self.assertEqual(len(self.empty_list), 0)

    def test_len(self):
        """ Tests the length of all lists created during setup."""
        for list, length in zip(self.lists, self.lengths):
            self.assertEqual(len(list), length)

    def test_is_empty_add(self):
        """ Tests lists that have been created empty/non-empty."""
        self.assertTrue(self.empty_list.is_empty())
        self.assertFalse(self.roomy_list.is_empty())
        self.assertFalse(self.large_list.is_empty())

    def test_is_empty_clear(self):
        """ Tests lists that have been cleared."""
        for list in self.lists:
            list.clear()
            self.assertTrue(list.is_empty())

    def test_is_empty_delete_at_index(self):
        """ Tests lists that have been created and then deleted completely."""
        for list in self.lists:
            for i in range(len(list)):
                self.assertEqual(list.delete_at_index(0), i)
            try:
                list.delete_at_index(-1)
            except:
                self.assertTrue(list.is_empty())

    def test_append_and_remove_item(self):
        for list in self.lists:
            nitems = self.ROOMY
            list.clear()
            for i in range(nitems):
                list.append(i)
            for i in range(nitems-1):
                list.remove(i)
                self.assertEqual(list[0], i+1)
            list.remove(nitems-1)
            self.assertTrue(list.is_empty())
            for i in range(nitems):
                list.append(i)
            for i in range(nitems-1, 0, -1):
                list.remove(i)
                self.assertEqual(list[len(list)-1], i-1)
            list.remove(0)
            self.assertTrue(list.is_empty())

    def test_clear(self):
        for list in self.lists:
            list.clear()
            self.assertTrue(list.is_empty())


if __name__ == '__main__':
    test_list = DataStructure.ARRAY
    suite = unittest.TestLoader().loadTestsFromTestCase(TestList)
    unittest.TextTestRunner().run(suite)

    test_list = DataStructure.LINK
    suite = unittest.TestLoader().loadTestsFromTestCase(TestList)
    unittest.TextTestRunner().run(suite)
