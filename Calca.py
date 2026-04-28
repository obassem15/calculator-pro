import Module as md
 
print("Hi in our calc")

history =[]

last_result = None

while True :
    
    print("\n===== CALCULATOR =====")
    print("1- Add (+)")
    print("2- Subtract (-)")
    print("3- Multiply (*)")
    print("4- Divide (/)")
    print("5- Power")
    print("6- History")
    print("7- Clear history")
    print("0- Exit")
   
    ch = input("\nEnter your choice ")

    if ch=="0":
        print("Good bye")
        break
    
    elif ch =="6":
       if len(history) == 0 :
         print("No history") 

       else :
          print("\nHistory")
          for h in history :
             print(h)

    elif ch == "7":
       history.clear()
       print("History deleted")       

    elif ch in ["1" ,"2" ,"3" , "4" , "5"] :
        try:
        
           num1 = float(input("Enter your number: "))
           num2 = float(input("Enter your number: "))   

           if ch == "1" :
             result = md.add(num1 , num2)
             print(f"Result is : {result} ") 
             history.append(f"{num1} + {num2} = {result}")
          
           elif ch == "2" :
             result = md.subtract(num1 , num2)
             print(f"Result is : {result} ") 
             history.append(f"{num1} - {num2} = {result}")
            
           elif ch == "3" :
             result = md.mp(num1 , num2)
             print(f"Result is : {result} ")
             history.append(f"{num1} * {num2} = {result}")

           elif ch == "4" : 

              if num2 == 0:
                 print("Can not divide by zero")     
              else:          
                result = md.dv(num1 , num2)
                print(f"Result is : {result} ")
                history.append(f"{num1} / {num2} = {result}")


           elif ch == "5":
              result = md.power(num1 , num2)
              print(f"Result is : {result} ")
              history.append(f"{num1} ** {num2} = {result}")


        except ValueError:
           print("Enter correct number")

    else :
             print("Please enter correct operation") 
             