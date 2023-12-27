#KTRA SỐ CHÍNH PHƯƠNG 
from math import* 
def so_chinh_phuong(n):
    if n==0:
        return False
    else :
        a=isqrt(n)
        if a*a==n:
            return True 
        else :
            return False 
#...................Nhập vào giá trị só bất kỳ để kiểm tra số nguyên ........................
a=int(input("Nhập a :"))
if so_chinh_phuong(a):
    print("số đó là số chính phương ")
else:
    print("Số đó ko là số chính phương ")

