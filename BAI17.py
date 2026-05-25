def sentinel_search(a, x):

    n = len(a)

    a.append(x)

    i = 0

    while a[i] != x:

        i = i + 1

    a.pop()

    if i < n:

        return i

    return -1

a = [3, 5, 7, 9, 11]
x = int(input("Nhập x: "))
print("Kết quả:", sentinel_search(a, x))