class Solution(object):
    def reverse(self, x):
        if(x == 0):
            return 0;
        str1 = str(x);
        result = 0;
        flag = 1;
        if( x<0 ):
            str1 = str1[1:];
            flag = 0;
        while(str1[len(str1)-1] == '0'):
            str1 = str1[0:len(str1)-1];

        str2 = str1[::-1];
        if(int(str2) > 2147483647):
            return 0;

        if(flag == 0):
            result = "-" + str2;
        else:
            result = str2;

        return int(result);

print Solution().reverse(1534236469);
