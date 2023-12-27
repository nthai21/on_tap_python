#Ktra số lẻ
def so_le(n):
    if n%2!=0 :
        return True
    else:
        return False
#Nhập vào số bất kỳ
a=int(input("Nhập vào số bất kỳ "))
if so_le(a) :
    print("Số đó là số lẻ")
else:
    print("Số đó không là số lẻ ")
