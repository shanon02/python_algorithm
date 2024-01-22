# testcase 1
# nums, n = [2, 5, 1, 3, 4, 7], 3  # [2, 3, 5, 4, 1, 7]

# testcase 2
# nums, n = [1,2,3,4,4,3,2,1], 4  # [1,4,2,3,3,2,4,1]

# testcase 3
# nums, n = [1,1,2,2], 2  # [1, 2, 1, 2]

names = ["Mary","John","Emma"]
heights = [180,165,170]
#Output: ["Mary","Emma","John"]

# 아래에 코드를 작성해주세요.
for i in range(len(heights) - 1):
    if heights[i]<heights[i+1]:
        # heights[i], heights[i+1] = heights[i+1], heights[i]
        names[i], names[i + 1] = names[i + 1], names[i]
print(names)