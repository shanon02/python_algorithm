# testcase 1
a, b = 3, 5  # 34

# testcase 2
# a, b = 6, 1  # 14

# testcase 3
# a, b = 2, 4  # 2


def solution(a, b):
    if a%2 == 1 and b%2 == 1:
        score = a**2 + b**2
    elif a%2 == 1 or b%2 ==1:
        score = 2*(a+b)
    else:
        score = abs(a-b)
    return score


print(solution(a, b))
