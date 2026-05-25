def ton_tai(a, x):

    for i in range(len(a)):

        if a[i] == x:

            return True
    return False

a = [1, 3, 5, 7, 9]
x = int(input("Nhập x: "))
print(ton_tai(a, x))