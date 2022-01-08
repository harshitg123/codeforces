# A. Linear Keyboard: https://codeforces.com/problemset/problem/1607/A

for i in range(int(input())):
    count = 0
    unique = []
    n = int(input())
    lis = [int(j) for j in input().split()]
    
    for k in range(0, n):
        
        if lis[k] not in unique:
            unique.append(lis[k])
            
        else:
            if lis[k]*-1 not in unique:
                unique.append(lis[k]*-1)

    print(len(unique))
