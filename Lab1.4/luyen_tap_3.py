def chuyen_chuoi_sang_chu_hoa(chuoi):
    chuoi_chu_hoa = ""
    for ky_tu in chuoi:
        # Kiểm tra nếu là ký tự thường
        if 'a' <= ky_tu <= 'z':
            # Chuyển đổi thành ký tự hoa sử dụng bảng mã ASCII
            ky_tu_chu_hoa = chr(ord(ky_tu) - ord('a') + ord('A'))
        else:
            # Nếu là ký tự khác, giữ nguyên
            ky_tu_chu_hoa = ky_tu
        
        chuoi_chu_hoa += ky_tu_chu_hoa
    
    return chuoi_chu_hoa

# Sử dụng hàm
chuoi_nhap = input("Nhập chuỗi: ")
chuoi_chu_hoa = chuyen_chuoi_sang_chu_hoa(chuoi_nhap)
print("Chuỗi chữ hoa: ", chuoi_chu_hoa)
