#Tìm bội chung cuả 2 số 
#BCNN(a*b)=(a*b)/UC(a,b)
def uc_chung(a, b):
    while b:
        a, b = b, a % b
    return a
def boi_chung(a,b):
    return a*b//uc_chung(a,b)
#Nhập vào 2 số bất kỳ 
a=int(input("Nhập vào số thứ nhất"))
b=int(input("Nhập vào số thứ hai "))
b_c=boi_chung(a,b)
print("Bội chung của 2 số ",a,"và",b,"là:",b_c)