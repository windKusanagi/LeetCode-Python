class Solution(object):
    def solve(self, board):
        if not board:
            return
        stack = []
        m , n = len(board) , len(board[0])
        for i in range(n):
            if board[0][i] == 'O':
                stack.append([0,i])
            if board[m-1][i] == 'O':
                stack.append([m-1,i])
        for i in range(1, m-1):
            if board[i][0] == 'O':
                stack.append([i,0])
            if board[i][n-1] == 'O':
                stack.append([i,n-1])
        visited = [[False for __ in range(n)] for __ in range(m)]
        while stack:
            cur = stack.pop()
            visited[cur[0]][cur[1]] = True
            if cur[0] >0 and board[cur[0]-1][cur[1]] == 'O' and visited[cur[0]-1][cur[1]] == False:
                stack.append( [ cur[0]-1, cur[1]])
            if cur[0] <m-1 and board[cur[0]+1][cur[1]] == 'O'and visited[cur[0]+1][cur[1]] == False:
                stack.append( [ cur[0]+1, cur[1]])
            if cur[1] >0 and board[cur[0]][cur[1]-1] == 'O' and visited[cur[0]][cur[1]-1] == False:
                stack.append( [ cur[0], cur[1]-1])
            if cur[1] <n-1 and board[cur[0]][cur[1]+1] == 'O'and visited[cur[0]][cur[1]+1] == False:
                stack.append( [ cur[0], cur[1]+1])
        result = []
        for i in range(m):
            temp = ""
            for j in range(n):
                if visited[i][j] == True:
                    temp+='O'
                else:
                    temp+= 'X'
            board[i] = temp
        return
board1 = ["XOXOXO",
         "OXOXOX",
         "XOXOXO",
         "OXOXOX"]
board = [['X','O','X','O','X','O'],
         ['O','X','O','X','O','X'],
         ['X','O','X','O','X','O'],
         ['O','X','O','X','O','X']]
board3 = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]
Solution().solve(board3)
print board3