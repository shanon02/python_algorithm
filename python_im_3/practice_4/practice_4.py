# testcase 1
nums1, nums2 = [1,2,3], [2,4,6]  # [[1,3],[4,6]]

# testcase 2
# nums1, nums2 = [1,2,3,3], [1,1,2,2]  # [[3], []]

# 아래에 코드를 작성해주세요.
answer_list = [[],[]]
answer_list[0] = list(set(nums1) - set(nums2))
answer_list[1] = list(set(nums2) - set(nums1))
print(answer_list)