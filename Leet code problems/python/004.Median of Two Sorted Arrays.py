class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        newlist=nums1+nums2
        newlist.sort()
        l=len(newlist)
        print(newlist)
        if l%2==0:
            print(newlist[l//2-1],newlist[l//2])
            o=float((newlist[l//2-1]+newlist[l//2])/2)
            print(o)
            return o
        else:
            print("sample")
            o=newlist[l//2]
            print(o)
            return o
