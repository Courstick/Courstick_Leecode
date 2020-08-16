"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
"""


def two_sum(numbers: list, target: int) -> list:
    """暴力搜索会超出时限， 由于数组是有序的 所以可以根据和与目标值的大小关系夹逼得出位置"""
    i, j = 0, len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            return [i+1, j+1]
        elif numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
