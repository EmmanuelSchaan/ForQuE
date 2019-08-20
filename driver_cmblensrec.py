import imp

import cmb
imp.reload(cmb)
from cmb import *

import cmb_lensing_rec
imp.reload(cmb_lensing_rec)
from cmb_lensing_rec import *

##################################################################################
# CMB experiment specifications

# multipoles used for lensing reconstruction
lMinT = 30.
lMaxT = 3.e3
lMaxP = 5.e3
cmb = StageIVCMB(beam=1., noise=1., lMin=lMinT, lMaxT=lMaxT, lMaxP=lMaxP, atm=False, name=None)


##################################################################################
# Noise power spectrum for QE from temperature and polarization

# lensing noise for QE
cmbLensRec = CMBLensRec(cmb, nProc=3)

# Normalizations and lensing noise autos for Q_XY
#cmbLensRec.saveNormQ(pol=True)
cmbLensRec.loadNormQ()
cmbLensRec.plotNoiseQAuto(pol=True)

# Lensing noise crosses for Q_XY and Q_WZ
#cmbLensRec.saveNoiseCov()
cmbLensRec.loadNoiseCov()
cmbLensRec.plotNoiseQ(pol=True)


##################################################################################
# Noise power spectrum for shear and dilation

# Normalizations for shear, dilation
#cmbLensRec.saveNormSD()
cmbLensRec.loadNormSD()

# Lensing noises for shear, dilation and QE (test)
#cmbLensRec.saveNoiseQSD()
cmbLensRec.loadNoiseQSD()
cmbLensRec.plotNoiseQSD()


##################################################################################
# Noise power spectrum for the multipole estimators

# precompute the multipoles of the lensing response f_TT
#cmbLensRec.save_f_TT_multipoles()
cmbLensRec.load_f_TT_multipoles()
cmbLensRec.plot_f_TT_multipoles()

# precompute the lensing noise for the monopole and quadrupole estimators
#cmbLensRec.save_N_k_TT_multipoles()
cmbLensRec.load_N_k_TT_multipoles()
cmbLensRec.plotNoiseMultipoles()
















