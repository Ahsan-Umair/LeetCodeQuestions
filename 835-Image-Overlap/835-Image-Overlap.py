class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        largest_count = 0

        for row_shift in range(-(n - 1), n):
            for col_shift in range(-(n - 1), n):
                count = 0

                for i in range(n):
                    for j in range(n):
                        new_i = i + row_shift
                        new_j = j + col_shift

                        if 0 <= new_i < n and 0 <= new_j < n:

                            if img1[i][j] == 1 and img2[new_i][new_j] == 1:
                                count +=1
                largest_count = max(largest_count, count)

        return largest_count

