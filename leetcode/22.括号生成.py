"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合
input: n = 3
output: [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
"""


def generateParenthesis(n: int):
    res = set(['()'])
    for i in range(n - 1):
        tmp = set()
        for r in res:
            tmp.update(set(r[:j] + '()' + r[j:] for j in range(len(r))))
        res = tmp
    return list(res)


print(generateParenthesis(3))
