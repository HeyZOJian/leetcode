"""
766. Toeplitz Matrix
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Input:
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output:
    True
Explanation:
    1234
    5123
    9512
In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]",
and in each diagonal all elements are the same, so the answer is True.

Input:
    matrix = [[1,2],[2,2]]
Output:
    False
Explanation:
    The diagonal "[1, 2]" has different elements.

Note:
    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].

利用处于同一条对角线上的x,y坐标的差值是相同的性质判断同一条对角线的值是否相同
enumerate同时获得索引和值
"""


class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r - c not in groups:
                    groups[r - c] = val
                elif groups[r - c] != val:
                    return False
        return True

if __name__ == "__main__":
    print(Solution().isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) == True)
    print(Solution().isToeplitzMatrix([[1, 2], [2, 2]]) == False)