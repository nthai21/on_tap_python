#Tính tổng của phân số đan dấu
def tong_so_dan_dau(n):
    tong=0
    for i in range(1,n+1):
        if i%2==0:
            tong-=1/i
        else :
            tong+=1/i
    print(tong)
    return tong_so_dan_dau
#Nhập giá trị 
a=int(input("Nhập giá trị của a:"))
print(tong_so_dan_dau(a))