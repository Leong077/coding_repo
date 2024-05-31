# -*- coding: utf-8 -*-
"""
@Time :2024/5/31 20:09
@Auth :Michael
@File :code01.py
@IDE :PyCharm
"""

# 遍历目标字符串t， 在源字符串s中找相同字符的子序列
def min_subsequences(s: str, t: str):
    s_len = len(s)
    subsequences_cnt = 0

    t_idx = 0
    while t_idx < len(t):
        s_idx = 0
        prev_t_idx = t_idx

        while s_idx < s_len and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1
        # 如果一次遍历发现t中包含s中没有的字符，索引没有移动，-1
        if prev_t_idx == t_idx:
            return -1
        subsequences_cnt += 1
    return subsequences_cnt


print(min_subsequences("abc", "acdbc"))


