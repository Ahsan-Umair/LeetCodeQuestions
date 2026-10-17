class Solution:
    def isHappy(self, n: int) -> bool:
        number = n
        seen = set()

        while number != 1 and number not in seen:
            seen.add(number)

            total = 0
            temp = number

            while temp > 0:
                last_digit = temp % 10
                last_digit = last_digit **2
                total += last_digit

                temp = temp // 10
            number = total
        return number == 1
