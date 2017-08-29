class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        #str1 = str(input());
        index = 0;
        expand = list();

        for i in range( 0 , 2*len(s)+1):
            if i%2 != 0:
                expand.append(s[index]);
                index += 1;
            else:
                expand.append('$');

        LenOfCur = list();


        for i in range(0,len(expand)):
            LenOfCur.append(0);

        start = 0;
        end = 0;
        i = 0;
        while i<len(expand):
            while  start>0 and end< (len(expand)-1) and (expand[start-1] == expand[end+1]) :
                start -= 1;
                end += 1;

            LenOfCur[i]= end-start+1;

            if end == (len(LenOfCur)-1):
                break;

            if i%2 == 0:
                nextCenter = end + 1;
            else:
                nextCenter = end ;


            for j in range (i+1 , end+1):

                LenOfCur[j] = min(LenOfCur[i - (j-i)] , 2* (end - j )+1);

                if (j+LenOfCur[i -(j-i)]/2) == end:

                    nextCenter = j;
                    break;

            i = nextCenter;
            end = i + LenOfCur[i]/2;
            start = i - LenOfCur[i]/2;

        pos = -1;
        max = -1;
        for i in range(0 , len(LenOfCur)):
            val = LenOfCur[i] /2 ;
            if max < val:
                max = val;
                pos = i;

        print max;
        print pos;
        result = list(expand[ pos - max : pos + max]);
        while result.count('$')!= 0:
            result.remove('$');
        resultStr = ''.join(result)
        return resultStr;

