"""
461. Hamming Distance
The Hamming distance between two integers
is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
"""


class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # bin(x,y) :0b...
        return int(str(bin(x ^ y)[2:].count("1")))
        # z = x ^ y;
        # ans = 0;
        # for i in range(32):
        #     ans += (z&1);
        #     z >>= 1;
        # return ans;

if __name__ == "__main__":
    print(Solution().hammingDistance(1, 4))