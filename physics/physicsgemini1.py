"""
This program is a physics problem solver for Physics 2 topics.
Created by Zachary A. Hampton
"""

import numpy as np  # We'll use NumPy for handling multi-charge calculations

# Constants
CONSTANTS = {
    "k": 8.99 * 10**9,  # Coulomb's constant (N*m^2/C^2)
    "epsilon0": 8.85 * 10**-12,  # Permittivity of free space (C^2/N*m^2)
    "pi": 3.14159,
    "mu0": 4 * 3.14159 * 10**-7,  # Permeability of free space (T*m/A)
}

def get_float_input(prompt):
    """Gets valid numerical input from the user. Includes units prompt."""
    while True:
        try:
            value = float(input(prompt))
            units = input("Enter the units: ")
            return value, units
        except ValueError:
            print("Invalid input. Please enter a number with units.")


def electric_fields_and_forces():
    """
    Calculates electric fields and forces due to multiple point charges.

    Formulas:
    * Electric field at point P from charge qi: E_i = k * qi / r_i^2 * r_hat_i
    * Net electric field at point P: E_net = sum(E_i)
    * Force on charge q at point P: F = q * E_net
    """

    num_charges = int(input("Enter the number of charges: "))
    charges = []
    positions = []

    for i in range(num_charges):
        charge, units = get_float_input(f"Enter the value of charge {i+1} (in Coulombs): ")
        charges.append(charge)

        x, units = get_float_input(f"Enter x-coordinate of charge {i+1} (in meters): ")
        y, units = get_float_input(f"Enter y-coordinate of charge {i+1} (in meters): ")
        z, units = get_float_input(f"Enter z-coordinate of charge {i+1} (in meters): ")
        positions.append(np.array([x, y, z]))

    # Calculate field & force at a point 
    px, units = get_float_input("Enter x-coordinate of the point (in meters): ")
    py, units = get_float_input("Enter y-coordinate of the point (in meters): ")
    pz, units = get_float_input("Enter z-coordinate of the point (in meters): ")
    point_of_interest = np.array([px, py, pz])

    net_electric_field = np.array([0.0, 0.0, 0.0])  # Start with zero field
    for charge, position in zip(charges, positions):
        r_vec = point_of_interest - position
        r_mag = np.linalg.norm(r_vec)
        r_hat = r_vec / r_mag

        E_i = CONSTANTS["k"] * charge / r_mag**2 * r_hat
        net_electric_field += E_i

    print("Net electric field at the point:", net_electric_field, "N/C")

    # ... (Add force calculation similarly) 

# ... Other problem-solving functions (revise accordingly) 

# Main Program (no substantial changes necessary)
# ... 
