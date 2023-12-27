def so_doi_xung(n):
    # Chuyển số thành chuỗi để dễ xử lý
    chuyen_doi_so  = str(n)
    
    # So sánh chuỗi với chuỗi đảo ngược
    return chuyen_doi_so == chuyen_doi_so[::-1]
#............................Nhập vào dãy số ...........................
a=int(input("Nhập vào số :"))
for i in range(1,a-1):
    if so_doi_xung(i):
        print(i,end=" ")