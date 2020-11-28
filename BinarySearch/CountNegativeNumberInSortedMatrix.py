# Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
# Return the number of negative numbers in grid

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            count += self.getNumberOfNegatives(row)
            print(count)
        return count


    def getNumberOfNegatives(self, row):
        if row[-1] >=0:
            return 0
        if row[0] <0:
            return len(row)

        l=0
        r =len(row)-1
        while l<=r:
            if l==r:
                return len(row) - l
            if r == l+1:
                return len(row)-l if row[l] < 0 else len(row)-r

            m = int( (l+r)/2)
            l = m if row[m] >= 0 else l
            r = m if row[m] < 0 else r
