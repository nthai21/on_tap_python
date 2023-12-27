#Tính tổng số lẻ 
def tong_so_le(n):
    tong=0
    for i in range(1,n+1):
        if i%2!=0:
            tong+=i
    print(tong)
    return tong_so_le
#Nhập giá trị
a=int(input("Nhập giá trị a:"))
print(tong_so_le(a))