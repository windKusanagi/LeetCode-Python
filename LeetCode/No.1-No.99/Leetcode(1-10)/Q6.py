class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s;
        result = '';
        pos = 0;
        length = len(s)
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                while pos < length:
                    result += s[pos]
                    pos += 2 * numRows - 2
                pos = i + 1
            else:
                while pos < length:
                    result += s[pos]
                    pos += 2 * numRows - 2 * i - 2
                    if pos> length:
                        break;
                    result += s[pos]
                    pos += 2 * i
                pos = i + 1
        return result

print Solution().convert("PAYPALISHIRING", 2);

'''
# Test cases
if __name__ == "__main__":
    Solution().convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"'''