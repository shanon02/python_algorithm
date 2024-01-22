# testcase 1
# mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 25

# testcase 2
mat = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]  # 8

# testcase 3
# mat = [[5]]  # 5

# 아래에 코드를 작성해주세요
def solution(mat):
    sum = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or i+j == len(mat) -1:
                sum += mat[i][j]
    return sum

print(solution(mat))