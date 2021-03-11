num=int(input("enter you are number"))
if num>1:
    for y in range(2,num):
        if (num%y)==0:
            print("not prime")
            break
        else:
            print(" prime")
            break
else:
    print("not prime")