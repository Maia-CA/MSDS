#Week1 - Module1
def Insert(arr,i):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key

def InsersionSort(arr):
    for i in range(1,len(arr)):
        Insert(arr,i)
# main
arr= [12,65,11,5,74,1241,41,4]
InsersionSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i])