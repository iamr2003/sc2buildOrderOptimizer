from indexedPQ import PriorityQueue
import unittest

#chatgpt generated unit tests

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()


    # having issues on this test case
    def test_push_pop(self):
        self.pq.push("a", 2, "element A")
        self.pq.push("c", 3, "element C")
        self.pq.push("b", 1, "element B")
        self.assertEqual(self.pq.pop(), "element B")
        self.assertEqual(self.pq.pop(), "element A")
        self.assertEqual(self.pq.pop(), "element C")

    def test_get(self):
        self.pq.push("a", 1, "element A")
        self.pq.push("b", 2, "element B")
        self.assertEqual(self.pq.get("a"), "element A")
        self.assertEqual(self.pq.get("b"), "element B")
        self.assertIsNone(self.pq.get("c"))

    def test_set_priority(self):
        self.pq.push("a", 1, "element A")
        self.pq.push("b", 2, "element B")
        self.pq.set_priority("a", 3)
        self.assertEqual(self.pq.pop(), "element B")
        self.assertEqual(self.pq.pop(), "element A")

    def test_remove(self):
        self.pq.push("a", 1, "element A")
        self.pq.push("b", 2, "element B")
        self.pq.remove("a")
        self.assertIsNone(self.pq.get("a"))
        self.assertEqual(self.pq.pop(), "element B")

    def test_contains(self):
        self.pq.push("a", 1, "element A")
        self.assertTrue(self.pq.contains("a"))
        self.assertFalse(self.pq.contains("b"))

    def test_get_priority(self):
        self.pq.push("a", 1, "element A")
        self.pq.push("b", 2, "element B")
        self.assertEqual(self.pq.get_priority("a"), 1)
        self.assertEqual(self.pq.get_priority("b"), 2)
        self.assertIsNone(self.pq.get_priority("c"))

    def test_mass_insertion(self):
        n = 1000000 #3.868s up to here on my machine, should be fast enough
        for i in range(n):
            self.pq.push(str(i), i, i)
        for i in range(n):
            self.assertEqual(self.pq.pop(), i)

    def test_mass_lookup(self):
        n = 1000000 #with all 5.418s
        for i in range(n):
            self.pq.push(str(i), i, i)
        for i in range(n):
            self.assertEqual(self.pq.get(str(i)), i)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPriorityQueue)
    unittest.TextTestRunner(verbosity=0).run(suite)