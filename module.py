import numpy as np

# d:distance[m], lmd:wavelength[m], pt:transmission power[dBm]
# ga:transmitter antenna gain[dBi], gr:receiver antenna gain[dBi]
# pr:received power[mW]
def friis(d, lmd, pt, ga, gr) :
    gamma = 10 * np.log10((4 * np.pi * d / lmd) ** 2)
    pr = pt + ga + gr - gamma
    pr_mw = 10 ** (pr / 10)
    return pr_mw
