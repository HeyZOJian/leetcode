"""
760. Find Anagram Mappings
Given two lists Aand B, and B is an anagram of A.
B is an anagram of A means B is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B.
A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.
"""


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        D = {x: i for i,x in enumerate(B)}
        return [D[x] for x in A]


if __name__ == "__main__":
    print(Solution().anagramMappings([12, 28, 46], [46, 12, 28]))