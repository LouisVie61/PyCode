# two sum + sorted array input
# 1 - indexed array of integer
# output need: exactly the index of these number.


def twoSum(numbers, target):
    my_map = {}

    for i in range(len(numbers)):
        rest = target - numbers[i]

        if rest in my_map:
            return [my_map[rest] + 1, i + 1]
        else:
            my_map[numbers[i]] = i


numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))