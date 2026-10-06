class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31 - 1

        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            value = divisor
            count = 1

            while dividend >= value + value:
                value += value
                count += count

            dividend -= value
            quotient += count

        if negative:
            quotient = -quotient

        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX

        return quotient
