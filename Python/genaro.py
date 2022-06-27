

input_array = [5,1,2,4,3]


def sort_array(arr):
    sorted_arr =[]
    min_value = 0
    while arr:
        for i in range(len(arr)):
            if i ==0:
                min_value=arr[i]
            if arr[i]<min_value:
                min_value=arr[i]
        arr.remove(min_value)
        sorted_arr.append(min_value)
    print(arr)
    print(sorted_arr)


sort_array(input_array)