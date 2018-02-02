"""
521. Longest Uncommon Subsequence I
Given a group of two strings,
you need to find the longest uncommon subsequence of this group of two strings.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings
and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence
by deleting some characters without changing the order of the remaining elements.
Trivially, any string is a subsequence of itself and an empty string is a subsequence of any string.

The input will be two strings,
and the output needs to be the length of the longest uncommon subsequence.
If the longest uncommon subsequence doesn't exist, return -1.

Input:
    "aba", "cdc"
Output:
    3
Explanation:
    The longest uncommon subsequence is "aba" (or "cdc"),
    because "aba" is a subsequence of "aba",
    but not a subsequence of any other strings in the group of two strings.
Note:
    1.Both strings' lengths will not exceed 100.
    2.Only letters from a ~ z will appear in input strings.

找最长的与a，b均不同的子序列
构造所求序列：
每一位找除了a，b串该位的字母外的任意字母即可，即最长序列的长度为a，b中长度的最大值
"""


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        else:
            return max(len(a), len(b))