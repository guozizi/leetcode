"""
给定一个整数数组，寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序，找到子数组最短，输出它的长度
input: [2,6,4,8,10,9,15]
output: 5  --> len([6,4,8,10,9])
"""


def findUnsortedSubarray(nums) -> int:
    diff = [i for i, (a, b) in enumerate(zip(nums, sorted(nums))) if a != b]
    return len(diff) and max(diff) - min(diff) + 1


print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
