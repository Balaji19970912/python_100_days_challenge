try:
    num1 = int(input("Enter a number: "))
    arra = [1,3,5,7,9]
    print(arra[num1])
except Exception as e:
    print("Some error occurred")
finally:
    print("Yoyo")