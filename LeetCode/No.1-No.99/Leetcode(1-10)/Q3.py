'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
'''


str1 = input()
str2= str1[0:1]
result=''
start, end , pointer , length = 0 , 1 , 2 , 2

if len(str1) == 1:
    print str1
elif len(str1) == 2 :
    if str1[0] != str1[1]:
        print str1
    else:
        print str1[1]
else:
    str2= str1[0:1]
    while pointer!= len(str1):
        if str2.find(str1[pointer]) != -1:
            if (end - start)>len:
                len = end - start
                result=str2
        else:

