#Hàm tìm ước chung lớn nhất
def uc_chung(a, b):
    while b:
        a, b = b, a % b
    return a
#Nhập vào 2 số bất kỳ 
m = int(input("Nhập số thứ nhất: "))
n = int(input("Nhập số thứ hai: "))
uoc_chung = uc_chung(m,n)
print("Ước chung lớn nhất của" ,m,"và",n,"là:", uoc_chung)