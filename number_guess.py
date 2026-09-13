hidden_number = 70
guess = float(input("please enter your guess :"))


while guess != 70 :
    if guess > 70 :
        print("adade shoma bozorgtar az adade makhfi ast.")
        guess = float(input("please enter your guess again :"))

    else :
        print("adade shoma kochektar az adade makhfi ast.")
        guess = float(input("please enter your guess again :"))


print("congratulation...")





"""

please enter your guess :60
adade shoma kochektar az adade makhfi ast.
please enter your guess again :32
adade shoma kochektar az adade makhfi ast.
please enter your guess again :70
congratulation...

"""