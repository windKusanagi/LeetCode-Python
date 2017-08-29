'''
class Solution:
    def twoSum(self, nums, target):
        i, j =0, len(nums)-1
        while(1):
            if i == j :
                return [];
            if nums[i]+nums[j] < target:
                i+=1;
            elif nums[i]+nums[j] > target:
                j-=1;
            else:
                return [i,j]

if __name__ == "__main__":
    list1,target =input(), input();
    list2 = list(list1)
    list1.sort()
    result = [list2.index(list1[Solution().twoSum(list1,target)[0]]),list2.index(list1[Solution().twoSum(list1,target)[1]])]
    print result
    '''
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index, value in enumerate(nums):
            lookup[value] = index
        print lookup
        for i, value in enumerate(nums):
            print i, value
            if target - value in lookup:
                j = lookup[target - value]
                print i, j
                if i != j:
                    return [i, j]

print Solution().twoSum((0, 7, 7, 0), 14)
'''
'''
        if (j+T[i -(j-1)]/2) == end:
        #if(j + T[i - (j - i)]/2 == end) :
list1 = list();

for i in range(0,5):
    list1.append(0);

print len(list1);
i = 3 t =5 j = 4
'''
list1 = [1,2,3,4,5]
print list1[ :2]
print list1[2:]

MAX_INT = 2**31-1
print MAX_INT