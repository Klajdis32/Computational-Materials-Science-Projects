import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 1. Define the Murnaghan Energy EOS
def murnaghan_energy(V, V0, B0, BP, E0):
    term1 = ((V0 / V)**BP) / (BP - 1) + 1
    return E0 + (B0 * V / BP) * term1 - (V0 * B0) / (BP - 1)

# 2. Load data from LAMMPS result.out
data = np.loadtxt("result.out", skiprows=1)

volumes = data[:, 0]      # Volume in Angstrom^3
energies = data[:, 1]     # Cohesive energy in eV/atom

# 3. Perform the fit
v0_guess = volumes[np.argmin(energies)]
e0_guess = np.min(energies)

p0 = [v0_guess, 0.001, 4.0, e0_guess]

params, _ = curve_fit(murnaghan_energy, volumes, energies, p0=p0)
V0, B0, BP, E0 = params

# 4. Generate smooth curve for the fit
v_fit = np.linspace(min(volumes), max(volumes), 200)
e_fit = murnaghan_energy(v_fit, *params)

# 5. Calculate lattice constant
N = 20
a0 = V0**(1/3) / N

# 6. Create the plot
plt.figure(figsize=(8, 5))
plt.scatter(volumes, energies, label='LAMMPS data')
plt.plot(v_fit, e_fit, label=f'Murnaghan Fit\nV0={V0:.2f} Å³, a0={a0:.4f} Å')

plt.axvline(V0, linestyle='--', alpha=0.5, label='Equilibrium Volume')

plt.title('Cohesive Energy vs Volume', fontsize=12)
plt.xlabel('Volume (Å³)', fontsize=10)
plt.ylabel('Cohesive Energy (eV/atom)', fontsize=10)

plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

plt.savefig('EOS.jpg', dpi=300)
plt.show()

# 7. Print results
print(f"Fit Results:")
print(f"V0 = {V0:.2f} Å³")
print(f"B0 = {B0:.2e} eV/Å³")
print(f"BP = {BP:.2f}")
print(f"E0 = {E0:.4f} eV/atom")
print(f"Equilibrium lattice constant a0 = {a0:.4f} Å")