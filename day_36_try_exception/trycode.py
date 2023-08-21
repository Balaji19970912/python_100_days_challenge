import os
os.system('cls')

num1 = int(input("Which number's multiplication table you want : "))
# print(num1)
try:
    for i in range(1,11):
        print(f"{num1} X {i} = {num1*i}")
except Exception as e:
    print(e)