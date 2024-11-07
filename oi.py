class io():
    def __init__(self):
        self.str1= " "
    def get(self):
        self.str1= input("Enter string: ")
    def pr(self):
        print(self.str1.upper())
str1= io()
str1.get()
str1.pr()