# testcase 1
# accounts = [[1,2,3],[3,2,1]]  # 6

# testcase 2
accounts = [[1,5],[7,3],[3,5]]  # 10

# 아래에 코드를 작성해주세요

def richest_money(accounts):
    max_money = 0
    for i in range(len(accounts)):
        sum_money = sum(accounts[i])
        if sum_money > max_money:
            max_money = sum_money
    return max_money

print(richest_money(accounts))
