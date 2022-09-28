nums = []

for _ in range(10):
    n = int(input('numero: '))
    nums.append(n)

print(sum(nums[::2]))
