"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元
素只出现一次，返回移除后数组的新长度
input: nums = [1,1,2]
output: 2
"""


def removeDuplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(removeDuplicates(nums))
