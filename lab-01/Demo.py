#biến
x=10 #biến x lưu trữ giá trị số nguyên 10
name = "Alice" #biến name lưu trữ chuỗi "Alice"
is_valid = true #biến is_valid lưu trữ giá trị boolean true
if = 5 # lỗi! "if"là từ khoá, không thể sử dụng làm tên biến

#cộng +
a = 5
b = 3
result  = a + b #Kết quả: 8

#trừ - 
a = 8 
b = 4
result = a - b #kết quả: 4

#nhân *
a = 6
b = 7
result = a * b #kết quả: 42

#chia /
a = 20
b = 5
result = a / b #kết quả: 42.0(kết quả luon là một số thập phân nếu có phần dư)

#chia lấy phần nguyên //
a = 20
b = 3
result = a // b #kết quả: 6

#chia lấy dư %
a = 20
b = 7
result = a % b #kết quả: 6(phần dư của 20 chia cho 7)

#luỹ thừa **
a = 2
b = 3
result = a ** b #kết quả: 8 (2^3=8)

#phép toán AND
x = 5
y = 3
result = (x>2) and (y<4) #kết quả : true

#phép toán OR
x = 5
y = 3
result = (x>2) or (y>4) #kết quả : true

#phép toán NOT
x = 5
result = (x==)  #kết quả : false

#phép so sánh bằng ==
x = 5
result = (x==5)  #kết quả : true

#phép so sánh không bằng !=
x = 5
result = (x!=3)  #kết quả : true

#phép so sánh lơn hơn >, nhỏ hơn <
x = 5
result = (x>3) #kết quả : true
result = (x<3) #kết quả: false

#hàm input
name = input("nhập tên của bạn")
print("xin chào,", name)

#hàm print
age = 25
print("tuổi của bạn là :"age)

#ví dụ
print("python", "là", "ngôn", "ngữ , "lập", "trình", sep= "-")
    #kết quả: python-là-ngôn-ngữ-lập-trình
print("xin chào", end=" ")
print("các bạn!") # kết quả: xin chào các bạn!

#câu lệnh điền kiện
x=10
if x >5:
  print("x lớn hơn 5")
elif x==5:
  print("x bằng 5")
else:
  print("x nhỏ ơn 5")
  
#vòng lặp 
#for
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)

#while
count = 0
while count < 5 :
   print(count)
   count += 1
   
#câu lệnh nhảy
#break
#tìm số chia hết cho 5 đầu tiên trong khoảng từ 1 đe3ens 1--
for i in range(1, 101):
   if 1 %5 ==0:
       print("số chia hết cho 5 đầu tiên là:", 1)
       break
#continue
#in các số chẵn từ 1 đến 10 và bỏ qua các số lẻ
for i in range(1, 11):
if i %2 !=0
   continue
   print(i)
#pass
#kiểm tra điều kiện, nếu đúng thực hiện, nếu sai thì không làm gì 
x=5
if x>10:
print("x lớn hơn 10")
else:
pass

#chuỗi
#khai báo chuỗi
#sử dụng dấu trong ngoặc đơn
string_single_quotes= 'đây là 1 chuỗi sử dụng dấu ngoặc dơn'
#sử dụng dấu trong ngoặc kép
string_double_quotes= "đây là 1 chuỗi sử dụng dấu ngoặc kép"
#sử dụng dấu trong ngoặc ba
string_triple_quotes= '''đây là 1 chuỗi sử dụng dấu ngoặc ba 
có thể 
trải nhiều dòng.'''

#truy cập kí tự trong chuỗi
my_string="hello, world!"
print(my_string[0]) #kết quả: 'H'
print(my_string[7]) #kết quả: 'W'

#các phép xử lý chuỗi
my_string="hello, world!"
print(my_string[7:]) #lấy từ ký tự thứ 7 đến hết:  kết quả: 'world!'
print(my_string[:5]) #lấy từ đầ đến ký tự thứ 4:  kết quả: 'hello
print(my_string[3:8]) #lấy từ ký tự thứ 3 đến ký tự thứ 7 kết quả: 'lo, W'

#ghép chuỗi
sring1="hello"
string="world"
concatenated_string=string1 + " "+ stromg2 #kết quả:"hello world"

#độ dài chuỗi
my_string = "hello, world!"
lenght = len(my_string) #kết quả 13

#1 số hàm dùng để xử lý chuỗi
my_string = "       hello,world!      "
print(my_string.srip()) #loại bỏ khoảng trắng: kết quả: "hello,world!

my_string = "hello, world!"
print(my_string.split(",")
#phân tách chuỗi: kết quả : ['hello','world']

my_string = "hello, world!"
print(my_string.replace("hello","hi"))
#thay thế chuỗi: kết quả : "hi,world!"

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


























































