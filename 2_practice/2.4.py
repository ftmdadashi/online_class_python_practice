"""

barnamee benevisid ke yek file matni ra bekhanad va tedade khotot, tedade

charechter va tedade kalamate aan ra chap konad.

"""


with open("info.txt","r") as f :
    numbers_of_lines = len(f.read().splitlines())
    print("numbers_of_lines :",numbers_of_lines)     #numbers_of_lines : 3


with open("info.txt","r") as f :
   numbers_of_word = len(f.read().split())
   print("numbers_of_words :",numbers_of_word )    # numbers_of_words : 14


with open("info.txt","r") as f :
   numbers_of_char = len(f.read())
   print("numbers_of_char :",numbers_of_char)     # numbers_of_char : 66

    
    
with open("info.txt","r") as f :
    print(f.read())
    
    
"""

numbers_of_lines : 3
numbers_of_words : 14
numbers_of_char : 66
My name is fatemeh
I am 35 years old.
now, I am practicing python.


"""