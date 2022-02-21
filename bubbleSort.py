arr = [24,25,68,75,2,5,1,3,4]
until = len(arr) 

def bubbleSort(arr, until):
    for step in range(until-1): 
        for i in range(until-1):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print(arr)


bubbleSort(arr, until)