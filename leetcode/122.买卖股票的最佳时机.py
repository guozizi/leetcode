"""
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
"""


# 当天卖出以后，当天还可以买入, 所以算法可以直接简化为只要今天比昨天大，就卖出

def maxProfit(prices):
    sum = 0
    for n in range(len(prices) - 1):
        if prices[n] < prices[n + 1]:
            num = prices[n + 1] - prices[n]
            sum += num
    return sum


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(maxProfit(prices))
