class Solution(object):
    def nextPermutation(self, nums):
        L = len(nums)-1
        vio, tar,  pos1, pos2= -1 , -1 , -1, -1
        flag = 0
        for i in xrange( L ):
            if nums[L-i] > nums[L-(i+1)]:
                #print "gere"
                vio = nums[L-(i+1)]
                pos1 = L-(i+1)
                print pos1
                flag = 1
                break
        if flag == 0:
            nums.reverse()
        else:
            for i in xrange( L- pos1):
                if nums[L-i] > vio:
                    tar = nums[L-i]
                    pos2 = L-i
                    break
            temp = nums[pos1]
            nums[pos1] = nums[pos2]
            nums[pos2] = temp
            nums[pos1 + 1:] = reversed(nums[pos1 + 1:])
nums1 = [1 ,2, 6 , 8 , 7 ,4 ,3 ,2 ]
#nums1 = [6 , 8 , 7 ,4 ,3 ,2 ]
Solution().nextPermutation(nums1)
print nums1
