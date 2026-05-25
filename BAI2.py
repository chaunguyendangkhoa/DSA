A = [7, 3, 9, 12, 5, 8, 1]
x = 5
print("Bắt đầu tìm kiếm:\n")
for i in range(len(A)):

    print("Bước", i + 1)

    print("i =", i)

    print("A[i] =", A[i])

    if A[i] == x:

        print("So sánh:", A[i], "==", x)
        print("Kết quả: Đúng")
        print("Đã tìm thấy x tại vị trí", i)
        print("Hàm trả về:", i)
        break
    else:

        print("So sánh:", A[i], "==", x)
        print("Kết quả: Sai")
        print("Tiếp tục tìm...\n")