import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter

# Load only the data block
data = np.genfromtxt('log.lammps', skip_header=63, max_rows=10000)

# Columns
step = data[:,0]
poteng = data[:,2]

# Formatter για να εμφανίζονται οι πραγματικές τιμές
formatter = ScalarFormatter(useOffset=False)
formatter.set_scientific(False)

# Plot potential energy vs timestep
fig, ax = plt.subplots()
ax.plot(step, poteng, linewidth=1.5)

ax.set_xlabel('Timestep')
ax.set_ylabel('Potential Energy (eV)')
ax.set_title('Potential Energy vs Timestep')

ax.yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.savefig('potential_energy.jpg', dpi=300)
plt.show()