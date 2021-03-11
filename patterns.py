a=int(input("enter your row :"))
for i in range(a):

    k=ord("a")+i
    
    for j in range(i+1):
        print(chr(k), end=" ")
        k=k+1
    print(a)
    