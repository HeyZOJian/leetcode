"""
557. Reverse Words in a String III

Description:
    Given a string, you need to reverse the order of characters in each word
    within a sentence while still preserving whitespace and initial word order.

Input:
    "Let's take LeetCode contest"
Output:
    "s'teL ekat edoCteeL tsetnoc"

Note:
    In the string, each word is separated by single space
    and there will not be any extra space in the string.
"""


class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ans = ""
        # for str in s.split():
        #     ans += (str[::-1])+" "
        # return ans[:ans.__len__()-1]
        return " ".join(x[::-1] for x in s.split())


if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))