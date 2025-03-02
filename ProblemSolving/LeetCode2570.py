# def merge2DArray(nums1: list[list], nums2: list[list]) -> list[list]:
#     i = j = 0
#     n1 = len(nums1)
#     n2 = len(nums2)
#     result = []
#     visited = set()
#
#     while i < n1 and j < n2:
#         if nums1[i][0] < nums2[j][0]:
#             if nums1[i][0] not in visited:
#                 result.append(nums1[i])
#                 visited.add(nums1[i][0])
#             else:
#                 for index in range(len(result)):
#                     if result[index][0] == nums1[i][0]:
#                         result[index][1] += nums1[i][1]
#                         break
#             i += 1
#         else:
#             if nums2[j][0] not in visited:
#                 result.append(nums2[j])
#                 visited.add(nums2[j][0])
#             else:
#                 for index in range(len(result)):
#                     if result[index][0] == nums2[j][0]:
#                         result[index][1] += nums2[j][1]
#                         break
#             j += 1
#
#     while i < n1:
#         if nums1[i][0] not in visited:
#             result.append(nums1[i])
#             visited.add(nums1[i][0])
#         else:
#             for index in range(len(result)):
#                 if result[index][0] == nums1[i][0]:
#                     result[index][1] += nums1[i][1]
#                     break
#         i += 1
#
#     while j < n2:
#         if nums2[j][0] not in visited:
#             result.append(nums2[j])
#             visited.add(nums2[j][0])
#         else:
#             for index in range(len(result)):
#                 if result[index][0] == nums2[j][0]:
#                     result[index][1] += nums2[j][1]
#                     break
#         j += 1
#
#     return result

# these code above have problems:
# Error 1: Inefficient Handling of Merging Values: iterate over result each time to find a key to update,
# which is inefficient (O(n) per lookup). Using a dictionary would be better (O(1) lookup).
# Error 2: Incorrect Handling of Duplicate Keys in nums1 and nums2
# Because I choose appends first, then update -> error of duplicate handling could occur here
# The current logic does not guarantee proper merging of elements from both lists when they have the same keys.

def imporveWay(nums1: list, nums2: list) -> list:
    result = []

    n1 = len(nums1)
    n2 = len(nums2)
    i = j = 0

    mergeDict = {}

    while i < n1 and j < n2:
        if nums1[i][0] < nums2[j][0]:
            key, value = nums1[i]
            i += 1
        elif nums1[i][0] > nums2[j][0]:
            key, value = nums2[j]
            j += 1
        else:
            key, value = nums1[i][0], nums1[i][1] + nums2[j][1]
            i += 1
            j += 1

        if key in mergeDict:
            mergeDict[key] += value
        else:
            mergeDict[key] = value

    while i < n1:
        key, value = nums1[i]
        if key in mergeDict:
            mergeDict[key] += value
        else:
            mergeDict[key] = value
        i += 1

    while j < n2:
        key, value = nums2[j]
        if key in mergeDict:
            mergeDict[key] += value
        else:
            mergeDict[key] = value
        j += 1

    result = [[k, v] for k, v in sorted(mergeDict.items())]
    return result

# test:
nums1 = [[1,2],[2,3],[4,5]]
nums2 = [[1,4],[3,2],[4,1]]
print(imporveWay(nums1, nums2))
