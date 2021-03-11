class CodesCracker:   #create a class
    def checkEvenOdd(self, n):#function dclearaion
        if n%2==0:#condition
            return 1#return

print("Enter a Number: ", end="") #get user value
num = int(input())#user input

obj = CodesCracker()#creating an object
chk = obj.checkEvenOdd(num)
if chk==1:
    print("Even Number")
else:
    print("Odd Number")