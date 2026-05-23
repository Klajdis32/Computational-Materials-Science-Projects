import numpy as np
import matplotlib.pyplot as plt

# files and corresponding timesteps
files = {
    "0.1 fs": "log1.lammps",
    "0.5 fs": "log2.lammps",
    "1 fs": "log3.lammps",
    "5 fs": "log4.lammps"
}

plt.figure(figsize=(8,5))

for label, file in files.items():

    data = np.genfromtxt(file, skip_header=1)

    step = data[:,0]
    toteng = data[:,4]

    plt.plot(step, toteng, linewidth=1.5, label=label)

plt.xlabel("Simulation Time (Timestep)")
plt.ylabel("Total Energy (eV)")
plt.title("Total Energy vs Simulation Time for Different Timesteps")

plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig("energy_comparison_timesteps.jpg", dpi=300)

plt.show()