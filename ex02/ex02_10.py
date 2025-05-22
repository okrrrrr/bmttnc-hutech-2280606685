def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
    # su dung ham dao_nguoc_chuoi va in ra
    input_string = input("Nhập vào một chuỗi: ")
    print("Chuỗi đảo ngược là:", dao_nguoc_chuoi(input_string))