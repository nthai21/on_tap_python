#KTRA SỐ NGUYÊN 
def so_nguyen(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5) + 1, 2):#key
            if n % i == 0:
                return False
        return True
#Nhập vào số bất kỳ 
a = int(input("Nhập một số: "))
if so_nguyen(a):
    print("là số nguyên tố.")
else:
    print(" Khôngphải là số nguyên tố.")
