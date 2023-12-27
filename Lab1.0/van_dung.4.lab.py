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
for i in range (1,a-1):
    if so_chinh_phuong(i):
        print(i,end=" ")