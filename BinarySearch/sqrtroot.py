# Implement int sqrt(int x).
# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        orig=x
        l=0
        r=orig
        while l<=r:
            if l==r:
                return l
            x = int( (l+r)/2 )
            if r==l+1:
                return l
            sq = pow(x, 2)
            if sq == orig:
                return x
            elif sq > orig:
                r=x
            else:
                l=x
