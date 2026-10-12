"""

chera bayad file ha ra bast ...

file ha gahi morede estefade gharar migirand ba estefade az open()

ba estefade az open( ) file ha baz mishavand va ma mitavanim dar mood haye

goonagoon az anan estefade kard. bad az anjam pardazeshhaye morede niyaz 

dar file ha bayad baste shavand zira da gheir in soorat ba tavajoh be moodi

ke da aan hastand moshkelati ijad mikonnad.

baraye mesal dar moode read(r) agar file ra nabandim , momkan ast natavanim

file ra be dorosti jabeja va ya hazf konim va hamchenin dar moode write(w) bedoone bastane 

file momkene taghirate aslan zakhireh nashavand.

zamani ke az open() estefade mikonim hatman dar enteh baayd file ra close()

konim dar soorati ke az with estefade konim be khodi khod bad az anjam 

process haye dakhele block, file be khodi kdod baste mishavad.


"""

f = open("numbers.txt","r")
print(f.read())
f.close()


"""barabar ast ba .........
"""


with open("numbers.txt","r") as f :
    print(f.read())