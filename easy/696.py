"""
696. Count Binary Substrings
Give a string s,
count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input:
    "00110011"
Output:
    6
Explanation:
    There are 6 substrings that have equal number of consecutive 1's and 0's:
    "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Note:

    1.s.length will be between 1 and 50,000.
    2.s will only consist of "0" or "1" characters.

因为要求连续的0和1
所以从每处01或者10开始往左右两边统计
"""


class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]:
                a, b = i-1, i+2
                ans += 1
                while a >= 0 and b < len(s) and s[a] == s[a+1] and s[b] == s[b-1]:
                    ans += 1
                    a -= 1
                    b += 1
        return ans


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("00110011"))