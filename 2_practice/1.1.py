"""

barnamee benevisid ke yek adad az karbar begirad va 2 barabar aan ra chap

konad. ba estefade az try/except vorodi gheir adadi ra modiriat konad va be

jaye cerash kardane barname, payame monasebi namayah dahad.

"""


try :
    number = int(input("please enter a number :"))
    new_number = number * 2
    print("new number is :",new_number)
    
except ValueError :
    print("you shoud enter number")
    