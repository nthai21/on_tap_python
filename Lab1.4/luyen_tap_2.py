#Chuỗi số đảo ngược
n=int(input("Mời nhập số :"))
lat=0
while n!=0:
    lat=lat*10 + n%10
    n//=10
print(lat)
