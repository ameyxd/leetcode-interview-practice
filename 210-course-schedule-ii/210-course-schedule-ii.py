class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Using topological sort: start with nodes with 0 indegree, add to queue and process neighbors by reducing their indegrees by 1
        
        adj = {i: [] for i in range(numCourses)}
        indegree = {}
        for course, prereq in prerequisites:
            indegree[course] = indegree.get(course, 0) + 1
            adj[prereq].append(course)
            
        queue = collections.deque([k for k in range(numCourses) if k not in indegree.keys()])
        top_sort_res = []
        
        while queue:
            course = queue.popleft()
            for prereq in adj[course]:
                indegree[prereq] -= 1
                if indegree[prereq] == 0:
                    queue.append(prereq)
            top_sort_res.append(course)

        return top_sort_res if len(top_sort_res) == numCourses else [] #Else there is a cycle