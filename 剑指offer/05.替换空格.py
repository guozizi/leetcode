"""
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

输入：s = "We are happy."
输出："We%20are%20happy."

"""


def replace_space(s: str):
    tmp = []
    for i in s:
        if i == ' ':
            tmp.append('%20')
        else:
            tmp.append(i)
    return ''.join(tmp)
