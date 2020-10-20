"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素
就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额
input : [2,7,9,3,1]
output: 12
"""


"""
动态规划
当前最大累计收益 = max(前一家的收益， 前前一家的收益加上当前的收益)
状态转移方程: dp[i] = max(dp[i-1], dp[i-2]+nums[i])
"""


def rop(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    before_two = nums[0]
    before_one = max(nums[0], nums[1])

    for i in range(2, n):
        next_ = max(before_two + nums[i], before_one)
        before_two, before_one = before_one, next_

    return before_one


print(rop([2, 7, 9, 3, 1]))
