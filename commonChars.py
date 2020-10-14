"""
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-common-characters
"""


def commonChars(A: list) -> list:
    result = []
    temp_list = A[1:]
    for i in A[0]:
        for j in temp_list:
            if j.find(i) == -1:
                break
        else:
            for index in range(0, len(temp_list)):
                temp_list[index] = temp_list[index].replace(i, "", 1)   # 通过下标替换原本的值
            result.append(i)
    return result


A = ["bella","label","roller"]
print(commonChars(A))
