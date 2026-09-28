class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binary_x = bin(x)[2:]
        binary_y = bin(y)[2:]
        len_x = len(binary_x)
        len_y = len(binary_y)

        length = max(len_x, len_y)

        binary_x = binary_x.zfill(length)
        binary_y = binary_y.zfill(length)

        count = 0

        for i in range(len(binary_x)):
            if binary_x[i] != binary_y[i]:
                count +=1
        return count