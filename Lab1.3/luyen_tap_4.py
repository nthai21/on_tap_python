def tong_so_nguyen(n):
    tong_so=0
    while n!=0:
       r = n%10
       tong_so += r
       n//10
    print(tong_so)
    return tong_so_nguyen
#Nhập số '
a=int(input())
print(tong_so_nguyen(a))