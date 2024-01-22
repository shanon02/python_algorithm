# testcase 1
# timeSeries, duration = [1, 4], 2  # 4

# testcase 2
timeSeries, duration = [1, 2], 2  # 3

# 아래에 코드를 작성해주세요.
poison_time = 0
for i in range(len(timeSeries)-1):
    if timeSeries[i] + duration > timeSeries[i+1]:
        poison_time += duration - timeSeries[i]
    else:
        poison_time += duration

poison_time += duration
print(poison_time)