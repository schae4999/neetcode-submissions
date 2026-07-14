class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # current recursion path
        visiting = set()
        # completely finished
        visited = set()

        prereq_map = {course: [] for course in range(numCourses)}
        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False

            visiting.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
