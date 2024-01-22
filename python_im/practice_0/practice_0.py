# testcase 1
array = [1, 8, 3]  # [8, 1]

# testcase 2
# array = [9, 10, 11, 8]  # [11, 2]


def solution(array):
    # 아래에 코드를 작성해주세요.
    for i in range(len(array) - 1):
        if array[i]>array[i+1]:
            max_num = array[i]
            max_index = i
    answer = [max_num, max_index]
    return answer


print(solution(array))

#sol 1
max_num = max(array)
answer = [max_num, array.index(max_num)]
print(answer)

#sol 2
for i in range(len(array) - 1):
    if array[i] > array[i + 1]:
        max_num = array[i]
        max_index = i
answer = [max_num, max_index]
print(answer)