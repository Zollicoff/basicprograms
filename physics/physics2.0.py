"""
This program is a physics problem solver for Physics 2 topics.
Created by Zachary A. Hampton
"""

# Constants
CONSTANTS = {
    "k": 8.99 * 10**9,  # Coulomb's constant
    "epsilon0": 8.85 * 10**-12,  # Permittivity of free space
    "pi": 3.14159,  # Value of pi
    "mu0": 4 * 3.14159 * 10**-7,  # Permeability of free space
}

def get_float_input(prompt):
    """
    This function prompts the user for input and returns a float.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def electric_fields_and_forces():
    """
    This function calculates the electric fields and forces.
    """
    q = get_float_input("Enter the charge (in Coulombs): ")
    r = get_float_input("Enter the distance from the charge (in meters): ")
    q1 = get_float_input("Enter the value of the first charge (in Coulombs): ")
    q2 = get_float_input("Enter the value of the second charge (in Coulombs): ")
    E = CONSTANTS["k"] * q / r**2
    F = CONSTANTS["k"] * q1 * q2 / r**2
    print("The electric field at a distance of", r, "meters from the charge is", E, "N/C.")
    print("The force between two charges", q1, "C and", q2, "C at a distance of", r, "meters is", F, "N.")

def gauss_law_applications():
    """
    Function to solve problems related to Gauss's law applications
    """
    q = get_float_input("Enter the charge enclosed by the Gaussian surface (in Coulombs): ")
    A = get_float_input("Enter the area of the Gaussian surface (in square meters): ")
    E = q / (CONSTANTS["epsilon0"] * A)
    print("The electric field through the Gaussian surface is", E, "N/C.")

def electric_potential_and_potential_energy():
    """
    Function to solve problems related to electric potential and potential energy
    """
    q = get_float_input("Enter the charge (in Coulombs): ")
    r = get_float_input("Enter the distance from the charge (in meters): ")
    q1 = get_float_input("Enter the value of the first charge (in Coulombs): ")
    q2 = get_float_input("Enter the value of the second charge (in Coulombs): ")
    V = CONSTANTS["k"] * q / r
    U = CONSTANTS["k"] * q1 * q2 / r
    print("The electric potential at a distance of", r, "meters from the charge is", V, "V.")
    print("The potential energy between two charges", q1, "C and", q2, "C at a distance of", r, "meters is", U, "J.")

def capacitance_and_dielectrics():
    """
    Function to solve problems related to capacitance and dielectrics
    """
    A = get_float_input("Enter the area of the capacitor plates (in square meters): ")
    d = get_float_input("Enter the distance between the capacitor plates (in meters): ")
    k = get_float_input("Enter the dielectric constant: ")
    C = (k * CONSTANTS["epsilon0"] * A) / d
    print("The capacitance of the capacitor is", C, "F.")

def current_resistance_and_emf():
    """
    Function to solve problems related to current, resistance, and electromotive force
    """
    V = get_float_input("Enter the voltage (in volts): ")
    R = get_float_input("Enter the resistance (in ohms): ")
    I = V / R
    print("The current in the circuit is", I, "A.")

def direct_current_circuits():
    """
    Function to solve problems related to direct current circuits
    """
    V = get_float_input("Enter the voltage (in volts): ")
    R1 = get_float_input("Enter the resistance of the first resistor (in ohms): ")
    R2 = get_float_input("Enter the resistance of the second resistor (in ohms): ")
    Req = R1 + R2
    I = V / Req
    print("The equivalent resistance of the circuit is", Req, "ohms.")
    print("The current in the circuit is", I, "A.")

def magnetic_fields_and_forces():
    """
    Function to solve problems related to magnetic fields and forces
    """
    I = get_float_input("Enter the current (in amperes): ")
    r = get_float_input("Enter the distance from the wire (in meters): ")
    B = (CONSTANTS["mu0"] * I) / (2 * CONSTANTS["pi"] * r)
    print("The magnetic field at a distance of", r, "meters from the wire is", B, "T.")

def sources_of_the_magnetic_field():
    """
    Function to solve problems related to sources of the magnetic field
    """
    N = get_float_input("Enter the number of turns in the coil: ")
    I = get_float_input("Enter the current in the coil (in amperes): ")
    A = get_float_input("Enter the area of the coil (in square meters): ")
    B = (CONSTANTS["mu0"] * N * I) / A
    print("The magnetic field inside the coil is", B, "T.")

def faradays_law():
    """
    Function to solve problems related to Faraday's law
    """
    N = get_float_input("Enter the number of turns in the coil: ")
    B = get_float_input("Enter the magnetic field (in teslas): ")
    A = get_float_input("Enter the area of the coil (in square meters): ")
    t = get_float_input("Enter the time interval (in seconds): ")
    emf = -N * B * A / t
    print("The induced emf in the coil is", emf, "V.")

def inductance():
    """
    Function to solve problems related to inductance
    """
    N = get_float_input("Enter the number of turns in the coil: ")
    A = get_float_input("Enter the area of the coil (in square meters): ")
    l = get_float_input("Enter the length of the coil (in meters): ")
    mu = get_float_input("Enter the permeability of the material: ")
    L = (mu * N**2 * A) / l
    print("The inductance of the coil is", L, "H.")

def electromagnetic_oscillations_and_alternating_current():
    """
    Function to solve problems related to electromagnetic oscillations and alternating current
    """
    L = get_float_input("Enter the inductance (in henrys): ")
    C = get_float_input("Enter the capacitance (in farads): ")
    f = 1 / (2 * CONSTANTS["pi"] * (L * C)**0.5)
    print("The resonant frequency of the circuit is", f, "Hz.")

def maxwells_equations_and_electromagnetic_waves():
    """
    Function to solve problems related to Maxwell's equations and electromagnetic waves
    """
    I = get_float_input("Enter the current (in amperes): ")
    A = get_float_input("Enter the area of the loop (in square meters): ")
    r = get_float_input("Enter the distance from the loop (in meters): ")
    B = (CONSTANTS["mu0"] * I * A) / (2 * CONSTANTS["pi"] * r**3)
    print("The magnetic field at a distance of", r, "meters from the loop is", B, "T.")

# Main Program

def main():
    """
    Main function to run the program
    """
    print("Welcome to the Physics 2 Problem Solver!")
    print("Please select the type of problem you would like to solve:")
    print("1. Electric Fields and Forces")
    print("2. Gauss's Law Applications")
    print("3. Electric Potential and Potential Energy")
    print("4. Capacitance and Dielectrics")
    print("5. Current, Resistance, and Electromotive Force")
    print("6. Direct Current Circuits")
    print("7. Magnetic Fields and Forces")
    print("8. Sources of the Magnetic Field")
    print("9. Faraday's Law")
    print("10. Inductance")
    print("11. Electromagnetic Oscillations and Alternating Current")
    print("12. Maxwell's Equations and Electromagnetic Waves")

    # Problem Selection
    try:
        problem = input("Enter the number of the problem type you would like to solve: ")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    problems = {
        "1": {"name": "Electric Fields and Forces", "description": "This problem type involves the calculation of electric fields and forces.", "function": electric_fields_and_forces},
        "2": {"name": "Gauss's Law Applications", "description": "This problem type involves the application of Gauss's law to calculate electric fields.", "function": gauss_law_applications},
        "3": {"name": "Electric Potential and Potential Energy", "description": "This problem type involves the calculation of electric potential and potential energy.", "function": electric_potential_and_potential_energy},
        "4": {"name": "Capacitance and Dielectrics", "description": "This problem type involves the calculation of capacitance and the effect of dielectrics.", "function": capacitance_and_dielectrics},
        "5": {"name": "Current, Resistance, and Electromotive Force", "description": "This problem type involves the calculation of current, resistance, and electromotive force in circuits.", "function": current_resistance_and_emf},
        "6": {"name": "Direct Current Circuits", "description": "This problem type involves the analysis of direct current circuits.", "function": direct_current_circuits},
        "7": {"name": "Magnetic Fields and Forces", "description": "This problem type involves the calculation of magnetic fields and forces.", "function": magnetic_fields_and_forces},
        "8": {"name": "Sources of the Magnetic Field", "description": "This problem type involves the calculation of magnetic fields from different sources.", "function": sources_of_the_magnetic_field},
        "9": {"name": "Faraday's Law", "description": "This problem type involves the application of Faraday's law to calculate induced emf.", "function": faradays_law},
        "10": {"name": "Inductance", "description": "This problem type involves the calculation of inductance.", "function": inductance},
        "11": {"name": "Electromagnetic Oscillations and Alternating Current", "description": "This problem type involves the analysis of electromagnetic oscillations and alternating current.", "function": electromagnetic_oscillations_and_alternating_current},
        "12": {"name": "Maxwell's Equations and Electromagnetic Waves", "description": "This problem type involves the application of Maxwell's equations and the analysis of electromagnetic waves.", "function": maxwells_equations_and_electromagnetic_waves},
    }

    if problem in problems:
        print(f"You have selected {problems[problem]['name']}.")
        print(problems[problem]['description'])
        print("Please enter the known values and the program will calculate the unknown values.")
        # Call the function to solve the problem
        problems[problem]['function']()
    else:
        print("Invalid problem number. Please enter a number between 1 and 12.")

if __name__ == "__main__":
    main()
