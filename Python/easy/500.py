"""
500. Keyboard Row
Given a List of words,
return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below.

https://leetcode.com/static/images/problemset/keyboard.png

Input:
    ["Hello", "Alaska", "Dad", "Peace"]
Output:
    ["Alaska", "Dad"]
Note:
    1.You may use one character in the keyboard more than once.
    2.You may assume the input string will only contain letters of alphabet.
"""


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('qwertyuiop')
        b = set('asdfghjkl')
        c = set('zxcvbnm')
        ans = []
        for word in words:
            t = set(word.lower())
            if a&t == t:
                ans.append(word)
            if b&t == t:
                ans.append(word)
            if c&t == t:
                ans.append(word)
        return ans


if __name__ == "__main__":
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]) == ["Alaska", "Dad"])