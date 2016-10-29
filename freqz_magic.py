
import numpy as np
import scipy.signal as sg
import matplotlib.pyplot as plt

def freqz_plot(line, cell):
    # line, cellをparse
    N, FS = [float(v) for v in line.split()]
    ba = cell.split("\n")
    b = [float(v) for v in ba[0].split(",")]
    a = [float(v) for v in ba[1].split(",")]

    # 時間特性、周波数特性、位相特性、群遅延特性等を計算
    w, h = sg.freqz(b, a, worN=int(N))
    f = w * FS / (2.0 * np.pi)
    z, p, k = sg.tf2zpk(b, a)
    _, gd = sg.group_delay((b, a), w=w)

    # 上記パラメータをプロット
    fig = plt.figure(1, figsize=(8, 12))
    
    ax = fig.add_subplot(321)
    ax.plot(b, "o-")
    ax.plot(a, "x-")
    ax.grid()
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")
    
    ax = fig.add_subplot(322)
    ax.semilogx(f, 20.0 * np.log10(np.abs(h)))
    ax.grid()
    ax.set_xlabel("frequency [Hz]")
    ax.set_ylabel("power [dB]")
    ax.set_xlim([10.0, FS/2.0])
    ax.set_ylim([-40.0, 10.0])

    ax = fig.add_subplot(323)
    ax.semilogx(f, np.angle(h))
    ax.grid()
    ax.set_xlim([10.0, FS/2.0])
    ax.set_ylim([-np.pi, np.pi])
    ax.set_xlabel("frequency [Hz]")
    ax.set_ylabel("phase [rad]")
    
    ax = fig.add_subplot(324)
    ax.semilogx(f, gd)
    ax.grid()
    ax.set_xlabel("frequency [Hz]")
    ax.set_ylabel("group delay [pt]")
    ax.set_xlim([10.0, FS/2.0])
    ax.set_ylim([-40.0, 40.0])

    ax = fig.add_subplot(325)
    ax.add_patch(plt.Circle((0.0, 0.0), 1.0, fc="white"))
    ax.plot(np.real(z), np.imag(z), "o", mfc="white")
    ax.plot(np.real(p), np.imag(p), "x", mfc="white")
    ax.grid()
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])

    plt.show()

    
def load_ipython_extension(ipython):
    ipython.register_magic_function(freqz_plot, 'cell')