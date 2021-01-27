from mcpi.minecraft import Minecraft as mc
mcs=mc.create()
x,y,z=mcs.player.getPos()
for i in range(60):
    mcs.setBlock(x+i,y-2,z,57)