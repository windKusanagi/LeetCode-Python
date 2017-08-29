class Solution(object):
    def hammingDistance(self, x, y):
        str1 = str(bin(x))[2::]
        str2 = str(bin(y))[2::]
        temp =""
        if len(str2)>len(str1):
            return self.hammingDistance(y,x)
        for i in range(len(str1)-len(str2)):
            temp+= "0"
        str2 = temp + str2
        result = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                result += 1
        return result

if __name__ == "__main__":
    print Solution().hammingDistance(0,1)