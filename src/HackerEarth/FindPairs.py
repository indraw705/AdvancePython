arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
pairs = 0
for i in set(arr):
    count = arr.count(i)
    pairs = pairs + count//2

print(pairs)

