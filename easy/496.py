"""
496. Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2
where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Input:
    nums1 = [4,1,2], nums2 = [1,3,4,2].
Output:
    [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

题意：
假设 a = nums1[i]，a在nums2中的下标是j，即a = nums2[j]
题目要求在nums2[j]后的数字中找第一个比nums2[j]大的数，找不到则输出-1
"""

# O(n^2)
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        for num1 in nums1:
            index = list(nums2).index(num1)
            flag = 0
            for num in nums2[index:]:
                if num > num1:
                    flag = 1
                    ans.append(num)
                    break
            if flag == 0:
                ans.append(-1)
        return ans


if __name__ == "__main__":
    print(Solution().nextGreaterElement([4,1,2],[1,3,4,2]))
    print(Solution().nextGreaterElement([2,4],[1,2,3,4]))