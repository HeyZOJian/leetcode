"""
476. Number Complement
Description:
    Given a positive integer, output its complement number.
    The complement strategy is to flip the bits of its binary representation.

Note:
    1.The given integer is guaranteed to fit within the range of a 32-bit signed integer.
    2.You could assume no leading zero bit in the integer’s binary representation.

Input:
    5
Output:
    2
Explanation:
    The binary representation of 5 is 101 (no leading zero bits),
    and its complement is 010. So you need to output 2.
"""
from math import log2, floor, ceil


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ ((1 << floor(log2(num)+1)) - 1)


if __name__ == "__main__":
    print(Solution().findComplement(5) == 2)
    print(Solution().findComplement(1) == 0)
    print(Solution().findComplement(2) == 1)