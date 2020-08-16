"""
在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。

最终结果按照字典顺序输出。

链接：https://leetcode-cn.com/problems/positions-of-large-groups
"""


class Solution:
    def largeGroupPositions(self, S: str):
        length = len(S)
        S = list(S)
        i, j = 0, 1
        result_list = list()
        while True:
            if j == length:
                if j - i >= 3:
                    result_list.append([i, j - 1])
                break
            if S[i] != S[j] and j - i < 3:
                i = j
                j += 1
            elif S[i] != S[j] and j - i >= 3:
                result_list.append([i, j - 1])
                i, j = j, j + 1
            elif S[i] == S[j]:
                j += 1
        return result_list
