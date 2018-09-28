"""
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

因为最后累加到个位数，所有答案只能是0~9，
很容易得出规律
0-9：  0，1，2，3，4，5，6，7，8，9
10-19：1，2，3，4，5，6，7，8，9，1
20-29：2，3，4，5，6，7，8，9，1
...
除了特殊的0，其他1-9都是依次出现
"""



class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 1 + (num - 1) % 9
