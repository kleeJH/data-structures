import unittest
from hash import LinearProbeTable

class TestHashTable(unittest.TestCase):
    def setup(self):
        pass

    def test_init(self):
        dictionary = LinearProbeTable()
        self.assertEqual(len(dictionary), 0, "Dictionary should be empty")

    def test_is_empty(self):
        dictionary = LinearProbeTable()
        self.assertTrue(dictionary.is_empty())

        dictionary["test"] = "test"
        self.assertFalse(dictionary.is_empty())

    def test_is_full(self):
        dictionary = LinearProbeTable(10)
        self.assertFalse(dictionary.is_full())

        for i in range(10):
            dictionary[str(i)] = i
        self.assertTrue(dictionary.is_full())

    def test_hash(self):
        dictionary = LinearProbeTable(5)
        for i in range(10):
            dictionary[str(i)] = i

        for i in range(10):
            self.assertEqual(dictionary[str(i)], i, "Could not find item: " + str(i))

    def test_len(self):
        dictionary = LinearProbeTable(5)
        self.assertEqual(len(dictionary), 0, "Dictionary should be empty")

        for i in range(3):
            dictionary[str(i)] = i

        self.assertEqual(len(dictionary), 3, "Dictionary should contain 3 items")

    def test_del(self):
        dictionary = LinearProbeTable(5)
        for i in range(10):
            dictionary[str(i)] = i

        for i in range(5):
            del dictionary[str(i)]

        for i in range(10):
            if i < 5:
                with self.assertRaises(KeyError):
                    _ = dictionary[str(i)]
            else:
                self.assertEqual(dictionary[str(i)], i, "Could not find item: " + str(i))

    def test_str(self):
        dictionary = LinearProbeTable(5)
        self.assertEqual(str(dictionary), "", "Dictionary should be empty")

        for i in range(5):
            dictionary[str(i)] = i
        for i in range(5):
            self.assertIn("(" + str(i) + "," + str(i) + ")", str(dictionary))


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHashTable)
    unittest.TextTestRunner(verbosity=2).run(suite)