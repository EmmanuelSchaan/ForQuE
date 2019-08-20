#  ForQuE

Computes the noise power spectrum for CMB lensing quadratic estimators for any CMB experiment, using Monte Carlo integration:

* Standard quadratic estimators from Hu & Okamoto 2002 from temperature and polarization. The minimum-variance estimator takes into account the noise covariance of the various quadratic estimators.
* Shear and magnification estimators of https://arxiv.org/abs/1804.06403
* Multipole lensing estimators of https://arxiv.org/abs/1804.06403

Requires the Monte Carlo library vegas (https://pypi.org/project/vegas):
```
pip install vegas
```
Just clone and run:
```
python driver_cmblensrec.py
```
Hope you find this code useful! Please cite https://arxiv.org/abs/1607.01761 if you use this code in a publication. Do not hesitate to contact me with any questions: eschaan@lbl.gov

