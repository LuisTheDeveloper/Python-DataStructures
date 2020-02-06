# implementing merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 47, 41, 87, 1]

def mergesort(dataset):
    # split the data set argument into two arrays
    if len(dataset)>1: # breaking condition when we have one element array
        mid = len(dataset) // 2 # mid point of the dataset
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]
        #print("leftarr:", leftarr)
        #print("rightarr:", rightarr)
        mergesort(leftarr)
        mergesort(rightarr)

        # Merging process:

        i=0 # left array index
        j=0 # right array index
        k=0 # merged array index

        # while both have values
        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                dataset[k] = leftarr[i]
                i += 1
            else: 
                dataset[k] = rightarr[j]
                j += 1
            k += 1

        # if the left array still have values
        while i < len(leftarr):
            dataset[k] = leftarr[i]
            i += 1
            k += 1

        while j < len(rightarr):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

print(items)
mergesort(items)
print(items)
