class Solution(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        result = list()
        lookup = {}
        for i in range(len(nums)):
            for j in range( i+1 , len(nums)):
                if nums[i] + nums[j] in lookup:
                    lookup[nums[i]+nums[j]].append((i,j))
                else:
                    lookup[nums[i]+nums[j]] = [(i,j)]

        for i in range(len(nums)):
            for j in range( i+1, len(nums)):
                diff = target - (nums[i] + nums[j])
                if diff in lookup:
                    for index in lookup[diff]:
                        if index[0] > j:
                            if not sorted([nums[i] , nums[j], nums[index[0]], nums[index[1]]]) in result:
                                result.append(sorted([nums[i] , nums[j], nums[index[0]], nums[index[1]]]))
        return result;

class Solution1(object):
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return [];
        result = list();
        map = {};

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] in map:
                    map[nums[i] + nums[j]].append((i, j));
                else:
                    map[nums[i] + nums[j]] = [(i, j)];

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                difference = target - (nums[i] + nums[j]);
                if difference in map:
                    for index in map[difference]:
                        if index[0] > j:
                            if not sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]]) in result:
                                result.append(sorted([nums[i], nums[j], nums[index[0]], nums[index[1]]]))
        #print result;
        return result;


#print Solution().fourSum([1, 0, -1, 0, -2, 2], 0)
print Solution().fourSum([-3, -2, -1, 0 ,0 ,1, 2,3], 0)
print Solution1().fourSum([-3, -2, -1, 0 ,0 ,1, 2,3], 0)