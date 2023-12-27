#Tính tổng của căn bậc 2
from math import*
def tong_can(n):
    tong=0
    for i in range(1,n+1):
        tong += sqrt(i)
    print(tong)
    return tong_can
#Nhập giá trị
a=int(input("Nhập giá trị a:"))
print(tong_can(a))