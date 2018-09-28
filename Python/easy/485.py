"""
485. Max Consecutive Ones
Given a binary array, find the maximum number of consecutive 1s in this array.
Input:
    [1,1,0,1,1,1]
Output:
    3
Explanation:
    The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        ans = 0
        for num in nums:
            if num == 1:
               sum += 1
            else:
               ans = max(ans, sum)
               sum = 0
        return max(ans, sum)


if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1,0,1,1,0]))