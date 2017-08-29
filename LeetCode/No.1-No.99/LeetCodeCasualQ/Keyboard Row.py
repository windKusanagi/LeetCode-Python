class Solution(object):
    def findWords(self, words):
        keyboard = [ ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'],
                     ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'],
                     ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']]
        result = []
        for i in range(len(words)):
            j, flag , judge = 1 , -1 , 1
            c = words[i][0]
            for j in range(3):
                if c in keyboard[j]:
                    flag = j
            for k in range(1,len(words[i])):
                if not words[i][k] in keyboard[flag] :
                    judge = 0
            if judge == 1:
                result.append(words[i])
        return result
print Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])