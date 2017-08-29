class Solution(object):
    def merge(self, nums1, m, nums2, n):
        cur = m+n -1
        l1, l2 = m -1, n-1
        while l1>=0 and l2>=0:
            if nums1[l1] > nums2[l2]:
                nums1[cur] = nums1[l1]
                l1 -= 1
            else:
                nums1[cur] = nums2[l2]
                l2 -= 1
            cur -= 1
        if l1 < l2:
            nums1[:l2+1] = nums2[:l2+1]
        print nums1

num1 = [1, 1, 2, 2, 4, 0, 0, 0, 0]
num2 = [0, 0, 2, 3]
Solution().merge(num1, 5, num2, 4)

