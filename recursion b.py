def product(a, b):
    if (a == 0 or b == 0):
        return 0
    elif (a < b):
        return product(b, a)
    elif b != 0:
        return (a + product(a, b - 1))


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("Product =", product(a, b))