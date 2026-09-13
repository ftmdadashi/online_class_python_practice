password = "admin1234"
count = 0


while count < 3 :
    user_password = input("please enter your password :")


    if user_password != password :
        count += 1 


    else :
        print("your password is right...")
        break
    
    
    
if count == 3 :
    print("you are blocked ...")        
    
