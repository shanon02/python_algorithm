# testcase 1
matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]  # True

# testcase 2
# matrix = [[1,2],[2,2]]  # False

# 아래에 코드를 작성해주세요

def get_answer(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0]) -1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False

    return True

print(get_answer(matrix))