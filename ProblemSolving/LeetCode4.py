# the code is asking to implement merge sort (merge operation)
def findMedian(nums1: list, nums2: list) -> float:
    def merge(nums1: list, nums2: list) -> list:
        i = j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        res = []

        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < n1:
            res.append(nums1[i])
            i += 1

        while j < n2:
            res.append(nums2[j])
            j += 1

        return res

    mergedArr = merge(nums1, nums2)
    n = len(mergedArr)
    if n % 2 != 0:
        return float(mergedArr[n//2])

    return float(mergedArr[n // 2] + mergedArr[(n // 2) - 1]) / 2.0


nums_1 = [1,3]
nums_2 = [2]
print(findMedian(nums_1, nums_2))