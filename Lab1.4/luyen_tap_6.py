# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập chuỗi với các từ được phân cách bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các từ sử dụng hàm split()
danh_sach_tu = chuoi_nhap.split(', ')

# In ra danh sách các từ
print("Danh sách các từ:")
for tu in danh_sach_tu:
    print(tu)
