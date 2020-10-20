"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个
整数，并返回他们的数组下标
input : nums = [2, 7, 11, 15], target = 9
output : [0, 1]
"""


def twoSum_1(nums, target):
    for index, num in enumerate(nums):
        if (target - num) in nums[index + 1:]:
            return [index, nums[index + 1:].index(target - num) + index + 1]
    return


print(twoSum_1([3, 3], 6))


def twoSum_2(nums, target):
    if not nums:
        return None
    d = {}
    for index, num in enumerate(nums):
        tmp = target - num
        for key, value in d.items():
            if value == tmp:
                return [key, index]
        d[index] = num
    return None


print(twoSum_2([2, 3, 7, 8, 5], 9))
