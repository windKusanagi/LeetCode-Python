class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False;
        cutter = 1;
        while x / cutter >= 10:
            cutter *= 10;

        while x > 0:
            left = x // cutter;
            right = x % 10;

            if left != right:
                return False;

            x %= cutter
            x //= 10
            cutter /= 100

        return True