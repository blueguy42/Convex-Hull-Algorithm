import numpy as np

def kirikanan_garis(arr, p1, pn, px):
    '''Memeriksa apakah sebuah titik berada di sebelah kiri atau
    kanan garis menggunakan penentuan determinan. Bila sebelah
    kiri maka hasil positif, kanan negatif, di garis 0.'''

    x1 = arr[p1][0]; y1 = arr[p1][1]; x2 = arr[pn][0]; y2 = arr[pn][1]; x3 = arr[px][0]; y3 = arr[px][1]

    return x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3


def sudut(a, b, c):
    '''Mengembalikan sudut dari segitiga ABC dengan B sudut yang
    terapit.'''

    # cos theta = ba.bc / |ba|*|bc|
    ba = a - b; bc = c - b
    cosine = np.dot(ba, bc)/(np.linalg.norm(ba)*np.linalg.norm(bc))

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


def convexhull(arr):
    """Mengembalikan hasil pasang titik garis pembentuk bidang
    convex hull. Fungsi juga langkah pertama algoritma divide
    and conquer convex hull dengan membagi titik-titik menjadi
    kiri/kanan garis minimal/maksimal x."""

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

    # Masuk fungsi rekursi convex hull kiri garis
    kiri = convexhull_recursive(arr_used, left_arr, p1, pn)
    # Masuk fungsi rekursi convex hull kanan garis
    kanan = convexhull_recursive(arr_used, right_arr, pn, p1)
    return kiri + kanan

def convexhull_recursive(arr_used, arr, p1, pn):
    """Fungsi rekursif penentu pasangan indeks titik garis
    pembentuk bidang convex hull pada sisi garis dengan arr
    array titik pada sisi garis."""

    # Basis: tidak ada titik di sisi garis
    if len(arr) == 0:
        # Memastikan pasangan titik tidak sama
        if p1 != pn:
            return [[p1, pn]]
        else:
            return []
    else:   # Rekursi: terdapat titik di sisi garis
        # Menentukan besar sudut p1-titik-pn untuk setiap titik
        degrees = []
        for i in range(len(arr)):
            # Memastikan ketiga titik sudut tidak sama agar
            # tidak error pembagian dibagi 0
            if p1 != pn and p1 != arr[i] and pn != arr[i]:
                tempdeg = sudut(arr_used[pn], arr_used[p1], arr_used[arr[i]])
            else:
                tempdeg = 0
            degrees.append(tempdeg)
        # Menentukan indeks titik dengan derajat terbesar
        px = arr[degrees.index(max(degrees))]

        # Rekursi titik-titik pada kiri garis p1-titik
        p1px = []
        for i in range(len(arr)):
            if kirikanan_garis(arr_used, p1, px, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                p1px.append(arr[i])
        p1titik = convexhull_recursive(arr_used, p1px, p1, px)

        # Rekursi titik-titik pada kiri garis titik-pn
        pxpn = []
        for i in range(len(arr)):
            if kirikanan_garis(arr_used, px, pn, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                pxpn.append(arr[i])
        titikpn = convexhull_recursive(arr_used, pxpn, px, pn)

        return p1titik + titikpn