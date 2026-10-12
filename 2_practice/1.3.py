"""

tabee be name safe_int(value) benevisid ke meghdar vorodi ra be int tabdil 

konad. agar tabdil momken nabood meghdar None bargardanad va har do khataye

valueerror va typeerror ra modiriat konad.

"""


def safe_int(value) :
    try :
        if isinstance(value, int)  :
            return value
        else :
            new_value = int(value)
            return new_value
        
    except ValueError :
        return None
    
    except TypeError :
        return None 
    
    
    
check = safe_int("fatemeh")
print(check)

#None