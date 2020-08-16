"""
这里有 n 门不同的在线课程，他们按从 1 到 n 编号。每一门课程有一定的持续上课时间（课程时间）t 以及关闭时间第 d 天。一门课要持续学习 t 天直到第 d 天时要完成，你将会从第 1 天开始。

给出 n 个在线课程用 (t, d) 对表示。你的任务是找出最多可以修几门课。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/course-schedule-iii
"""

# 贪心
# class Solution:
#     def scheduleCourse(self, courses: List[List[int]]) -> int:
class Solution:
    def scheduleCourse(self, courses: list):
        # 先按照结束时间把课程从前到后排序
        courses = sorted(courses, key=lambda x: x[1])
        today = 0  # 记录今天是那一天
        choose_list = []
        for i in courses:
            if today + i[0] <= i[1]:
                choose_list.append(i[0])
                today = sum(choose_list)
            # 如果后面有课程时间比已选课程时间短的课程就替换之前选的最长的
            elif today and i[0] < max(choose_list):
                choose_list = sorted(choose_list)
                choose_list.pop()
                choose_list.append(i[0])
                today = sum(choose_list)
        return len(choose_list)
