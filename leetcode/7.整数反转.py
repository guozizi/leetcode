"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
input: 123
output: 321
"""


def reverse(x: int):
    s = int(str(abs(x))[::-1])
    if x < 0:
        anx = -s
    else:
        anx = s

    if anx in range(-2147483648, 2147483647):
        return anx
    else:
        return 0


print(reverse(-23950))
