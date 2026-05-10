class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #create adjacency list 
        graph = [[] for _ in range(numCourses)]
        for course, preq in prerequisites:
            graph[preq].append(course)
        #state list
        state = [0] * numCourses
        order = []

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for nei in graph[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2
            order.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        order.reverse()
        return order
