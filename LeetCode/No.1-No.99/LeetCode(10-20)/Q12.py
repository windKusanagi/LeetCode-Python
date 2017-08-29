class Solution(object):
    def intToRoman(self, num):

        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
        strings = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
        pos=0;
        result = "";
        while num>0:
            if ( num - nums[pos] )>=0:
                num = num - nums[pos];
                result+= strings[pos];
            else:
                pos+=1;

        return result;

print Solution().intToRoman(99);

