#Tính tổng các số chẵn từ 1-n
def tong_so_chan(n):
    tong=0
    for i in range(1,n+1):
        if i %2==0:
            tong+=i
    print(tong)
    return tong_so_chan
#Nhập giá trị
a=int(input("Nhập a:"))
ket_qua=tong_so_chan(a)
print("Tổng số chẵn là :",ket_qua)