# testcase 1
# a, b = [1, 2, 3, 4] , [-3, -1, 0, 2]  # 3

# testcase 2
a, b = [-1, 0, 1] , [1, 0, -1]  # -2


def solution(a, b):
    inner_product = 0
    for i in range(len(a)):
        inner_product += a[i] * b[i]
    return inner_product


print(solution(a, b))
