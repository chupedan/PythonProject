def dem_so_lan_xuat_hien(doan_tho):
    # Tách từng từ trong đoạn thơ
    tu = doan_tho.split()

    # Tạo một đối tượng từ điển để lưu trữ số lần xuất hiện của từng từ
    dem_tu = {}

    # Đếm số lần xuất hiện của từng từ
    for tu_ky in tu:
        # Chuyển đổi từ về dạng chữ thường để không phân biệt chữ hoa, chữ thường
        tu_ky = tu_ky.lower()

        # Thêm từ vào từ điển hoặc tăng giá trị đếm nếu từ đã tồn tại
        dem_tu[tu_ky] = dem_tu.get(tu_ky, 0) + 1

    return dem_tu

# Đoạn thơ của bạn
doan_tho = "Vườn xuân hoa nở muôn màu Tỏa hương thơm ngát dạt dào ngất ngây Ong vờn bướm lượn vui say Thi nhân ghé lại tháng ngày lãng quên."

# Đếm số lần xuất hiện của từng từ trong đoạn thơ
ket_qua = dem_so_lan_xuat_hien(doan_tho)

# Hiển thị kết quả
for tu, so_lan in ket_qua.items():
    print(f"{tu}: {so_lan} lần")
############################
word_count = {}
for w in words:
    if not w in word_count:
        word_count[w] = 1
    else:
        
for k, v in word_count.item()
