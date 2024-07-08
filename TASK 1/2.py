def arithemetic():                                                     
        a = int(input("Enter 1st number : "))                        
        b = int(input("Enter 2nd number : "))                       
        print("Addition : ",a+b)                                      
        print("Subraction : ",a-b)                                      
        print("Multiplication : ",a*b)                                  
        print("Division : ",a/b)                                       

def strings():                                                          
    s = input("Enter a String : ")                                      
    ss = input("Enter a string : ")                                     
    print("Concatenation : ",s+ss)
    print("Index of [0] : ",s[0])                                     
    print("Index of [5] : ",s[5])                                     
    print("Slicing [0:5] : ",s[0:5])                                    

print("1 . Arithmetic Operations\n2 . String Operations\n3 . Exit\n")
ch= int(input("Enter the choice :"))                                    
if ch == 1:                                                             
    arithemetic()                                                       
elif ch == 2:
    strings()                                                           
elif ch == 3:
    print("Closing")
else:
    print("Invalid Choice !")
