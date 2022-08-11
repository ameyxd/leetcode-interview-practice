# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    # Level order BFS
    def depthSum1(self, nestedList: List[NestedInteger]) -> int:
        depth = 1
        res = 0
        queue = collections.deque()
        for nested in nestedList:
            queue.append((nested, depth))

        while queue:
            nested, depth = queue.popleft()
            if nested.isInteger():
                res += depth * nested.getInteger()
            else:
                for el in nested.getList():
                    queue.append((el, depth + 1))
        return res

    # Recursive DFS
    def depthSum2(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nestedList, depth):
            total = 0
            for nested in nestedList:
                if nested.isInteger():
                    total += depth * nested.getInteger()
                else:
                    total += dfs(nested.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)

    # Iterative DFS
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [(ni, 1) for ni in nestedList]
        count = 0
        while stack:
            nested, depth = stack.pop()
            if nested.isInteger():
                count += nested.getInteger() * depth
            else:
                for subitem in nested.getList():
                    stack.append((subitem, depth + 1))
        return count