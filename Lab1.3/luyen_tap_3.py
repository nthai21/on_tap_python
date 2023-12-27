#Đếm số nguyên đã nhập
def dem_so(a):       
    tong=0
    while a!=0:
        tong+=1
        a//=10
    print(tong)
    return dem_so
#Tính tổng số nguyên vừa nhập
def tong_so_nguyen(n):
    tong_so=0
    while n!=0:
       r = n%10
       tong_so += r
       n//=10
    print(tong_so)
    return tong_so_nguyen
#Tính trung bình công số nguyên 
def tb_so_vua_nhap(m):
   tb=tong_so_nguyen//dem_so
   print(tb)
   return tb_so_vua_nhap
#Nhập số bất kỳ 
a=int(input("Nhập số nguyên bất kỳ :"))
print(tb_so_vua_nhap(a))
