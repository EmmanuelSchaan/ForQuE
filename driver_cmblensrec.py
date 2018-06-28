import cmb
reload(cmb)
from cmb import *

import cmb_lensing_rec
reload(cmb_lensing_rec)
from cmb_lensing_rec import *



# CMB S4: 3' beam fwhm, 1muK' white noise
cmb = StageIVCMB(beam=3., noise=1.)

# Other experiments
#cmb = PlanckSMICACMB()
#cmb = ACTPolCMB()
#cmb = AdvACTCMB()

# show the CMB power spectrum, noise and foregrounds
cmb.plotCl()
cmb.plotTEB()

# Compute the CMB lensing noise
cmbLensRec = CMBLensRec(cmb, save=False)

# Plot it
cmbLensRec.plotNoise()








