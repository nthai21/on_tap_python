#Tính tổng các số nguyên tố
def la_so_nguyen_to(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):#key
        if x % i == 0:
            return False
    return True
def tong_so_nguyen_to(n):
    tong=0
    for i in range(2,n+1):
        if la_so_nguyen_to(i):
            tong+=i
    print(tong)
    return tong_so_nguyen_to
#Nhập giá trị
a=int(input("Nhập giá trị của a:"))
print(tong_so_nguyen_to(a))

