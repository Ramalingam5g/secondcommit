user_input=int(input("enter the floor where you want to go:"))
def floor_elevator():

    if user_input>=4:
        print("just wait a moment......")
        print("you are now in",user_input,"floor")
        return True
    
     
    else:
        return user_input
user_output=floor_elevator()
print(user_output)

def function_floor():
    user_input2=int(input("enter the floor where u want to go:"))
    if user_input2>user_input:
        print("now you are in",user_input2,"floor")
        return True
    elif user_input2==user_input:
        print("u are in same floor")
        return True
    else:
        return False
c=function_floor()
print(c)
    
