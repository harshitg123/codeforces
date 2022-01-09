# Linear Keyboard: https://codeforces.com/problemset/problem/1607/A

for i in range(int(input())):
    poss = []
    keyboard = input()
    word = input()

    for j in word:
        for k in range(0, len(keyboard)):
            if j == keyboard[k]:
                poss.append(k+1)
                break
    sm = 0
    for l in range(0, len(poss)-1):
        first = poss[l]
        nxt = poss[l+1]
        temp = nxt - first
        if temp >= 0:
            sm = sm + temp
        else:
            sm = sm + temp*-1
    print(sm)

# Test Cases

# 5
# abcdefghijklmnopqrstuvwxyz
# hello
# abcdefghijklmnopqrstuvwxyz
# i
# abcdefghijklmnopqrstuvwxyz
# codeforces
# qwertyuiopasdfghjklzxcvbnm
# qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq
# qwertyuiopasdfghjklzxcvbnm
# abacaba
