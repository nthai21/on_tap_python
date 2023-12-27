#Tìm số nguyên dương m lớn nhất sao cho: 1 + 2 + … + m < A
def tim_so_n(A):
    n = 1
    tich = 1

    while tich <= A:
        n += 1
        tich *= n

    return n

def main():
    # Nhập giá trị A từ người dùng
    A = int(input("Nhập giá trị A: "))
    print(tim_so_n(A))

if __name__ == "__main__":
    main()
