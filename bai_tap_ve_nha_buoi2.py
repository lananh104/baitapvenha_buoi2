# bài 1: Giải phương trình  bậc 2 a^2*x+b*x+c=0
import math
print("Giải phương trình a^2*x+b*x+c=0")
a=float(input("Với hệ số a="))
b=float(input("Với hệ số b="))
c=float(input("Với hệ số c="))
denta=b**2-4*a*c
if denta>0:
    x1=(-b+math.sqrt(denta))/2*a
    x2=(-b-math.sqrt(denta))/2*a
    print("Phương trình có 2 nghiệm phân biệt: x1= %s,x2= %s" %(round(x1,4),round(x2,4)))
elif denta==0:
    x=-b/2*a
    print("Phương trình có nghiệm kép: x1=x2=%s" %(round(x,4)))
else:
    x1=complex(-b/2*a,-math.sqrt(abs(denta))/2*a)
    x2=complex(-b/2*a,math.sqrt(abs(denta))/2*a)
    print("Phương trình có 2 nghiêm phức là: x1={}, x2={}".format(x1,x2))
#bài 2:Tính các tổng S1,S2,S3
import math
#tính tổng S1=1 + x + x^2 + x^3 + ... + x^n
print("Tính tổng S1=1 + x + x^2 + x^3 + ... + x^n ")
x=float(input("Nhập x:"))
n=int(input("Nhập bậc cao nhất của x trong dãy: "))
S1=0
for i in range(0,n+1,1):
    S=x**i
    S1+=S
print("Tổng của dãy số là : S1 = {} ".format(S1))
#tính tổng của dãy S2=1-x+x^2-x^3...+(-1)^n*x^n
print("Tính tổng S2=1-x+x^2-x^3...+(-1)^n*x^n")
x=float(input("Nhập x: "))
n=int(input("Nhập bậc cao nhất của x trong dãy số: "))
S2=0
for i in range(0,n+1,1):
    S=(-1)**i*x**i
    S2+=S
print("Tổng cần tìm là: S2 = %s " %(S2))
#tính tổng S3 = 1 + \dfrac{x}{1!} + \dfrac{x}{2!} + ... + \dfrac{x^n}{n!}
x=float(input("Nhập x: "))
n=int(input("Nhập bậc cao nhất của x trong dãy: "))
S3=0
for i in range(0,n+1,1):
    S=x**i/math.factorial(i)
    S3+=S
print("Tổng cần tìm là: S3 = %s " %(round(S3,2)))
'''
Bài 3. Lập chương trình thực hiện các công việc sau:
Nhập 1 số nguyên dương n bất kì (n<1000). Yêu cầu kiểm tra dữ liệu đầu vào, nếu sai yêu cầu nhập lại.
Tính tổng các chữ số của số đó.
Hiển thị kết qủa ra màn hình
'''
n=int(input("Nhập số nguyên dương n nhỏ hơn 1000: "))
while True:
    if n>=1000:
        print("Số vừa nhập không thỏa mãn yêu cầu, mời nhập lại.")
        break
    else:
        a=n//100
        b=(n-100*a)//10
        c=(n-100*a-10*b)
        print("Tổng các chữ số của số n vừa nhập là: {}".format(a+b+c))
        break
'''bài 4
 Nhập 3 số a, b, c bất kì
 Hãy kiểm tra xem ba số đó có phải là độ dài của các cạnh của một tam giác hay không?
 Nếu đúng là tam giác thì xác định là tam giác vuông hay không?
'''
a,b,c=float(input("Nhập số a= ")),float(input("Nhập số b= ")),float(input("Nhập số c= "))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    print("Ba số a,b,c vừa nhập là độ dài của một tam giác ")
    if a**2==b**2+c**2 or c**2==b**2+a**2 or b**2==a**2+c**2:
        print("Và đây là một tam giác vuông")
    else:
        print("Và đây không phải là tam giác vuông")
else:
    print("Ba số a,b,c vừa nhập không phải là cạnh của một tam giác")















