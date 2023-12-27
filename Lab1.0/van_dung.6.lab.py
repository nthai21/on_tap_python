#Tìm số sao cho số đó chia hết cho tổng số
def so_chia_het(n):
    # Chuyển số thành danh sách các chữ số
    chu_so  = [int(so) for so in str(n)]

    # Tính tổng các chữ số
    tong_chu_so = sum(chu_so)

    # Kiểm tra xem số có chia hết cho tổng chữ số không
    return n % tong_chu_so == 0

# Sử dụng hàm để kiểm tra một số
a=int(input("Nhập số bất kỳ :"))
for i in range(1,a):
    if so_chia_het(i):
        print(i,end=" ")