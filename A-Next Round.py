n,k = input().split(" ")

n = int(n)
k = int(k)
count = 0

lis = [int(i) for i in input().split(" ")]

for i in lis:
    if i >= lis[k-1] and i > 0:
        count = count + 1

print (count)
