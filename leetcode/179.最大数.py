"""
给定一组非负整数， 重新排列它们的顺序使之成为最大的整数
input [10,2]
output '210'
"""


def _compare(a, b):
    return int(str(a) + str(b)) < int(str(b) + str(a))


def largestNumber(nums):
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if _compare(nums[j], nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    if all(num == 0 for num in nums):
        return '0'
    return ''.join(str(num) for num in nums)


if __name__ == '__main__':
    nums = ['20', '30', '3', '6', '4']
    print(largestNumber(nums))


class LargerNumKey(str):
    def __lt__(x, y):
        a = x + y > y + x
        return x + y > y + x


class Solition:
    def largestNumber(self, nums):
        a = map(str, nums)
        c = sorted(a, key=LargerNumKey)
        largest_num = ''.join(c)
        # largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    nums = [2, 30, 3, 6, 4]
    print(Solition().largestNumber(nums))
