from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
number = 15
for i in range(8):
    for j in range(number):
        mc.spawn.Entity(x,y,z,60)
        number = number *2
        mc.postToChat("Spawn It."+str(number)+"Fish")
        
    
    