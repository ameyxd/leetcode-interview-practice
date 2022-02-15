class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # Strat: Keep two data structures - preMap as an adjacency list hashmap and visited set - to keep track of the current path of dfs to see if there is a loop
#         preMap = {i: [] for i in range(numCourses)}
#         for course, prereq in prerequisites:
#             preMap[course].append(prereq)
            
#         visitSet = set()
        
#         def dfs(course):
#             # if loop exists
#             if course in visitSet:
#                 return False
#             # if course reached has no prereqs, it can be taken
#             if preMap[course] == []:
#                 return True
            
#             # Add course to visit set to keep track of if there is a loop
#             # Postorder DFS: First process descendants
#             visitSet.add(course)
#             for pre in preMap[course]:
#                 if not dfs(pre): # Loop found
#                     return False
#             # Postorder DFS: Then process node
#             visitSet.remove(course) # Done with course and its prerequisites
#             preMap[course] = []
#             return True
        
#         # Graph is not fully connected so run dfs on each node
#         for course in range(numCourses):
#             if not dfs(course):
#                 return False
        # return True
    
    # Another strat: Topological sort - essentially glorified way of checking cycle. If cycle is present, top sort will not be the same length as the number of vertices
            # Adjacency list
            adj = collections.defaultdict(list)
            # maintain indegree hashmap
            indegree = {}
            for course, prereq in prerequisites:
                adj[prereq].append(course)
                indegree[course] = indegree.get(course, 0) + 1
            # Only keep nodes with 0 indegree in queue at all times
            queue = collections.deque([k for k in range(numCourses) if k not in indegree.keys()])
            top_sort = []
            while queue:
                course = queue.popleft()
                top_sort.append(course)
                # For every node linking to node in queue, reduce its indegree by 1 and add to queue if its indegree becomes 0
                for prereq in adj[course]:
                    indegree[prereq] -= 1
                    if indegree[prereq] == 0:
                        queue.append(prereq)
            # If topological sort is not the length of the number of nodes, there was a cycle
            return len(top_sort) == numCourses