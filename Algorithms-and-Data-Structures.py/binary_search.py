

#need a sorted list to use binary search, could run quicksort on an unsorted array first then use this using a redirect in the CLI
# runtime O(log n) fast and efficient algo

def binary_search(list, target):
    first = 0
    last = len(list) -1 
    
    while first <= last:
        midpoint = (first + last) // 2
        
        if list[midpoint] == target:
            return midpoint
        #best case scenario ^
        
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint -1          
            
    return None

# the while loop is what causes the runtime to grow
def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 6)
verify(result)
           
    
         