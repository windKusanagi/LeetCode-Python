class Solution(object):
    def threeSumClosest(self, nums , target):
        nums.sort();
        result  = 0;
        mind = 2**31-1;
        for i in range(len(nums)-2):
            j = i+1;
            k = len(nums)-1;
            while j < k:
                sum = nums[i] + nums[j] + nums[k];
                if sum == target:
                    return target;

                if abs(target - sum) < mind:
                    mind = abs(target - sum);
                    result = sum;
                elif sum > target:
                    k-=1;
                else:
                    j+=1;

        return result;

print Solution().threeSumClosest([1, 1, 1, 1], -100)