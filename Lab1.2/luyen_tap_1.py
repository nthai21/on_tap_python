#Nhập vào giá trị A sao cho 1+2+3...+n>A
def tong_so_nho_hon_A(A):
    n = 1
    tong = 0
    
    while tong <= A:
       tong += n
       n += 1
    return n - 1

# Nhập số nguyên dương A từ người dùng
A = int(input("Nhập vào số nguyên dương A: "))
print(tong_so_nho_hon_A(A))



