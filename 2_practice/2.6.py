"""

file shamele tadadi adad (har adad dar yek khat) bekhanid va majmoe anan 

ra chap konid, khoototi ke adade motabar nistnd (masalan khali ya shamele matn)

ra ba try/except nadide begirid.

"""

with open("numbers.txt","w") as f :
    f.write("1\n")
    f.write("2\n")
    f.write("3\n")
    f.write("4\n")
    f.write("5\n")
    f.write("6\n")
    f.write("fatemeh\n")
    f.write("dadashi")
    
    
    
sum_numbers = 0

with open("numbers.txt","r") as f :
    for line in f.readlines() :
        try :
            sum_numbers += int(line)
        except ValueError :
            continue
        
    print("sum of numbers is :", sum_numbers)
    

    
            