class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n ==0:
            return 0
        l=1
        r=int(n/2)+1
        m = int((l+r)/2)
        while r-l >1:
            prod=m *(m+1)
            if prod == 2*n:
                return m
            if prod<2*n:
                l=m
            else:
                r=m
            m = int((l+r)/2)
        return r if r*(r+1) <= 2*n else l
