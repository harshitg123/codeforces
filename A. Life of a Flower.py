# A. Life of a Flower:

# Test Cases
# 4
# 3
# 1 0 1
# 3
# 0 1 1
# 4
# 1 0 0 1
# 1
# 0

for _ in range(int(input())):
    n = int(input())
    lis = [int(i) for i in input().split()]

    life = 1
    prev = None
    for j in range(0, n):
        curr = lis[j]
        if curr==1 and (prev==None or prev==0):
            life += 1
        elif curr==1 and prev==1:
            life += 5
        elif curr==0 and prev==0:
            life = -1
            break
        prev = curr

    print(life)
