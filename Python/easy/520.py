"""
520. Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
"""


class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() or word.isupper() or word.istitle():
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().detectCapitalUse('CHINA'))
    print(Solution().detectCapitalUse('china'))
    print(Solution().detectCapitalUse('China'))
    print(Solution().detectCapitalUse('USa'))