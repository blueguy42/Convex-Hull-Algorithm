from heapq import merge
import numpy as np
import math

ayy = ([[6.3, 3.3], [5.8, 2.7], [7.1, 3.0], [6.3, 2.9], [6.5, 3.0], [7.6, 3.0], [4.9, 2.5], [7.3, 2.9], [6.7, 2.5], [7.2, 3.6], [6.5, 3.2], [6.4, 2.7], [6.8, 3.0], [5.7, 2.5], [5.8, 2.8], [6.4, 3.2], [6.5, 3.0], [7.7, 3.8], [7.7, 2.6], [6.0, 2.2], [6.9, 3.2], [5.6, 2.8], [7.7, 2.8], [6.3, 2.7], [6.7, 3.3], [7.2, 3.2], [6.2, 2.8], [6.1, 3.0], [6.4, 2.8], [7.2, 3.0], [7.4, 2.8], [7.9, 3.8], [6.4, 2.8], [6.3, 2.8], [6.1, 2.6], [7.7, 3.0], [6.3, 3.4], [6.4, 3.1], [6.0, 3.0], [6.9, 3.1], [6.7, 3.1], [6.9, 3.1], [5.8, 2.7], [6.8, 3.2], [6.7, 3.3], [6.7, 3.0], [6.3, 2.5], [6.5, 3.0], [6.2, 3.4], [5.9, 3.0]])

def kirikanan_garis(arr, p1, pn, px):
    '''Memeriksa apakah sebuah titik berada di sebelah kiri atau
    kanan garis. Bila sebelah kiri maka hasil positif menggunakan
    penentuan determinan'''

    x1 = arr[p1][0]; y1 = arr[p1][1]; x2 = arr[pn][0]; y2 = arr[pn][1]; x3 = arr[px][0]; y3 = arr[px][1]

    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3


def jarak(arr, p1, pn, px):
    '''Memeriksa jarak titik px ke garis p1, pn'''

    x1 = arr[p1][0]; y1 = arr[p1][1]; x2 = arr[pn][0]; y2 = arr[pn][1]; x3 = arr[px][0]; y3 = arr[px][1]
    
    return abs(((x2-x1)*(y1-y3)-(x1-x3)*(y2-y1))/math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)))

def sudut(a, b, c):
    '''Mengembalikan sudut dari segitiga ABC dengan B sudut yang terapit'''

    # https://manivannan-ai.medium.com/find-the-angle-between-three-points-from-2d-using-python-348c513e2cd
    ba = a - b; bc = c - b

    cosine_angle = np.dot(ba, bc)/(np.linalg.norm(ba)*np.linalg.norm(bc))
    return np.degrees(np.arccos(cosine_angle))


# def sudut(a, b, c):
#     ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
#     return ang + 360 if ang < 0 else ang

def minmax_x(arr_np):
    '''Mengembalikan indeks koordinat yang memiliki nilai x minimal atau maximal'''

    x_coordinates = []
    for i in range(len(arr_np)):
        x_coordinates.append(arr_np[i][0])
    x_min = min(x_coordinates)
    x_max = max(x_coordinates)

    min_index = 0
    found = True
    while min_index < len(arr_np) and found:
        if arr_np[min_index][0] == x_min:
            found = False
        else: min_index += 1
        
    max_index = 0
    found = True
    while (max_index < len(arr_np) and found):
        if arr_np[max_index][0] == x_max:
            found = False
        else: max_index += 1
    
    return (min_index, max_index)


def convexhull(arr):
    arr_used = np.array(arr).astype(float)
    
    # Cari p1 dan pn terluar
    p1, pn = minmax_x(arr_used)
    
    # Bagi menjadi kiri dan kanan garis p1, pn
    left_arr = []; right_arr = []
    for i in range(len(arr_used)):
        if kirikanan_garis(arr_used, p1, pn, i) > 0 and i != p1 and i != pn:
            left_arr.append(i)
        elif kirikanan_garis(arr_used, p1, pn, i) < 0 and i != p1 and i != pn:
            right_arr.append(i)

    a = recursive(arr_used, left_arr, p1, pn, True)
    b = recursive(arr_used, right_arr, pn, p1, False)
    return a+b

def recursive(arr_used, arr, p1, pn, kirikanan):
    # print(p1, pn)
    # print(arr)
    if len(arr) == 0:
        if p1 != pn:
            return [[p1, pn]]
        else:
            return []
    else:
        degrees = []
        for i in range(len(arr)):
            print(arr_used[p1], arr_used[pn], arr_used[arr[i]])
            if p1 != pn and p1 != arr[i] and pn != arr[i]:
                tempdeg = sudut(arr_used[pn], arr_used[p1], arr_used[arr[i]])
            else:
                tempdeg = 0
                # tempdeg = sudut(arr_used[arr[i]], arr_used[p1], arr_used[pn])
            print(kirikanan, tempdeg)
            degrees.append(tempdeg)
        px = arr[degrees.index(max(degrees))]
        # print(px)

        p1px = []
        for i in range(len(arr)):
            if kirikanan_garis(arr_used, p1, px, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                p1px.append(arr[i])
        # print(p1px)

        pxpn = []
        for i in range(len(arr)):
            if kirikanan_garis(arr_used, px, pn, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                pxpn.append(arr[i])
        # print(pxpn)
        # print()

        a = recursive(arr_used, p1px, p1, px, kirikanan)
        b = recursive(arr_used, pxpn, px, pn, kirikanan)

        return a+b


    # print(px)
    # print(p1, pn)
    # print(left_arr)
    # print()
    # print(degrees)
    # print()
    # print(right_arr)

# convexhull(ayy)
