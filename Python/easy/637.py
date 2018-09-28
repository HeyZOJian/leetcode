"""
637. Average of Levels in Binary Tree
Given a non-empty binary tree,
return the average value of the nodes on each level in the form of an array.

Input:
    3
   / \
  9  20
    /  \
   15   7
Output:
    [3, 14.5, 11]
Explanation:
    The average value of nodes on level 0 is 3,
    on level 1 is 14.5,
    and on level 2 is 11.
    Hence return [3, 14.5, 11].

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        queue = []
        temp = []
        s = 0
        temp.append(root)
        while len(temp):
            queue = temp
            temp = []
            s = 0
            for i in queue:
                s += i.val
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            ans.append(s / len(queue))
        return ans
