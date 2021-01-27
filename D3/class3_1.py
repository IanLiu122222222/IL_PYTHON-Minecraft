from mcpi.minecraft import Minecraft as mc
mcs=mc.create()

while True:
    hits = mcs.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z = hit.pos.x ,hit.pos.y  ,hit.pos.z
        block = mcs.getBlock(x,y,z)
        mcs.setBlock(x,y,z,20)