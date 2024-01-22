# testcase 1
x, n = 2, 5  # [2, 4, 6, 8, 10]

# testcase 2
# x, n = 4, 3  # [4, 8, 12]

# testcase 3
# x, n = -4, 2  # [-4, -8]


def solution(x, n):
    answer = list(range(x, n*x + 1, x))
    return answer


print(solution(x,n))