from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        p1, p2 = 0, 1
        while p2 < len(nums) and p1 < len(nums) - 1:
            if nums[p1] == nums[p2]:
                return False
            elif nums[p1]%2 == nums[p2]%2:
                return False

            p1 += 1
            p2 += 1


        return True

arr = [1, 2, 3]
s = Solution()
print(s.isArraySpecial(arr))
arr1 = [1,1, 3]
s = Solution()
print(s.isArraySpecial(arr1))
arr2 = [9,1,3]
s = Solution()
print(s.isArraySpecial(arr2))

