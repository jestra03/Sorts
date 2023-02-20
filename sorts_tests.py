import unittest
from sorts import *
from heap import *


class SortingTests(unittest.TestCase):
    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

        nums = [23, 10]
        comps = bubble_sort(nums)
        self.assertEqual(comps, 2)
        self.assertEqual(nums, [10, 23])

    def test_selection_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        comps = selection_sort(nums)
        self.assertEqual(comps, 45)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])

    def test_insertion_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 26)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])

    def test_bubble_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        comps = bubble_sort(nums)
        self.assertEqual(comps, 54)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])

    def test_heap_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        heap = MaxHeap(10)
        heap.heap_sort(nums)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])

    def test_merge_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        merge_sort(nums)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])

    def test_hybrid_sort(self):
        nums = [91, 24, 24, 65, 17, 77, 74, 45, 97, 56]
        hybrid_sort(nums)
        self.assertEqual(nums, [17, 24, 24, 45, 56, 65, 74, 77, 91, 97])
        nums = [851, 814, 608, 965, 428, 874, 983, 940, 540, 856, 184, 4, 601, 945, 792, 408, 593, 695, 888, 407, 892,
                795, 152, 250, 435, 444, 427, 711, 713, 249, 561, 38, 251, 236, 768, 700, 500, 565, 483, 252, 956, 556,
                781, 971, 534, 141, 217, 721, 309, 598, 742, 25, 493, 325, 730, 109, 939, 913, 217, 678, 137, 525, 534,
                440, 793, 137, 517, 180, 624, 254, 323, 468, 604, 530, 76, 27, 395, 669, 196, 411, 640, 848, 614, 660,
                639, 746, 819, 453, 304, 667, 670, 995, 633, 811, 29, 249, 204, 232, 656, 480]
        sol = [4, 25, 27, 29, 38, 76, 109, 137, 137, 141, 152, 180, 184, 196, 204, 217, 217, 232, 236, 249, 249, 250,
               251, 252, 254, 304, 309, 323, 325, 395, 407, 408, 411, 427, 428, 435, 440, 444, 453, 468, 480, 483, 493,
               500, 517, 525, 530, 534, 534, 540, 556, 561, 565, 593, 598, 601, 604, 608, 614, 624, 633, 639, 640, 656,
               660, 667, 669, 670, 678, 695, 700, 711, 713, 721, 730, 742, 746, 768, 781, 792, 793, 795, 811, 814, 819,
               848, 851, 856, 874, 888, 892, 913, 939, 940, 945, 956, 965, 971, 983, 995]
        hybrid_sort(nums)
        self.assertEqual(nums, sol)


if __name__ == '__main__':
    unittest.main()
