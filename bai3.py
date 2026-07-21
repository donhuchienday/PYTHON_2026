def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def xu_ly_so(n):
    chuoi_so = str(abs(n))
    so_chu_so = len(chuoi_so)
    
    tong_chu_so = 0
    for chu_so in chuoi_so:
        tong_chu_so += int(chu_so)
    
    if kiem_tra_nguyen_to(n):
        ket_luan = "là số nguyên tố"
    else:
        ket_luan = "không phải là số nguyên tố"
        
    print(f"Số chữ số: {so_chu_so}, Tổng chữ số: {tong_chu_so}, {n} {ket_luan}.")

xu_ly_so(54)
xu_ly_so(53)
xu_ly_so(123)
xu_ly_so(2)