# testcase 1
player1, player2 = [4,10,7,9], [6,5,2,3]  # 1

# testcase 2
# player1, player2 = [3,5,7,6], [8,10,10,2]  # 2

# testcase 3
# player1, player2 = [2, 3], [4, 1]  # 0

# 아래에 코드를 작성해주세요.
score1 = player1[0] + player1[1]
score2 = player2[0] + player2[1]

for i in range(2, len(player1)):
    if player1[i-1] == 10 or player1[i-2] == 10:
        score1 += player1[i] * 2
    else:
        score1 += player1[i]
    if player2[i-1] == 10 or player2[i-2] == 10:
        score2 += player2[i] * 2
    else:
        score2 += player2[i]

def game_result(score1, score2):
    if score1 > score2:
        return 1
    elif score1 < score2:
        return 2
    return 0

print(game_result(score1, score2))
print(score1)
print(score2)