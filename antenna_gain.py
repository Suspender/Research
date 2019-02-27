import numpy as np
import matplotlib.pyplot as plt
import module

lmd = 0.328 #meter
eirp = 10 * np.log10(3) + 30 #dbm
pt = eirp - 8

gr = 6.1 #dBi directional patch
degree = [20, 30, 40, 50, 60]
distance=[]
for i in range(5, 31, 1):
    distance.append(i)

for index, theta in enumerate(degree):
    list=[]
    for d in distance:
        ga = 52525 / theta / 90
        pr_mw = np.log10(module.friis(d, lmd, pt, ga, gr))
        list.append(pr_mw)
    if index==0 :
        c="red"
        lab="20°"
    elif index==1 :
        c="blue"
        lab="30°"
    elif index==2 :
        c="green"
        lab="40°"
    elif index==3 :
        c="cyan"
        lab="50°"
    elif index==4 :
        c="m"
        lab="60°"
    plt.plot(distance, list, color=c, label=lab)

plt.xlabel("Distance [m]")
plt.ylabel("Received power [mW]")
plt.legend()
plt.show()
