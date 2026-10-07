class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        for num in range(left, right + 1):
            binary = bin(num)[2:]
            set_bits = binary.count("1")

            is_prime = True

            if set_bits < 2:
                is_prime = False

            else:
                for i in range(2, set_bits):
                    if set_bits % i == 0:
                        is_prime = False
                        break
                if is_prime == True:
                    count +=1
        return count