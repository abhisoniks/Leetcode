class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while right-left >1:
            med = int((left + right) /2)
            print(right, left, med)
            if arr[med-1] <= arr[med] and arr[med+1] <= arr[med]:
                return med
            elif arr[med-1] >= arr[med] and arr[med+1] <= arr[med]:
                right=med
            elif arr[med-1] <= arr[med] and arr[med+1] >= arr[med]:
                left = med


        if left==right:
            return left
        return left if arr[left] <= arr[right] else right
        
