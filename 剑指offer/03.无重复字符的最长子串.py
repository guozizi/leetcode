"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
input : "abcabcbb"
output: 3
"""

""""
滑动窗口
"""


def lengthOfLongestSubstring(s: str):
    left, right = 0, 0
    while right < len(s):
        if len(s[left:right + 1]) != len(set(s[left:right + 1])):
            left += 1
        right += 1
    return right - left


print(lengthOfLongestSubstring('abcabcbb'))
