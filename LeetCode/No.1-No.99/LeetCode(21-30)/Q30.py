import collections

class Solution:
     def findSubstring(self, s, words):
        result, word_num, word_len = [], len(words), len(words[0])
        worddict = collections.defaultdict(int)
        for i in words:
            worddict[i] += 1

        for i in xrange(len(s) + 1 - word_len * word_num):
            cur, j = collections.defaultdict(int), 0
            while j < word_num:
                word = s[i + j * word_len:i + j * word_len + word_len]
                if word not in words:
                    break
                cur[word] += 1
                if cur[word] > worddict[word]:
                    break
                j += 1
            if j == word_num:
                print j
                result.append(i)

        return result

if __name__ == "__main__":
    print Solution().findSubstring("barfoothefoobarman", ["foo", "bar"])