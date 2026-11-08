class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Compute the half of the m x n, go to that indices
        m = len(matrix)
        n = len(matrix[0])

        def bs(arr, target):
            left = 0
            right = (m * n) - 1
            
            while left <= right:
                mid = left + (right - left) // 2

                # compute the index of mid
                row = mid // n
                col = mid % n

                if matrix[row][col] == target:
                    return True
                elif matrix[row][col] < target:
                    left = mid + 1
                else: 
                    right = mid - 1

            return False
        
        return bs(matrix, target)