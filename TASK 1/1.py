name = "rich dad poor dad"                         
price = 800.00                                       
qty = 5                                                
available = True                                    
author = 'wokong'                                    
ite = 2                                             

def writ():                                             
    if available:                                   
        print(f"{author} wrote this book")
    else:
        print(f"{author} does not wrote this book")

for j in range(ite):                                    
    if qty == 0:                                         
        print("Available")
    else:
        print("Not available")

    for i in range(qty-1):                               
        print("qty = ",i)
        writ()                                           
    print("Executed")
