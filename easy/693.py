"""
693. Binary Number with Alternating Bits
Given a positive integer, check whether it has alternating bits:
namely, if two adjacent bits will always have different values.

Input:
    5
Output:
    True
Explanation:
    The binary representation of 5 is: 101
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        # for i in range(len(n)-1):
        #     if n[i] == n[i+1]:
        #         return False
        # return True
        return all(n[i] != n[i+1]
                   for i in range(len(n)-1))


if __name__ == "__main__":
    print(Solution().hasAlternatingBits(5) == True)
    print(Solution().hasAlternatingBits(11) == False)