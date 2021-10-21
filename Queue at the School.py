n,t = input().split(" ")
st = " ".join(input())
lis = st.split(" ")
n = int(n)
t = int(t)

for i in range(t):
    index = []
    for i in range(n):
        if lis[i] == 'B':
            index.append(i)
    
    for j in range(len(index)):
        if index[j] < n-1:
            temp = lis[index[j]]
            lis[index[j]] = lis[index[j]+1] 
            lis[index[j]+1] = temp 

for i in lis:
    print(i,end="")
