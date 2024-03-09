p = 29
nums = [14, 6, 11]
results = [False, False, False]
for i in range(29):
    residue = (i**2) % 29
    for j, num in enumerate(nums):
        if (num == residue):
            print(i)
            results[j] = i
print(results)
print(-21**2 % 29)
