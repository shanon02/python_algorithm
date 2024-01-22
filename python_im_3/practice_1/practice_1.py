# testcase 1
words, pref = ["pay","attention","practice","attend"], "at"  # 2

# testcase 2
# words, pref = ["leetcode","win","loops","success"], "code"  # 0

# 아래에 코드를 작성해주세요.
pref_cnt = 0
accord_cnt = 0
for i in range(len(words)):
    for j in range(len(pref)):
        if(words[i][j] != pref[j]):
            break
        else:
            accord_cnt += 1
    if accord_cnt == len(pref):
        pref_cnt += 1
print(pref_cnt)