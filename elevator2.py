user_input=int(input("enter where you want to go: "))
start = 0
end =4
def function_floor():
    if (user_input==start):
        print("you are in",user_input,"floor")
    elif user_input<end:
        print("you are in", user_input,"floor")       
    else:
        print("please enter valid number")

        return True
print(function_floor())
        
def floor_elevator():

    user_input2=int(input("enter where you want to go: "))
    if user_input2==user_input:
        print("you are in same floor")
    elif user_input2>user_input:
        print("you are in ",user_input2,"floor")
    elif user_input2<user_input:
        print("you are in",user_input2,"floor")
    else:
        print("print ANY KEYS")
        return False

    
function_floor()
floor_elevator()
