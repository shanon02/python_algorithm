# testcase 1
# nums, n = [ 2, 5, 1, 3, 4, 7], 3  # [2, 3, 5, 4, 1, 7]

# testcase 2
# nums, n = [1,2,3,4,4,3,2,1], 4  # [1,4,2,3,3,2,4,1]

# testcase 3
nums, n = [1,1,2,2], 2  # [1,2,1,2]

# 아래에 코드를 작성해주세요.

array1 = []
for i in range(n):
    array1.append(nums[i])
    array1.append(nums[i+n])

print(array1)