# testcase 1
matrix = [[1,2,3],[4,5,6],[7,8,9]]  # [[1,4,7],[2,5,8],[3,6,9]]

# testcase 2
# matrix = [[1,2,3],[4,5,6]]  # [[1,4],[2,5],[3,6]]

# 아래에 코드를 작성해주세요
def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_arr = [[0 for j in range(rows)] for i in range(cols)]
    for i in range(len(new_arr)):
        for j in range(len(new_arr[0])):
            new_arr[i][j] = matrix[j][i]
    return new_arr

print(solution(matrix))