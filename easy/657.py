"""
657. Judge Route Circle
Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string.
And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot makes a circle.
"""


class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for move in moves:
            if move == 'L':
                x -= 1
            elif move == 'R':
                x += 1
            elif move == 'U':
                y -= 1
            else:
                y += 1
        print(x, y)
        return x == 0 and y == 0


if __name__ == "__main__":
    print(Solution().judgeCircle("UD"))
    print(Solution().judgeCircle("LL"))
    print(Solution().judgeCircle("DURDLDRRLL"))