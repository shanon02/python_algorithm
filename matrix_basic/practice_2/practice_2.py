# testcase 1
grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]  # True

# testcase 2
# grid = [[5,7,0],[0,3,1],[0,5,0]]  # False

# 아래에 코드를 작성해주세요

def get_answer(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == j or i+j == len(grid) - 1:
                if grid[i][j] == 0:
                    return False
            else:
                if grid[i][j] != 0:
                    return False

    return True
print(get_answer(grid))