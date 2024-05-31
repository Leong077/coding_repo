# -*- coding: utf-8 -*-
"""
@Time :2024/5/31 20:09
@Auth :Michael
@File :code02.py
@IDE :PyCharm
"""

# 栈放入括号进行匹配
def check_brackets(s: str):
    stack = []
    result = list(s)

    for i, char in enumerate(s):
        if char == '(':
            stack.append((char, i))
            result[i] = ' '
        elif char == ')':
            if stack:
                stack.pop()
                result[i] = ' '
            else:
                result[i] = '?'
        else:
            result[i] = ' '

    while stack:
        result[stack[-1][1]] = 'x'
        stack.pop()
    return ''.join(result)


s = "brh)))"
print(check_brackets(s))