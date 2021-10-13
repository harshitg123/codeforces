def noOfRowChange(arr):
    global row
    row = 0
    for k in range(5):
        if(any(arr[k])):
            if row == 0 or row == 4:
                return 2
            elif row == 1 or row == 3:
                return 1
            else:
                return 0
        else:
            row = row + 1
            
def noOfColumnChnange(arr, index):
    temp = 0
    for l in arr[index]:
        if l == 1:
            if temp == 0 or temp == 4:
                return 2
            elif temp == 1 or temp == 3:
                return 1
            else:
                return 0
        else:
            temp = temp + 1
    
array = [[int(i) for i in input().split(" ")] for _ in range(5)]
count = noOfRowChange(array)
count = noOfColumnChnange(array, row) + count
print(count)
 
