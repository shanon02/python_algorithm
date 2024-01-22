# testcase 1
nums, k = [1,12,-5,-6,50,3], 4  # 12.75000

# testcase 2
# nums, k = [5], 1  # 5.00000

# 아래에 코드를 작성해주세요.

result_sum = 0
for i in range(len(nums)-k+1):
    sum = 0
    for j in range(i, i + k):
        sum += nums[j]
    if sum >=result_sum:
        result_sum = sum
result_average = result_sum/k
print(result_average)