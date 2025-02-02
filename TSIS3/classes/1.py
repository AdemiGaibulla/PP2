class strOperations():
    def __init__(self):
        self.str = ""

    def getString(self):
        self.str = str(input("Enter a string: "))

    def printString(self):
        print(self.str.upper())

a = strOperations()
a.getString()
a.printString()
