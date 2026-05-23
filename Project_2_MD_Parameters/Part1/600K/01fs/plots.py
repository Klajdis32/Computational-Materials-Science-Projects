import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Load only the data block
data = np.genfromtxt('log.lammps', skip_header=63, max_rows=501)

# Columns
step = data[:,0]
poteng = data[:,2]
kineng = data[:,3]
toteng = data[:,4]

# Formatter για να εμφανίζονται οι πραγματικές τιμές
formatter = ScalarFormatter(useOffset=False)
formatter.set_scientific(False)

# Plot potential energy vs timestep
fig, ax = plt.subplots()
ax.plot(step, poteng)
ax.set_xlabel('Timestep')
ax.set_ylabel('Potential Energy (eV)')
ax.set_title('Potential Energy vs Timestep')
ax.yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.savefig('potential_energy.jpg', dpi=300)
plt.close()

# Plot kinetic energy vs timestep
fig, ax = plt.subplots()
ax.plot(step, kineng)
ax.set_xlabel('Timestep')
ax.set_ylabel('Kinetic Energy (eV)')
ax.set_title('Kinetic Energy vs Timestep')
ax.yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.savefig('kinetic_energy.jpg', dpi=300)
plt.close()

# Plot total energy vs timestep
fig, ax = plt.subplots()
ax.plot(step, toteng, linewidth=1.5)
ax.set_xlabel('Timestep')
ax.set_ylabel('Total Energy (eV)')
ax.set_title('Total Energy vs Timestep')
ax.yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.savefig('total_energy.jpg', dpi=300)
plt.close()

# Calculate average total energy
avg_toteng = np.mean(toteng)

print(f"Average Total Energy = {avg_toteng:.6f} eV")