def tinh_tong_uoc_so(n):
    uoc_so = []
    tong_uoc_so = 0

    for i in range(1, n+1):
        if n % i == 0:
            uoc_so.append(i)
            tong_uoc_so += i

    return uoc_so, len(uoc_so), tong_uoc_so

# Nhập số nguyên dương n
n = int(input("Nhập một số nguyên dương n: "))

# Tính tổng các ước số và in kết quả
uoc_so, so_luong_uoc_so, tong_uoc_so = tinh_tong_uoc_so(n)

print("Ước số của ",n," là" ,uoc_so)
print("Số lượng ước số của", n, 'là',":",so_luong_uoc_so )
print("Tổng các ước số của",n," là:" ,tong_uoc_so)
