#Tính tích các số từ 1-n
def tich_so(n):
    tich=1
    for i in range(1,n+1):
        tich*=i
    print(tich)
    return tich_so
#Nhập giá trị
a=int(input("Nhập giá trị a:"))
print(tich_so(a))

