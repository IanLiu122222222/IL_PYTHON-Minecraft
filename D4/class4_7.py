from mcpi.minecraft import Minecraft as mcs
from time import sleep
import random
mcs = mcs.create()
myID = mcs.getPlayerEntityId("Ianliu5487")
mineral = [14,15,16,56,73,129]
while True:
    sleep(0.5)
    r = random.choice(mineral)
    x,y,z = mcs.entity.getTilePos(myID)
    mcs.setBlocks(x+1,y,z+1,x-1,y+3,z-1,r)
