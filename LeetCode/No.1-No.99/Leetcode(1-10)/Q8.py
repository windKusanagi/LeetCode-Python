class Solution(object):
    def myAtoi(self, str):

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        if not str:
            return 0

        str = str.strip();
        if not str:
            return 0;

        flag = 1;
        if str[0] in ['+', '-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]

        if not str or not str[0].isdigit():
            return 0

        for i, v in enumerate(str):
            if not v.isdigit():
                str = str[:i]
                break
        result = 0
        for d in str:
            result += ord(d) - ord('0')
            result *= 10
        result /= 10

        result *= flag

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result

