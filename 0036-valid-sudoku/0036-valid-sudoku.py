class Solution:
    from collections import defaultdict
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [defaultdict(lambda: False) for _ in range(9)]
        col = [defaultdict(lambda: False) for _ in range(9)]
        sub = [defaultdict(lambda: False) for _ in range(9)]

        def get_sub_box(i, k):
            if i <= 2:
                if k <= 2:
                    return 0
                elif k <= 5:
                    return 1
                else:
                    return 2
            elif i <= 5:
                if k <= 2:
                    return 3
                elif k <= 5:
                    return 4
                else:
                    return 5
            if k <= 2:
                return 6
            elif k <= 5:
                return 7
            return 8

        for i, r in enumerate(board):
            for k, value in enumerate(r):
                if value == ".":
                    continue
                subindex = get_sub_box(i, k)
                if row[i][value]:
                    return False
                if col[k][value]:
                    return False
                if sub[subindex][value]:
                    return False
                row[i][value] = True
                col[k][value] = True
                sub[subindex][value] = True

        return True

        