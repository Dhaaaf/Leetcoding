# Given an m x n matrix, return all elements of the matrix in spiral order.



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # initialize a result array
        # initialize a right, left, top, bottom variables
        # while left < right, and top < bottom
        # Iterate through and move our pointers over
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # top 2
        # right 2
        # bottom 2
        # left 1

        # 1, 2, 3,  6, 9, 8, 7, 4, 5

        while left < right and top < bottom:
            # Get top row
            for i in range(left,right):
                res.append(matrix[top][i])
            top += 1
            # Get right column
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -=1
            if (left < right and top < bottom):
                # Get bottom row
                for i in range(right -1, left - 1, -1):
                    res.append(matrix[bottom-1][i])
                bottom -=1
                # Get left column
                for i in range (bottom-1, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res
