"""

barnamee benevisid ke mohtavaye yek file matni ra dar file digari copy konad va 

dar in farayand hameye horof ra be horofe bozorg tabdil konad .

"""


with open("info.txt","r") as f :
    copy = f.read().upper()
    
with open("new_info.txt","w") as f :
    f.write(copy)
    
with open("new_info.txt","r") as f :
    print(f.read())
    
    
    
"""

MY NAME IS FATEMEH
I AM 35 YEARS OLD.
NOW, I AM PRACTICING PYTHON.

"""