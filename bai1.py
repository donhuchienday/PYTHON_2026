def tinh_so_ngay(thang, nam):
    la_nam_nhuan = (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)
    
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if la_nam_nhuan:
            return 29
        else:
            return 28
    else:
        return -1

thang_nhap = int(input("Nhập tháng: "))
nam_nhap = int(input("Nhập năm: "))

ket_qua = tinh_so_ngay(thang_nhap, nam_nhap)

if ket_qua != -1:
    print(f"Số ngày của tháng {thang_nhap} năm {nam_nhap} là: {ket_qua}")
else:
    print("Tháng bạn nhập không hợp lệ! Vui lòng nhập từ 1 đến 12.")