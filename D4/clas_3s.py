from mcpi.minecraft import Minecraft
import random
from time import sleep
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
for j in range(3):
    for i in range(5):
        r = random.randint(1,4)
        if r == 1:
            mc.setBlocks(x,y,z,x+4,y,z,1)
            x = x+4
        elif r ==2:
            mc.setBlocks(x,y,z,x-4,y,z,1)
            x = x-4
        elif r ==3:
            mc.setBlocks(x,y,z,x,y,z+4,1)
            z = z+4
        else:
            mc.setBlocks(x,y,z,x,y,z-4,1)
            z = z-4
        
