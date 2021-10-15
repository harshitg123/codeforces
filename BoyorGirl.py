st = input()
lis = []
count = 0

for i in st:
    
    if i in lis:
        pass
    else:
        lis.append(i)
        count = count + 1
        
if count % 2 == 0:
    print("CHAT WITH HER!")
    
else:
    print("IGNORE HIM!")
