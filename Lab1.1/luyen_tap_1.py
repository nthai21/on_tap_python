#Tính tổng của A=1+2+3....n
def tinh_tong(n):
    tong=0
    for i in range(1,n+1): 
        tong+=i
    print(tong)
    return tinh_tong 
#Nhập giá trị
a=int(input("Nhập a:"))
print(tinh_tong(a))