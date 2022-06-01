class aa:
    x = 0

    def __init__(self, age):
        self.x = age
    def __str__ (self):
        return 'Age:' + str(self.x)
a = aa(input("Enter age:"))

print(a)
