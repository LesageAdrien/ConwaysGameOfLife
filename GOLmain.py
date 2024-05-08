import GOLprocessor
import GOLrenderer
import numpy as np



size = 300
golp = GOLprocessor.GameOfLife((size,size))
#golp.setarr(GOLprocessor.makeAshoot(size))
golp.setarr(GOLprocessor.centeredsoup(size))
golp.symetrize()
golr = GOLrenderer.GameOfLifeRenderer()
while golr.isRunning():
    golr.disp(golp.getarr())
    golp.tick()
    golr.wait(0.05)
del(golr)

