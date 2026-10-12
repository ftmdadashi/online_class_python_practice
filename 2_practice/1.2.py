"""

barnamee benevisid ke do adad ra az karbar begirad va adade aval ra 

be adade dovom taghsim konad. khataye zero divisionerror ra modiriat konad va dar

sorate taghsim bar sefr, payame monasebi chap konad.

"""


try :
    number1 = int(input("please enter the first number :"))
    number2 = int(input("please enter the second number :"))
    number_division = number1 / number2
    print("The result of division is :", number_division)
    
except ValueError :
    print("you shoud enter a number")
    
except ZeroDivisionError :
    print("you can't enter zero(0) for second number ")