#Tìm các số chia hết cho 3 nhưng không là số chẵn 
def tim_so_chia_het_cho_3_khong_chan(a,b):
    # Tìm và in các số theo yêu cầu
    for i in range(a+1, b + 1, 2):  # Bắt đầu từ start + 1 để đảm bảo số lẻ
        if i % 3 == 0:
            print(i,end=",")

# Gọi hàm và in kết quả
tim_so_chia_het_cho_3_khong_chan(1000, 2000)