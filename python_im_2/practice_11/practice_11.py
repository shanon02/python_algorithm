# testcase 1
# nums = [1, 2, 2, 3]  # True

# testcase 2
# nums = [6, 5, 4, 4]  # True

# testcase 3
nums = [1, 3, 2]  # False

# 아래에 코드를 작성해주세요.



# ascending_cnt = 0
# decending_cnt = 0
# for i in range(len(nums)-1):
#     if nums[i] < nums[i+1]:
#         ascending_cnt += 1
#     elif nums[i] > nums[i+1]:
#         decending_cnt += 1
#     else:
#         ascending_cnt += 1
#         decending_cnt += 1
#
# if ascending_cnt == len(nums) -1 or decending_cnt == len(nums) -1:
#     print("True")
# else:
#     print("False")