"""
if n  is odd, print Weird
If n is even and in the inclusive range of 2 to5 , print Not Weird
If  n is even and in the inclusive range of6  to 20, print Weird
If  n is even and greater than 20, print Not Weird
"""
def check_odd_even():
    n=int(input("enter you numbr:"))
    if n%2==0:
        n>0
        n<=5
        print("not weired")
        if n>6:
            n<20
            print("weird")
        else:
            n>=20
            print("not weird")
else:
    print("weird")
check_odd_even()