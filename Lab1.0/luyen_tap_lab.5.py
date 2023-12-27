#Ktra số chẵn
def so_chan(n):
    if n%2==0:
        return True
    else:
        return False
#Nhập vào số bất kỳ
a=int(input("Nhập vào số bất kỳ "))
if so_chan(a):
    print("số đó là số chẵn ")
else:
    print("Số đó không là số chẵn")