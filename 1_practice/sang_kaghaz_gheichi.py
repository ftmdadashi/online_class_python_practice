"""

BAZI SANG, KAGHAZ, GHEICHI...

"""

print("rock")
print("paper")
print("scissors")
print("-------------------")

user_1 = input("user 1: please enter your choice between(rock, paper, scissors) :")
user_2 = input("user 2 : please enter your choice between(rock, paper, scissors) :")




if user_1 == "rock" :
    if user_2 == "rock":
        print("bazi mosavi ast.")
        
    elif user_2 == "paper":
        print("bazikon 2 barande ast.")
        
        
    else :
        print("bazikon 1 barande ast.")
        

elif user_1 == "paper" :
    if user_2 == "rock":
        print("bazikon 1 barande ast.")
        
    elif user_2 == "paper":
        print("bazi mosavi ast.")
        
        
    else :
        print("bazikon 2 barande ast.")
        
        

else :
    if user_2 == "rock":
        print("bazikon 2 barande ast.")
        
    elif user_2 == "paper":
        print("bazikon 1 barande ast.")
        
        
    else :
        print("bazi mosavi ast.")
        
    
#dar in tabe mitoni az random estefade koni

        
        
"""

in barname ba farze tanha yekbar tekrare bazi mibashad.

khoroji:
    
rock
paper
scissors
-------------------
user 1: please enter your choice between(rock, paper, scissors) :rock
user 2 : please enter your choice between(rock, paper, scissors) :scissors
bazikon 1 barande ast.




rock
paper
scissors
-------------------
user 1: please enter your choice between(rock, paper, scissors) :paper
user 2 : please enter your choice between(rock, paper, scissors) :scissors
bazikon 2 barande ast.



rock
paper
scissors
-------------------
user 1: please enter your choice between(rock, paper, scissors) :scissors
user 2 : please enter your choice between(rock, paper, scissors) :scissors
bazi mosavi ast.

"""


    