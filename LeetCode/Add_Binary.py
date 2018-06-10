#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0.
#
#Example 1:
#Input: a = "11", b = "1"
#Output: "100"
#
#Example 2:
#Input: a = "1010", b = "1011"
#Output: "10101"


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = ""
        
        while i >= 0 or j >= 0 or carry:
            carry += 1 if i >= 0 and ord(a[i]) - ord('0') else 0
            carry += 1 if j >= 0 and ord(b[j]) - ord('0') else 0
            res = str(carry % 2) + res 
            
            carry //= 2
            i -= 1
            j -= 1
            
        return res
