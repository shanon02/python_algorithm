# testcase 1
# a, b, n = 2, 1, 20  # 19

# testcase 2
a, b, n = 3, 1, 20  # 9

def solution(a, b, n):
    free_bottle_sum = 0
    while n >= a :
        free_bottle = (n // a) * b
        bottle_remain = n % a
        n = free_bottle + bottle_remain
        free_bottle_sum += free_bottle
    return free_bottle_sum


print(solution(a, b, n))
