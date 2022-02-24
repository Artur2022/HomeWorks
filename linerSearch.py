arr = [1, 24, 25, 1, 68, 75, 2, 5, 1, 1, 3, 4]


def search(arr, num):
    for i in arr:
        if(i == num):
            print(arr.index(i))
        else:
            print('number is not defined')


search(arr, 1)
