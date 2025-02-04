from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    k = 0
    index = 0
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = '_'
        else:
            nums[index] = nums[i]
            k += 1
            index += 1

    print(*nums)
    return k
