"""
575. Distribute Candies
Given an integer array with even length,
where different numbers in this array represent different kinds of candies.
Each number means one candy of the corresponding kind.
You need to distribute these candies equally in number to brother and sister.
Return the maximum number of kinds of candies the sister could gain.

Input:
    candies = [1,1,2,2,3,3]
Output:
    3
Explanation:
    There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
    Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
    The sister has three different kinds of candies.

贪心：
当糖果种类大于糖果数一半时，由于糖果要平均分所有女孩的糖果种类最多为糖果数一半
当糖果种类小于糖果数一半时，优先将所有种类的糖果都给一颗给女孩然后再补，最终女孩手中有所有的糖果种类
"""


class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) // 2, len(set(candies)))


if __name__ == "__main__":
    print(Solution().distributeCandies([1,1,2,2,3,3]) == 3)
    print(Solution().distributeCandies([1,1,2,3]) == 2)
    print(Solution().distributeCandies([1,11]) == 1)
    print(Solution().distributeCandies([1,1,11,11]) == 2)
    print(Solution().distributeCandies([1000,1,1,1]) == 2)
    print(Solution().distributeCandies([0,0,14,0,10,0,0,0]) == 3)