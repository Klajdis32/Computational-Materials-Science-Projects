import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Load data from log.lammps
data = np.genfromtxt('log.lammps', skip_header=63, max_rows=51)

# Columns
step = data[:, 0]
temp = data[:, 1]

# Keep only data after timestep 3000
mask = step >= 3000
step_after = step[mask]
temp_after = temp[mask]

# Statistics from simulation
mean_temp = np.mean(temp_after)
sigma_T = np.std(temp_after)

print(f"Average Temperature = {mean_temp:.3f} K")
print(f"Temperature Standard Deviation (σ_T) = {sigma_T:.3f} K")

# Formatter for axis
formatter = ScalarFormatter(useOffset=False)
formatter.set_scientific(False)

# Plot
fig, ax = plt.subplots()

ax.plot(step, temp, linewidth=1.5)
ax.axvline(x=3000, linestyle="--", linewidth=1, label="Equilibration cutoff")

ax.set_xlabel("Simulation Time (Timestep)")
ax.set_ylabel("Temperature (K)")
ax.set_title("Temperature vs Simulation Time")

ax.yaxis.set_major_formatter(formatter)
ax.legend()

plt.tight_layout()
plt.savefig("temperature_vs_time.jpg", dpi=300)
plt.close()