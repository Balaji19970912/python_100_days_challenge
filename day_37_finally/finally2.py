def func1():
    try:
        num1 = int(input("Enter a number : "))
        arra = [1,3,5,7,9]
        # print(arra[num1])
        return 1
    except:
        print("Some error occurred")
        return 0
    finally:
        print("yoyo")

x = func1()
print(x)