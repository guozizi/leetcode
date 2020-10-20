"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target,找出给定目标值在
数组中的开始位置和结束位置
你的算法时间复杂度必须是 O(log n) 级别
input : nums = [5,7,7,8,8,10], target = 8
output: [3,4]
"""


def searchRange(nums, target):
    left = 0
    R = len(nums) - 1
    while left <= R:
        mid = left + (R - left) // 2
        if nums[mid] < target:  # 目标值在右侧
            left = mid + 1
            continue
        if nums[mid] > target:  # 目标值在左侧
            R = mid - 1
        if nums[mid] == target:  # 找到目标值
            left = mid
            R = mid
            while left > 0 and nums[left - 1] == nums[left]:
                left = left - 1
            while R < len(nums) - 1 and nums[R] == nums[R + 1]:
                R = R + 1
            return [left, R]
    return [-1, 1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10, 11, 12]
    print(searchRange(nums, 8))
