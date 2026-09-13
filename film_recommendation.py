"""

dictionary az filmha dar ekhtiyar darim shamel etelaati az ghabile: zhanr, sene 

mojaz va emtiyaze sabt shode.

barnamee benevisid ke etelaati az ghabile sen, zhanre morede alaghe va hadeaghal

emyiyaze ghabele ghabool ra baresi kadreh va tanha filmhaee ra pishnahad dahad

ke sene karbar bozogtar ya mosavi hadeaghal sene mojaz bashad, zhanr film ba zhanre

morede alaghe karbar tatabogh dashte bashad va emtiyaz film bozorgtar ya mosavi

hadeaghal emtiyaze made nazare karbar bashad.

"""


film_dict = [{"name":"megan", "genre":"horror", "age":16 , "star":4},
             {"name":"the italian job", "genre":"action", "age":12 , "star":3.5},
             {"name":"inception", "genre":"sci-fi", "age":14 , "star":5},
             {"name":"game of thrones", "genre":"fantasy", "age":18 , "star":4.5},
             {"name":"papillon", "genre":"crime", "age":16 , "star":4}]




age = int(input("please enter your age :"))
genre = input("please enter your favorite genre betwwen (horror,action,sci-fi,fantasy,crime) :")
star = float(input("please enter your acceptable star betwwen 1 to 5 :"))
film_recommend = False

for i in film_dict :
    if age >= i["age"] :
        if genre == i["genre"]:
            if star <= i["star"]:
                film_recommend = True
                print("my recommendtaion film is :",i["name"])
            
                            

if film_recommend == False :
    print(" I have' not any recommendtation...")                
            
    
                
                
                
                
"""

please enter your age :18
please enter your favorite genre betwwen (horror,action,sci-fi,fantasy,crime) :crime
please enter your acceptable star betwwen 1 to 5 :3
my recommendtaion film is : papillon


"""                
                
                
                
                
                
                
                
                
                
