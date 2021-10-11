
count = 0

for i in range(int(input())):
    X = input().lower()
    
    if X == "++x" or X == "x++":
        count = count + 1
        
    else:
        count = count - 1
        
print(count)
