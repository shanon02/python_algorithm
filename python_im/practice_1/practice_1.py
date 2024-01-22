# testcase 1
num_list = [4, 2, 6, 1, 7, 6]  # 17

# testcase 2
# num_list = [-1, 2, 5, 6, 3]  # 8


def solution(num_list):
    # 아래에 코드를 작성해주세요.
    sum_odd = 0
    sum_even = 0
    for i in range(len(num_list)):
        if i%2 == 0:
            sum_odd += num_list[i]
        else:
            sum_even += num_list[i]
    if sum_odd > sum_even:
        answer = sum_odd
    else:
        answer = sum_even
    return answer


print(solution(num_list))
