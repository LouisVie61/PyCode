# constraints: max length of an array could have is 100 elements
# brute-force way
# for rotated sorted array, there is a way to solve the problem related to that, it is creating a breaking point
# the breaking point will check the perspective of a sorted array that will be definitely one (1) for them when
# rotating the array. Otherwise, if it is more than one (1), it's not a rotated sorted array.
# exploit this aspect, handle the subtask -> duplicate elements could appear in the input
from typing import List


def check(self, nums: List[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return True

    break_point = 0

    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            continue

        if nums[i] > nums[i + 1]:
            break_point += 1

        if break_point > 1:
            return False

    if break_point == 1:
        return nums[n - 1] <= nums[0]
    else:
        return True