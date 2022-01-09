# Two Subsequences: https://codeforces.com/problemset/problem/1602/A

# Test Cases:

# 3
# fc
# aaaa
# thebrightboiler

for _ in range(int(input())):
    temp = st = input()
    a = sorted(temp)[0]
    print(a, st.replace(a,"",1))
