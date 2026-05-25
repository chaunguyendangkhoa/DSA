def linear_search(a, x):

    for i in range(len(a)):

        if a[i] == x:

            return i

    return -1


# Nhập mảng
a = list(map(int, input("Nhập mảng: ").split()))

# Nhập giá trị cần tìm
x = int(input("Nhập x: "))

# Gọi hàm
ket_qua = linear_search(a, x)

# In kết quả
print("Kết quả:", ket_qua)