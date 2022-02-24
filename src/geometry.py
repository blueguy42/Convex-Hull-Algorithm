import numpy as np

def kirikanan_garis(arr, p1, pn, px):
    '''Memeriksa apakah sebuah titik berada di sebelah kiri atau
    kanan garis menggunakan penentuan determinan. Bila sebelah
    kiri maka hasil positif, kanan negatif, di garis 0.'''

    x1 = arr[p1][0]; y1 = arr[p1][1]; x2 = arr[pn][0]; y2 = arr[pn][1]; x3 = arr[px][0]; y3 = arr[px][1]

    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3


def sudut(a, b, c):
    '''Mengembalikan sudut dari segitiga ABC dengan B sudut yang
    terapit menggunakan definisi dot product.'''

    # cos theta = ba.bc / |ba|*|bc|
    ba = a - b; bc = c - b
    cosine = np.dot(ba, bc)/(np.linalg.norm(ba)*np.linalg.norm(bc))

    # Clipping cosine due to floating rounding inaccuracy
    cosine = np.clip(cosine, -1, 1)
    
    return np.degrees(np.arccos(cosine))


def minmax_x(arr_np):
    """Mengembalikan tuple indeks titik dengan nilai x minimal
    dan maksimal."""

    # Mencari nilai x minimal atau maksimal
    x_coordinates = []
    for i in range(len(arr_np)):
        x_coordinates.append(arr_np[i][0])
    x_min = min(x_coordinates)
    x_max = max(x_coordinates)

    # Menentukan indeks dengan x minimal
    min_index = 0
    found = True
    while min_index < len(arr_np) and found:
        if arr_np[min_index][0] == x_min:
            found = False
        else: min_index += 1
        
    # Menentukan indeks dengan x maksimal
    max_index = 0
    found = True
    while (max_index < len(arr_np) and found):
        if arr_np[max_index][0] == x_max:
            found = False
        else: max_index += 1
    
    return (min_index, max_index)

