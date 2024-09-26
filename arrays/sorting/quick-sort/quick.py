def partition(arr,start,end):
    i = -1;
    j = 0;

    pivot = arr[end] # pivot element is last element of array, you can consider any element as pivot - last, first, median or any random element

    for j in range(0,end):
        if arr[j] < pivot:
            # element is smaller thnn pivot, so we will swap it with element at i+1
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]

        else:
            # element is greater than or equal to pivot, so we will not do anything, just take one j one step forward
            pass

    # j runs upto end-1, so pivot is at last, swap it for i+1 (i is the last smallest element)
    arr[i+1],arr[end] = arr[end],arr[i+1]

    return i; # here i is our pivot position

def quickSort(arr,low,high):
    if low < high: # If low become greater than high then we can't divide the array further
       # after partioning, pivot will be at its right position, all the elements less than pivot will be on left side and all elements greater than pivot will be on right side
       pivot = arr[high]

       # recursively call quick sort again for all the elements less than pivot
       quickSort(arr,low,pivot-1)
       quickSort(arr,pivot+1,high)

# Driver Code
if __name__ == "__main__":
    arr = [10,7,8,9,1]
    print("Given array is", arr)

    # Quick Sorting
    quickSort(arr,0,len(arr)-1)

    print("Sorted array is", arr)
