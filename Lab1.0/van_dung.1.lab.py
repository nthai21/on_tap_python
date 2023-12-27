#Liệt kê ra các số lẻ 
def so_le(n):
    if n%2!=0 :
        return True
    else:
        return False
#Nhập vào số bất kỳ
a=int(input("Nhập vào số bất kỳ "))
for i in range (1,a-1):
    if so_le(i):
        print(i, end=" ")