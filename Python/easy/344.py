"""
344. Reverse String
    Write a function that takes a string as input and returns the string reversed.

Example:
    Given s = "hello", return "olleh".
"""


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


if __name__ == "__main__":
    print(Solution().reverseString("hello") == "olleh")