class Elevator:
    def floor_elevator(self):
        
        person_input=int(input(" you are in ground floor \n which floor you want go :"))

        if person_input<=4:
            print("now you reach",person_input,"floor")
    def first_floor(self):
        
        person_input2= int(input("where you want to go:"))

        

        if person_input2 < person_input:
            print("YOU ARE IN ",person_input2, "FLOOR ")
        elif person_input2 > person_input:
            print("you are in",person_input2,"floor")
        else:

            print("PRESS ANY KEY")
    def second_floor(self):

        person_input3= int(input("where you want to go UP OR DOWN:"))

        if person_input3 <=2:
            print("you are in SECOND floor")
        elif person_input3=="DOWN":
            print("you are in  floor")
        else:
            print("is it wrong")

            
            

        
       

obj=Elevator()
obj.floor_elevator()
obj.first_floor()
obj.second_floor()

            

        
        