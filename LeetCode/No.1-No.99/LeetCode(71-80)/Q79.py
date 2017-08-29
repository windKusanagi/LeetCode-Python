'''
class Solution:
    def exist(self, board, word):
        visit = [[0 for __ in range(len(board[0]))] for __ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existRecu(board, word, 0, i, j, visit):
                    return True

        return False

    def existRecu(self, board, word, cur, i, j, visit):
        if cur == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visit[i][j] == 1 or board[i][j] != word[cur]:
            return False
        visit[i][j] = 1
        cur += 1
        result = self.existRecu(board, word, cur , i + 1, j, visit) or\
                 self.existRecu(board, word, cur , i - 1, j, visit) or\
                 self.existRecu(board, word, cur , i, j + 1, visit) or\
                 self.existRecu(board, word, cur , i, j - 1, visit)
        visit[i][j] = 0

        return result
'''
class Solution:
    def exist(self, board, word):
        visit = [[ 0 for __ in range(len(board[0]))] for __ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.existDF(word, 0, i, j, board, visit):
                    return True
        return False

    def existDF (self, word, cur, i, j, board, visit):
        if len(word) == cur:
            return True
        if i<0 or i>= len(board) or j<0 or j>= len(board[0]) or\
                        visit[i][j] == 1 or board[i][j] != word[cur]:
            return False
        visit[i][j] = 1
        cur += 1
        result = self.existDF(word, cur, i+1, j, board, visit) or\
                 self.existDF(word, cur, i, j+1, board, visit) or\
                 self.existDF(word, cur, i-1, j, board, visit) or\
                 self.existDF(word, cur, i, j-1, board, visit)
        visit[i][j] = 0
        return result

if __name__ == "__main__":
    board = [
              "ABCE",
              "SFCS",
              "ADEE"
            ]
    print Solution().exist(board, "ABCCED")
    print Solution().exist(board, "SFCS")
    print Solution().exist(board, "ABCB")