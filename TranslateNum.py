"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
"""


def translateNum(num: int) -> int:
    """
    获取num各位数字 从右向左遍历
    如果组成的两位数大于等于10且小于等于25则可以用字母翻译
    递推公式为 f(i) = f(i-1) + f(i-2) 如果数字Xi-1Xi可以被翻译
               f(i) = f(i-1) 如果数字Xi-1Xi不可以被翻译
    :param num:
    :return:
    """
    a = b = 1
    y = num % 10
    while num != 0:
        num //= 10
        x = num % 10
        a, b = (a + b if 10 <= x * 10 + y <= 25 else a), a
        y = x
    return a
