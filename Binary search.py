num = [7,10,12,14,16,20,29,37]
print("List =", num)

def binarySearch(arr, l, r, x):
 
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)

print("Num: 14 (array) =", binarySearch(num, 0, len(num)-1, 14))
print("Num: 29 (array) =", binarySearch(num, 0, len(num)-1, 29))