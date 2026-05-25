sinh_vien = [
    {
        "ma_sv": "SV01",
        "ho_ten": "Nguyen Van A",
        "dtb": 8.5
    },

    {
        "ma_sv": "SV02",
        "ho_ten": "Tran Thi B",
        "dtb": 7.8
    },

    {
        "ma_sv": "SV03",
        "ho_ten": "Le Van C",
        "dtb": 9.0
    }
]


def tim_sinh_vien(ds, ma_sv):

    for sv in ds:

        if sv["ma_sv"] == ma_sv:

            return sv
    return None

ma_can_tim = input("Nhập mã sinh viên: ")

ket_qua = tim_sinh_vien(sinh_vien, ma_can_tim)

if ket_qua != None:

    print("Thông tin sinh viên:")
    print("Mã SV:", ket_qua["ma_sv"])
    print("Họ tên:", ket_qua["ho_ten"])
    print("Điểm trung bình:", ket_qua["dtb"])
else:
    print("Không tìm thấy sinh viên")