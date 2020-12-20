import unittest

from utils.word_counter import final_count
from utils.reader import read


class Tests(unittest.TestCase):

    def test(self):
        words = read("./wchain1.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 6)
        words = read("./wchain2.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 4)
        words = read("./wchain3.in")
        self.assertEqual(final_count(sorted(words, key=len), {}), 1)


if __name__ == '__main__':
    unittest.main()