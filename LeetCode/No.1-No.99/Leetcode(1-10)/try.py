'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        lookup, index , maxlength = [-1 for i in range(128)] , -1 , 0
        for i, value in enumerate(s):
            if (lookup[ord(value)] > index):
                index = lookup[ord(value)]
            maxlength = max(maxlength, i - index)
            lookup[ord(value)] = i
        return maxlength

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcea") == 4
'''
str1 = "112345601";
#print str1[1:5];
str2 = ["hello", "heabc", "hell"];
#for strt in reversed(str1):
#    print strt;
list1 = []
for i, v in enumerate(str1):
    list1+=[str1[i]]

print list1

list2 = list( set(list1) )
print list2