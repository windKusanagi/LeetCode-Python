class Solution(object):
    def findComplement(self, num):
        str1 = str(bin(num))[2::]
        length = len(str1)
        str2 = ""
        for i in range(length):
            if str1[i] == "0" :
                str2+="1"
            else:
                str2+="0"
        return int(str2 , 2)

if __name__ == "__main__":
    print Solution().findComplement(1)