a = [4, 2, 9, 1, 7]

min_value = a[0]
max_value = a[0]

vi_tri_min = 0
vi_tri_max = 0

for i in range(len(a)):

    if a[i] < min_value:

        min_value = a[i]

        vi_tri_min = i

    if a[i] > max_value:

        max_value = a[i]

        vi_tri_max = i


print("Giá trị nhỏ nhất:", min_value)
print("Vị trí min:", vi_tri_min)
print("Giá trị lớn nhất:", max_value)
print("Vị trí max:", vi_tri_max)