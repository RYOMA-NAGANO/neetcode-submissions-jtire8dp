class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            newDigits = digits[i] + carry
            if newDigits >= 10:
                carry = 1
                digits[i] = newDigits % 10
            else:
                carry = 0
                digits[i] = newDigits
        
        if carry == 1:
            digits.append(1)
            return digits[::-1]
        else:
            return digits