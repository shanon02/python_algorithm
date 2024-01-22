# testcase 1
arr_1, arr_2 = [1, 2, 3], [2, 3, 4]
# 1 2 3
# 2 3 4
matrix_1 = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12]]  # 10 35 35

# 아래에 코드를 작성해주세요

#1번
new_arr = [arr_1, arr_2]

for i in range(2):
    for j in range(3):
        print(new_arr[i][j], end = " ")
    print()

for i in range(len(matrix_1)):
    print(sum(matrix_1[i]), end = " ")