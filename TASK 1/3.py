def list():
    li = [1,2,3,4,5,6]                            
    print("List : ",li)
    li.append(35)                                       
    li.insert(1,10)                                     
    li.remove(17)                                       
    a = li[1]                                           
    print("At index 1 : ",a)
    print("Updated list : ",li)

def dict():
    d = {"Name" : "Priya","Age" : 17,"Year" : 1}     
    print("Dictionary : ",d)
    d["Dept"] = "AI&ML"                               
    del d["Year"]                                      
    d["Age"] = 18                                       
    print("Updated Dictionary : ",d)

def tuple():
    t = (10,45,78,96,131,64)                              
    u = t + (35,)                                      
    t[:1]+t[5:]                                         
    print("Removed Tuple : ",t)
    l = 500
    t[:1]+(l,)+t[6:]                                    
    print("Updated Tuple : ",t)

print("LIST")
list()                                                  
print("DICTIONARY")
dict()                                                  
print("TUPLE")
tuple()                                                 
