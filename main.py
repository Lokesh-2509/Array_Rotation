def rotate_array(arr, B):
    n = len(arr)
    B = B % n 
    return arr[-B:] + arr[:-B]
A1 = [1, 2, 3, 4]
B1 = 2
print(rotate_array(A1, B1))
A2 = [2, 5, 6]
B2 = 1
print(rotate_array(A2, B2))
