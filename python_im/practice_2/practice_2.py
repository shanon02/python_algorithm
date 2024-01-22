# testcase 1
num_str = "123456789"  # 45

# testcase 2
# num_str = "1000000"  # 1


def solution(num_str):
    answer = 0
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer


print(solution(num_str))
