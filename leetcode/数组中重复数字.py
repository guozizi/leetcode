def find_repeat_number1( nums: [int]) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]:
            return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1


def find_repeat_number2(nums: List[int]) -> int:
    nums_set = set()
    for index, element in enumerate(nums):
        a.add(element)
        if index != len(nums_set)-1:
            return element


find_repeat_number1([2, 3, 1, 2, 2, 5, 3])