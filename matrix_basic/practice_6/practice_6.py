# testcase 1
# mat = [[1,0,0],[0,0,1],[1,0,0]]  # 1

# testcase 2
mat = [[1,0,0],[0,1,0],[0,0,1]]  # 3

# 아래에 코드를 작성해주세요
special_cnt = 0
for i in range(len(mat)):
    sum_row = 0
    sum_col = 0
    for j in range(len(mat[i])):
        sum_row += mat[i][j]
        sum_col += mat[j][i]
    if sum_row == 1 and sum_col == 1:
        special_cnt += 1

print(special_cnt)