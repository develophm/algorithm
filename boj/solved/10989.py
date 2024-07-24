import sys
input = sys.stdin.readline

N = int(input())
nums = [0] * 10001
for i in range(N):
    nums[int(input())] += 1

for i in range(1, len(nums)):
    if nums[i] == 0:
        continue
    for j in range(nums[i]):
        print(i)
