#Dãy số đối xứng
def so_doi_xung(n):
    # Chuyển số thành chuỗi để dễ xử lý
    chuyen_doi_so  = str(n)
    
    # So sánh chuỗi với chuỗi đảo ngược
    return chuyen_doi_so == chuyen_doi_so[::-1]
#Nhập vào dãy số bất kỳ
a= int(input("Nhập một số: "))
if so_doi_xung(a):
    print(" là số đối xứng.")
else:
    print("không phải là số đối xứng.")