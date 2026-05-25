def tim_ten(ds, ten):

    ten = ten.lower()

    for i in range(len(ds)):

        if ds[i].lower() == ten:

            return i

    return -1


ds = ["An", "Binh", "Chau"]

ten = input("Nhập tên cần tìm: ")

print("Vị trí:", tim_ten(ds, ten))