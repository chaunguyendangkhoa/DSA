danh_ba = []


while True:

    print("\n===== MENU =====")

    print("1. Thêm liên hệ")

    print("2. Tìm số điện thoại theo tên")

    print("3. Tìm tên theo số điện thoại")

    print("4. Đếm số điện thoại bắt đầu bằng đầu số")

    print("0. Thoát")


    chon = input("Nhập lựa chọn: ")


    # Thêm liên hệ
    if chon == "1":

        ten = input("Nhập tên: ")

        sdt = input("Nhập số điện thoại: ")

        lien_he = {
            "ten": ten,
            "sdt": sdt
        }

        danh_ba.append(lien_he)

        print("Đã thêm liên hệ")

    # Tìm số điện thoại theo tên
    elif chon == "2":

        ten_can_tim = input("Nhập tên cần tìm: ")

        tim_thay = False

        for lh in danh_ba:

            if lh["ten"] == ten_can_tim:

                print("Số điện thoại:", lh["sdt"])

                tim_thay = True

        if tim_thay == False:

            print("Không tìm thấy")

    # Tìm tên theo số điện thoại
    elif chon == "3":

        sdt_can_tim = input("Nhập số điện thoại: ")

        tim_thay = False

        for lh in danh_ba:

            if lh["sdt"] == sdt_can_tim:

                print("Tên:", lh["ten"])

                tim_thay = True
        if tim_thay == False:

            print("Không tìm thấy")

    # Đếm đầu số
    elif chon == "4":

        dau_so = input("Nhập đầu số: ")

        dem = 0

        for lh in danh_ba:

            if lh["sdt"].startswith(dau_so):

                dem = dem + 1

        print("Có", dem, "số điện thoại bắt đầu bằng", dau_so)

    # Thoát
    elif chon == "0":

        print("Kết thúc chương trình")

        break

    else:

        print("Lựa chọn không hợp lệ")