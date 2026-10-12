"""

ba estefade az os.path.exisi() barresi konid ke aya yek file vojod darad

ya kheir, agar vojod nadasht aan ra besazid va yek payam monaseb chap konid,

agar ham vojod dasht mohtaviat aan ra chap konid.

"""

import os

if os.path.exists("numbers.txt") :
    with open("numbers.txt" , "r") as f:
        print(f.read())
        
else :
    with open("numbers.txt","r") as f :
        print("file number.txt is made.")