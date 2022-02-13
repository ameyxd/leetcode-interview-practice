class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        visitSet = set()
        
        def dfs(course):
            # if loop exists
            if course in visitSet:
                return False
            # if course reached has no prereqs, it can be taken
            if preMap[course] == []:
                return True
            
            # Add course to visit set to keep track of if there is a loop
            visitSet.add(course)
            for pre in preMap[course]:
                if not dfs(pre): # Loop found
                    return False
            visitSet.remove(course) # Done with course and its prerequisites
            preMap[course] = []
            return True
        
        # Graph is not fully connected so run dfs on each node
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True