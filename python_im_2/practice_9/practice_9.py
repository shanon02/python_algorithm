# testcase 1
# nums = [4,3,2,7,8,2,3,1]  # [5, 6]

# testcase 2
nums = [1, 1]  # [2]

# 아래에 코드를 작성해주세요.
list1 = []
for i in range(1, len(nums)+1):
    if i not in nums:
        list1.append(i)

print(list1)