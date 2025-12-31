from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row_idx in range(9):
            for col_idx in range(9):
                if (value := board[row_idx][col_idx]) == ".":
                    continue
                if (
                    value in rows[row_idx]
                    or value in columns[col_idx]
                    or value in squares[(row_idx // 3, col_idx // 3)]
                ):
                    return False
                rows[row_idx].add(value)
                columns[col_idx].add(value)
                squares[(row_idx // 3, col_idx // 3)].add(value)
        return True


input_matrix = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

Solution().isValidSudoku(input_matrix)
