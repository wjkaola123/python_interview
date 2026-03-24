from typing import List


# 深度优先搜索
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = []
        path = []
        index_list = []
        ans_index = []
        m = len(board)
        n = len(board[0])

        def dfs(board, i, j, index):

            if index == len(word):  # 找到word 的边界, 找到了
                ans.append("".join(path.copy()))
                ans_index.append(index_list.copy())
                return

            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return  # 到达搜索边界, 停止遍历

            if board[i][j] == word[index]:
                path.append(board[i][j])
                board[i][j] = ""  # 标记已访问
                index_list.append((i, j))
                dfs(board, i + 1, j, index + 1)  # 下
                dfs(board, i - 1, j, index + 1)  # 上
                dfs(board, i, j + 1, index + 1)  # 右
                dfs(board, i, j - 1, index + 1)  # 左
                board[i][j] = word[index]  # 恢复现场
                path.pop()  # 恢复现场
                index_list.pop()

        for i in range(m):
            for j in range(n):
                dfs(board, i, j, 0)

        if ans:
            return ans[0] == word
        return False


# s = Solution()
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
# print(s.exist(board, word))
#
# board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "SEE"
# print(s.exist(board1, word))
#
# board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
# print(s.exist(board2, word))
#
# board3 = [["a"]]
# word = "a"
# print(s.exist(board3, word))


class Solution2:
    def exist(self, board: List[List[str]], word: str) -> (bool, list):
        path = []
        ans_path = []

        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
                return False

            path.append((i, j))

            if k == len(word) - 1:
                ans_path.append(path.copy())
                return True

            board[i][j] = ''
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = word[k]
            path.pop()
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True, ans_path
        return False, []


s = Solution2()
# board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
# print(s.exist(board, word))
#
board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "SEE"
print(s.exist(board1, word))
#
#
# board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
# print(s.exist(board2, word))
