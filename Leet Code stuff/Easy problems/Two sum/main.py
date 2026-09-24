nums = [2,5,5,11]
target = int(10)

final_numbers = []
for n in range(len(nums)):
    for j in range(n + 1, len(nums)) :
        if nums[n] + nums[j] == target and len(final_numbers) != 2:
            final_numbers = [n, j]

print(final_numbers)