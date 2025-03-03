# an application or implementation of Quick-sort algorithm
from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right, middle = [], [], []

        for num in nums:
            if num > pivot:
                right.append(num)
            elif num < pivot:
                left.append(num)
            else:
                middle.append(num)

        return left + middle + right
        # recursive left, right => become quick-sort algorithm
        # picking a pivot firstly, then do the above work