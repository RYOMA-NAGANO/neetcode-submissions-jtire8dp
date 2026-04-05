class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                l = 0
                r = len(matrix[mid]) - 1
                while l <= r:
                    mid1 = l + (r - l) // 2
                    if target == matrix[mid][mid1]:
                        return True
                    elif target < matrix[mid][mid1]:
                        r = mid1 - 1
                    else:
                        l = mid1 + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
        return False