# Given two non-negative integers num1 and num2 represented as strings,
# return the product of num1 and num2, also represented as a string.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """Multiply num1 and num2. Return result as string.
        """
        # Tests for input
        assert len(num1) >= 1 and len(num1) <= 200
        assert len(num2) >= 1 and len(num2) <= 200

        return str(eval(num1) * eval(num2))
