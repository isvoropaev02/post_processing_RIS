import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def diagramma_estimation(phases, amplitudes=None):
    f = 25*1e9 # Hz
    c = 3*1e8 # m/s
    #dy = 0.0058*2 # m
    num_periods = 3 # количество периодов

    theta = np.linspace(-90, 90, 200)
    k = 2*np.pi * f / c

    dy = 2*np.pi/(k*np.sin(np.pi/6)) / 6
    #dy = 0.005 # m

    if amplitudes == None:
        dn_target = np.zeros(theta.shape[0], dtype=complex)

        for n in range(len(phases)*num_periods):
            ind = n % phases.shape[0]
            dn_target += np.exp(1j*phases[ind] * np.pi/180) * np.exp(1j*k*dy*n*np.sin(theta* np.pi/180))
        dn_target /= (phases.shape[0]*num_periods)

    else:
        dn_target = np.zeros(theta.shape[0], dtype=complex)

        for n in range(len(phases)*num_periods):
            ind = n % phases.shape[0]
            dn_target += amplitudes[ind] * np.exp(1j*phases[ind] * np.pi/180) * np.exp(1j*k*dy*n*np.sin(theta* np.pi/180))
        dn_target /= (phases.shape[0]*num_periods)

    return theta, dn_target


theta1, pat_ideal = diagramma_estimation(np.array([180, 120, 60, 0, -60, -120]))
#theta1, pat_ideal = diagramma_estimation(np.array([-120, -60, 0, 60, 120, 180]))
theta2, pat_kvant = diagramma_estimation(np.array([110, 110, 110, 0, 0, 0]))
#theta2, pat_kvant = diagramma_estimation(np.array([180, 180, 0, 0, 0, 180]))

fig1 = plt.figure(figsize=(8,5))

ax_1 = fig1.add_subplot(111)
ax_1.plot(theta1, np.abs(pat_ideal),'r', label='В идеальном случае')
ax_1.plot(theta2, np.abs(pat_kvant),'royalblue', label=r'С 2 значениями фазы, $\Delta\phi \neq 180^\circ$')
#ax_1.scatter([-27.4], [1], color='k', label='max (-27.4 deg)')
ax_1.set_ylabel(r"Абсолютное значение $F(\psi)$")
ax_1.set_xlabel(r"$\psi$, град.")
ax_1.legend(loc='upper left')
ax_1.set_xticks([-90, -60, -30, 0, 30, 60, 90])
ax_1.grid()


#fig1.suptitle('Множитель решетки')
plt.show()

#exp_theta, exp_diagr = diagramma_estimation(np.array([180, 180, 180, 0, 0, 180, 180, 0, 0, 0, 180, 180, 0, 0, 0]))
exp_theta, exp_diagr = diagramma_estimation(np.array([0, 0, 0, 180, 180, 0, 0, 180, 180, 180, 0, 0, 180, 180, 180]))

fig2 = plt.figure(figsize=(8,5))

ax_1 = fig2.add_subplot(111)
ax_1.plot(exp_theta, 20*np.log10(np.abs(exp_diagr)),'r', label='Оценка')
#ax_1.scatter([-27.4], [1], color='k', label='max (-27.4 deg)')
ax_1.set_ylabel("Абсолютное значение, дН")
ax_1.set_xlabel(r"$\theta$, град.")
ax_1.set_xlim([10, 70])
ax_1.set_ylim(bottom=-30)
ax_1.legend()
ax_1.grid()


fig2.suptitle('Множитель решетки')
plt.show()