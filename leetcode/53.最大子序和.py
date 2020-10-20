"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
input: [-2,1,-3,4,-1,2,1,-5,4]
output: 6
"""


def maxSubArray(nums: list):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + max(nums[i - 1], 0)
    return max(nums)

