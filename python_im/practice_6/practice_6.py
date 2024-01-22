# testcase 1
# array = [7, 77, 17]  # 4

# testcase 2
array = [10, 29]  # 0


def solution(array):
    list_to_str = ' '.join(map(str, array))
    seven_cnt = list_to_str.count('7')
    return seven_cnt


print(solution(array))