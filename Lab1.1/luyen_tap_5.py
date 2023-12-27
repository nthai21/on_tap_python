#Tích các số chia hết cho 3
def tich_3(n):
    tich=1
    for i in range(1,n+1):
      if i%3==0:
        tich*=i
    print(tich)
    return tich_3
#Nhập giá trị
a=int(input("Nhập giá trị a:"))
print(tich_3(a))