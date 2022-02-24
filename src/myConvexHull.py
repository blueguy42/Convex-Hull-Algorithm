from geometry import *

def myConvexHull(arr):
    """Mengembalikan hasil pasang titik garis pembentuk bidang
    convex hull. Fungsi juga langkah pertama algoritma divide
    and conquer convex hull dengan membagi titik-titik menjadi
    kiri/kanan garis minimal/maksimal x."""

    arr_used = np.array(arr).astype(float)
    
    # Cari p1 dan pn terluar
    p1, pn = minMax(arr_used)
    
    # Bagi menjadi kiri dan kanan garis p1, pn
    left_arr = []; right_arr = []
    for i in range(len(arr_used)):
        if kiriKananGaris(arr_used, p1, pn, i) > 0 and i != p1 and i != pn:
            left_arr.append(i)
        elif kiriKananGaris(arr_used, p1, pn, i) < 0 and i != p1 and i != pn:
            right_arr.append(i)

    # Masuk fungsi rekursi convex hull kiri garis
    kiri = myConvexHullRecursive(arr_used, left_arr, p1, pn)
    # Masuk fungsi rekursi convex hull kanan garis
    kanan = myConvexHullRecursive(arr_used, right_arr, pn, p1)
    return kiri + kanan


def myConvexHullRecursive(arr_used, arr, p1, pn):
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
            if kiriKananGaris(arr_used, p1, px, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                p1px.append(arr[i])
        p1titik = myConvexHullRecursive(arr_used, p1px, p1, px)

        # Rekursi titik-titik pada kiri garis titik-pn
        pxpn = []
        for i in range(len(arr)):
            if kiriKananGaris(arr_used, px, pn, arr[i]) > 0 and arr[i] != p1 and arr[i] != pn:
                pxpn.append(arr[i])
        titikpn = myConvexHullRecursive(arr_used, pxpn, px, pn)

        return p1titik + titikpn