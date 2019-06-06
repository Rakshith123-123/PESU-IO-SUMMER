
string = input("enter numbers by space")
a = input("enter number to be searched")
x = int(a)
list = string.split(" ")
arr = []
for i in list :
    arr.append(int(i))
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = l + (r - l)//2; 
          
        # Check if x is present at mid 
        if arr[mid] == x: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < x: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
      
    # If we reach here, then the element was not present 
    return -1 

  
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index",result) 
else: 
    print ("Element is not present in array")