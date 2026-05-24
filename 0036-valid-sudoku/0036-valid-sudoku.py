class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        box_sets = [set() for _ in range(9)]

        for rowNum, row in enumerate(board):
            for colNum, cell in enumerate(row):
                if cell != ".":
                    print(f'{rowNum} {colNum}: {cell}')
                    if cell in row_sets[rowNum]:
                        print(f'exist! rowNum: {rowNum} {row_sets}')
                        return False
                    row_sets[rowNum].add(cell)

                    if cell in col_sets[colNum]:
                        print(f'exist! colNum: {colNum} {col_sets}')
                        return False
                    col_sets[colNum].add(cell)

                    boxNum = 3 * (colNum // 3) + (rowNum // 3)

                    if cell in box_sets[boxNum]:
                        print(f'exist! boxNum: {boxNum} {box_sets}')
                        return False
                    box_sets[boxNum].add(cell)


        return True

                    






        