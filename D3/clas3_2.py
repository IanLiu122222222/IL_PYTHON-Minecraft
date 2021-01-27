from mcpi.minecraft import Minecraft as mc
import random
import time
mcs=mc.create()
x,y,z = mcs.player.getPos()
while True:
    time.sleep(1)
    x= x+random.uniform(-20,20)
    y= y+random.uniform(-20,20)
    z= z+random.uniform(-20,20)
    mcs.spawnEntity(x,y,z,64)