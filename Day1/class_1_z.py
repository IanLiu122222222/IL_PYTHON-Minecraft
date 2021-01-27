from mcpi.minecraft import Minecraft as mc
mcs = mc.create()
print(mcs.player.getTilePos)
x=50 
y=60
z=70
mcs.player.setTilePos(x,y,z)