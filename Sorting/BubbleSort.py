# Bubble sort algorithm

def BubbleSort(dataset):
    print("Current state: ", dataset)
    print("len:", len(dataset))

    # starts at the last index, stops at index 0 and step -1
    for i in range(len(dataset)-1,0,-1):
        for j in range(i):
            print("dataset[j]: ", dataset[j])
            print("dataset[j+1]: ", dataset[j+1])
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1]= temp
                print("Current state: ", dataset)

def main():

    list1 = [6, 20, 5, 19, 8,]# 23, 87, 41, 12]
    
    BubbleSort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()

