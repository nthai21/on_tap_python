#Nhập A và tim giá trị nhỏ nhất của n để 1+2**2+...n**2>A
def tim_n(A):
    n = 1
    tong = 0
    
    while tong <= A:
        tong += n**2
        n += 1
    
    return n - 1

# Nhập số nguyên dương A từ người dùng
A = int(input("Nhập vào số nguyên dương A: "))
print(tim_n(A))