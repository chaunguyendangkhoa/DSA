a = [3, 7, 2, 9, 5]

max_value = a[0]

vi_tri = 0

for i in range(len(a)):

    if a[i] > max_value:

        max_value = a[i]

        vi_tri = i

print("Giá trị lớn nhất:", max_value)
print("Vị trí:", vi_tri)