"""

farz konid data = [1,2,3] darim. az karbar yek andis begirid va ozve motenazere

aan ra chap konid. khataye indexerror va valueerror ra ba 2 payame jodagane

modoriat konid.

"""


data = [1, 2, 3]

try :
    
    index_number = int(input("please enter your index :")) 
    if index_number in range(len(data)):
        number = data[index_number]
        print("your number in list is :", number)
        
        
    else :
        raise IndexError()
        
        
except IndexError :
    print("your index is not in available range")
    
except ValueError :
    print("you should enter a number")
        
        