# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n ==0:
            return 0
        l=1
        r=n
        m = int((l+r)/2)
        while r-l >1:
            if isBadVersion(m):
                if not isBadVersion(m-1):
                    return m
                else:
                    r = m
            else:
                l=m
            m = int((l+r)/2)
        return l if isBadVersion(l) else r        
