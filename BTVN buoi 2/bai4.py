def tinh_so_chai_bia(n):
    so_chai_mua = n // 28
    tong_so_chai = so_chai_mua
    so_vo_chai = so_chai_mua

    while so_vo_chai >= 3:
        chai_doi_duoc = so_vo_chai // 3
        tong_so_chai += chai_doi_duoc
        so_vo_chai = (so_vo_chai % 3) + chai_doi_duoc

    print(f"Số chai bia có thể mua được là: {tong_so_chai}")

tinh_so_chai_bia(28)
tinh_so_chai_bia(56)
tinh_so_chai_bia(84)