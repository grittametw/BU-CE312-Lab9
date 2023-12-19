num = [7,10,12,14,16,20,29,37]
print("List =", num)

def linearsearch(arr,n):

   for i in range(len(arr)):

       if arr[i] == n:
            return i

   return 0
    
print("Num: 14 (array) =", linearsearch(num,14))
print("Num: 29 (array) =", linearsearch(num,29))