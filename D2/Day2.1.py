from mcpi.minecraft import Minecraft as mc
import time 
mcs=mc.create()
x,y,z=mcs.player.getTilePos()
s=190
mcs.setBlocks(x+s,y,z+s,x-s,y+s,z-s,0)