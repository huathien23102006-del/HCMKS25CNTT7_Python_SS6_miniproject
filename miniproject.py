# câu 1
unit_price = float(input("Nhập vào đơn giá: "))
quantity = int(input("Nhập số lượng mua: "))

total_price = unit_price * quantity

if(total_price >= 1000000):
    sell = total_price * 0.9
else:
    sell = total_price

print("Số tiền cần thanh toán: ",sell)

# câu 2

password = "123456"
check = 0
for i in range(3):
    in_pass = input("Nhập vào mật khẩu: ")

    if(in_pass == password):
        print("Đăng nhập thành công!")
        check = 1
        break
    else:
        print("Mật khẩu sai, vui lòng nhập lại!")

if(check == 0):
    print("Tài khoản đã bị khóa")

# câu 3
total_quantity = int(input("Nhập vào số lượng sản phẩm của từng thùng: "))
total_container = 0
while True:
    containers = int(input("Nhập số thùng hàng: "))
    if(containers > 0):
       total_container += 1
    elif(containers == 0):
        break
    else:
        print("Số lượng không hợp lệ, bỏ qua thùng này")
        continue

total = total_container * total_quantity

print("Tổng số thùng hàng hợp lệ đã đếm: ", total_container)
print("Tổng số lượng sản phẩm thu được: ", total)
