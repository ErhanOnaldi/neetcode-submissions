class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[b].append(a)
            

        status = [0] * numCourses

        def dfs(course):
            if status[course] == 1:
                return False
            if status[course] ==2:
                return True
            
            status[course] = 1

            for i in adj[course]:
                if not dfs(i):
                    return False
            status[course] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True