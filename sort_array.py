def sort_array():
    arr_1 = [85, 5, 21, 82, 54, 17, 15]
    for i in range(len(arr_1)):
        for j in range(1, len(arr_1)):
            if arr_1[j] <= arr_1[j - 1]:
                arr_1[j], arr_1[j - 1] = arr_1[j - 1], arr_1[j]
    print(arr_1)


sort_array()