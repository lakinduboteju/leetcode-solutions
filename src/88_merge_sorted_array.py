from typing import List


# Question : 88. Merge Sorted Array
# URL : https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        next_to_be_set_idx = m + n - 1

        next_nums1_idx = m - 1
        next_nums2_idx = n - 1

        while next_to_be_set_idx > -1:
            if next_nums1_idx > -1 and next_nums2_idx > -1:
                num1 = nums1[next_nums1_idx]
                num2 = nums2[next_nums2_idx]

                if num2 > num1:
                    nums1[next_to_be_set_idx] = num2
                    next_nums2_idx -= 1
                else:
                    nums1[next_to_be_set_idx] = num1
                    next_nums1_idx -= 1

            elif next_nums1_idx > -1:
                nums1[next_to_be_set_idx] = nums1[next_nums1_idx]
                next_nums1_idx -= 1

            else:
                nums1[next_to_be_set_idx] = nums2[next_nums2_idx]
                next_nums2_idx -= 1

            next_to_be_set_idx -= 1

        return None


solution = Solution()

args = (
    [1, 2, 3, 0, 0, 0], 3,
    [2, 5, 6], 3,
)
solution.merge(*args)
print(args)

args = (
    [1], 1,
    [], 0,
)
solution.merge(*args)
print(args)

args = (
    [0], 0,
    [1], 1,
)
solution.merge(*args)
print(args)

args = (
    [2,0], 1,
    [1], 1,
)
solution.merge(*args)
print(args)

args = (
    [4,5,6,0,0,0], 3,
    [1,2,3], 3,
)
solution.merge(*args)
print(args)

args = (
    [4,0,0,0,0,0], 1,
    [1,2,3,5,6], 5,
)
solution.merge(*args)
print(args)

args = (
    [1,2,4,5,6,0], 5,
    [3], 1,
)
solution.merge(*args)
print(args)
