# Odd Even program
"""def evenodd(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
num=int(input("enter the number : "))
evenodd(num)
input()"""

# If Else program
""" num=-7
# if num<4:
#     if num<0:
#         print("number is less than zero")
#     else:
#         print("number is greater than zero")
# elif num>4:
#     print("number is greater than four")
# else:
#     print("number is equal to four")"""

# Sum of 10 numbers

"""sum=0
num=int(input("enter the number : "))
for i in range(num+1):
    sum=sum+i
print(f"sum of {num} is ",sum)"""

# Fibonacci series

"""num=int(input("enter the number : "))
fib=[0,1]
for i in range(2,num+1):
    fibo=fib[-1]+fib[-2]
    fib.append(fibo)
print("fibonacci numbers are : ",fib)"""

# Vowel or uppercase or lowercase

"""str=input("enter the alphabet : ")
if str in ("a","e","i","o","u"):
    print("alphabet is vowel")
elif str.islower():
    print("alphabet is lower")
elif str.isupper():
    print("alphabet is upper")
else:
    print("alphabet is invalid")"""

# Display all numbers till user entered zero

"""number=[]
while True:
    num=int(input("enter the number : "))
    if num==0:
        print("Exiting program....")
        break
    else:
        number.append(num)
print("number entered")
for i in number:
    print(i)"""

# Prime numbers 3 to 30

for i in range(3,31):
    if i>1:
        for j in range(2, int(i**0.5) + 1):
            if i%j==0:
                break
        else:
            print(i)