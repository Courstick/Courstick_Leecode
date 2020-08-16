'''
我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。

例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。

现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足 f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character
'''


class Solution:
    # def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
    def findSmallerAlphabet(self, string):
        '''
        :param string:
        :return:一个单词中最小的字母
        '''
        smaller = string[0]
        for i in string:
            if smaller == 'a':
                break
            if smaller > i:
                smaller = i
        return smaller

    def countAlphabet(self, string, alpha):
        '''
        :param string:
        :param alpha:
        :return: 最小的字母在单词中出现的次数
        '''
        count = 0
        for i in string:
            if i == alpha:
                count += 1
        return count

    def countSmallestAlphabet(self, string):
        '''
        从查找找到最小的字母开始计数
        :param string:
        :return: 次数
        '''
        smallest = 'z'
        count = 0
        for i in string:
            if smallest > i:
                smallest = i
                count = 1
            elif i == smallest:
                count += 1
        return count


    def numSmallerByFrequency(self, queries: list, words: list):
        # words词汇表中每个词的长度
        count_alpha_in_words = []
        # 存储queries中每个词的最小字母的出现频次比词汇表中小的个数
        queries_list = []
        # for i in words:
        #     count_alpha = self.countAlphabet(i, self.findSmallerAlphabet(i))
        #     count_alpha_in_words.append(count_alpha)
        # for i in queries:
        #     count = 0
        #     count_in_queries = self.countAlphabet(i, self.findSmallerAlphabet(i))
        #     for j in count_alpha_in_words:
        #         if count_in_queries < j:
        #             count += 1
        #     queries_list.append(count)

        for i in words:
            count_alpha_in_words.append(self.countSmallestAlphabet(i))
        for i in queries:
            count = 0
            count_in_queries = self.countSmallestAlphabet(i)
            for j in count_alpha_in_words:
                if count_in_queries < j:
                    count += 1
            queries_list.append(count)

        return queries_list
