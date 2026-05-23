import numpy as np
import matplotlib.pyplot as plt

# Load data
data = np.genfromtxt('log.lammps', skip_header=57, skip_footer=30)

# Plot temperature vs timestep
plt.plot(data[:,0], data[:,1])
plt.xlabel('Timestep')
plt.ylabel('Temperature (?)')
plt.savefig('T.jpg')
plt.close()

# Plot pressure vs timestep
plt.plot(data[:,0], data[:,5])
plt.xlabel('Timestep')
plt.ylabel('Pressure (?)')
plt.savefig('P.jpg')
plt.close()

# Calculate averages
print(f"Average temperature: {np.average(data[101:,1]):.3f} ?")
print(f"Average pressure: {np.average(data[101:,5]):.3f} ?")

