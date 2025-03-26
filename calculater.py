def add(a,b):
    answer = a+b
    print(str(a) + "+" + str(b) + " = " + str(answer) +"\n")

def sub(a,b):
    answer = a - b
    print(str(a) + "-" + str(b) + " = " + str(answer) + "\n")
     
def multi(a,b):
    answer = a * b
    print( str(a) + " * " + str(b) + " = " + str(answer) + "\n")    

def div(a,b):
    answer = a / b
    print( str(a) + " / " + str(b) + " = " + str(answer) + "\n")  
while True:
     
     print("A. addition ")
     print("B. subtraction")
     print("C. multipliction") 
     print("D. division")   
     print("E. exit") 

     choice = input("input your choice: ")


     if choice == "a" or choice =="A":
         print("addition")
         a = int(input("input first number: "))
         b = int(input ("input second number: "))
         add(a,b)
     elif choice == "b" or choice == "B":
         print("subtrection") 
         a = int(input("input first number: "))
         b = int(input("input second number: "))
         sub(a,b)
 
     elif choice == "c" or choice == "C":
          print("multiplication") 
          a = int(input("input first number: "))
          b = int(input("input second number: "))
          multi(a,b)
     elif choice == "d" or choice == "D":
           print("division") 
           a = int(input("input first number: "))
           b = int(input("input second number: "))
           div(a,b)

     elif choice == "e" or choice == "E":
          print("PROGRAM ENDED") 
          quit()



