from mcpi.minecraft import Minecraft as mc
import time 
mcs=mc.create()
while True:
    num = 0
    try:
        num = int(input('What do you want'))
    except:
        print("That is not number")
    x,y,z=mcs.player.getPos()
    mcs.setBlock(x,y,z,num)
    e=input("EXIT")
    if e == 'Y' or e == 'y' or e == 'yes' or e == 'YES' :
        break
    else :
        continue