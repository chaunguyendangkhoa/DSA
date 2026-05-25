A = [7, 3, 9, 12, 5, 8, 1]
def dem_so_sanh(A, x):
    count = 0
    for i in range(len(A)):
        count = count + 1
        if A[i] == x:
            return count
    return count


ss1 = dem_so_sanh(A, 7)

ss2 = dem_so_sanh(A, 1)
ss3 = dem_so_sanh(A, 100)
print("x = 7")
print("Số phép so sánh:", ss1)
print()
print("x = 1")
print("Số phép so sánh:", ss2)
print()
print("x = 100")
print("Số phép so sánh:", ss3)
print()
print("Nhận xét:")
print("Phần tử ở đầu mảng cần ít phép so sánh hơn.")
print("Phần tử ở cuối hoặc không có trong mảng cần nhiều phép so sánh hơn.")