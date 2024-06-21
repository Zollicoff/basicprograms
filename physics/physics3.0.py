"""
This program is a physics problem solver for Physics 2 topics.
Created by Zachary A. Hampton
"""

# Constants
K = 8.99e9
EPSILON0 = 8.85e-12
PI = 3.14159
MU0 = 4 * PI * 1e-7

def get_float_input(prompt, min_value=None):
    """ 
    Get a valid float input from the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError("Value must be greater than or equal to {}".format(min_value))
            return value
        except ValueError as e:
            print("Invalid input:", e)

def calculate_and_print(description, formula, **inputs):
    """
    Calculate the result of a formula and print the result with the given description.
    """
    result = formula(**inputs)
    print(description.format(**inputs, result=result))

def electric_fields_and_forces():
    """
    Calculate the electric field and force between charges.
    """
    q, r, q1, q2 = [get_float_input(prompt, 0) for prompt in [
        "Enter the charge (in Coulombs): ",
        "Enter the distance from the charge (in meters): ",
        "Enter the value of the first charge (in Coulombs): ",
        "Enter the value of the second charge (in Coulombs): "
    ]]
    calculate_and_print("The electric field at a distance of {r} meters from the charge is {result} N/C.", lambda q, r: K * q / r**2, q=q, r=r)
    calculate_and_print("The force between two charges {q1} C and {q2} C at a distance of {r} meters is {result} N.", lambda q1, q2, r: K * q1 * q2 / r**2, q1=q1, q2=q2, r=r)

def gauss_law_applications():
    """
    Calculate the electric field through a Gaussian surface.
    """
    q, A = [get_float_input(prompt, 0) for prompt in [
        "Enter the charge enclosed by the Gaussian surface (in Coulombs): ",
        "Enter the area of the Gaussian surface (in square meters): "
    ]]
    calculate_and_print("The electric field through the Gaussian surface is {result} N/C.", lambda q, A: q / (EPSILON0 * A), q=q, A=A)

def electric_potential_and_potential_energy():
    """
    Calculate the electric potential and potential energy between charges.
    """
    q, r, q1, q2 = [get_float_input(prompt, 0) for prompt in [
        "Enter the charge (in Coulombs): ",
        "Enter the distance from the charge (in meters): ",
        "Enter the value of the first charge (in Coulombs): ",
        "Enter the value of the second charge (in Coulombs): "
    ]]
    calculate_and_print("The electric potential at a distance of {r} meters from the charge is {result} V.", lambda q, r: K * q / r, q=q, r=r)
    calculate_and_print("The potential energy between two charges {q1} C and {q2} C at a distance of {r} meters is {result} J.", lambda q1, q2, r: K * q1 * q2 / r, q1=q1, q2=q2, r=r)

def capacitance_and_dielectrics():
    """
    Calculate the capacitance of a capacitor.
    """
    A, d, k_dielectric = [get_float_input(prompt, 0) for prompt in [
        "Enter the area of the capacitor plates (in square meters): ",
        "Enter the distance between the capacitor plates (in meters): ",
        "Enter the dielectric constant: "
    ]]
    calculate_and_print("The capacitance of the capacitor is {result} F.", lambda A, d, k_dielectric: (k_dielectric * EPSILON0 * A) / d, A=A, d=d, k_dielectric=k_dielectric)

def current_resistance_and_emf():
    """
    Calculate the current in a circuit and the equivalent resistance.
    """
    V, R = [get_float_input(prompt, 0) for prompt in [
        "Enter the voltage (in volts): ",
        "Enter the resistance (in ohms): "
    ]]
    calculate_and_print("The current in the circuit is {result} A.", lambda V, R: V / R, V=V, R=R)

def direct_current_circuits():
    """
    Calculate the equivalent resistance and current in a circuit.
    """
    V, R1, R2 = [get_float_input(prompt, 0) for prompt in [
        "Enter the voltage (in volts): ",
        "Enter the resistance of the first resistor (in ohms): ",
        "Enter the resistance of the second resistor (in ohms): "
    ]]
    Req = R1 + R2
    calculate_and_print("The equivalent resistance of the circuit is {Req} ohms.", lambda V, Req: V / Req, V=V, Req=Req)
    calculate_and_print("The current in the circuit is {result} A.", lambda V, Req: V / Req, V=V, Req=Req)

def magnetic_fields_and_forces():
    """
    Calculate the magnetic field and force between charges.
    """
    I, r = [get_float_input(prompt, 0) for prompt in [
        "Enter the current (in amperes): ",
        "Enter the distance from the wire (in meters): "
    ]]
    calculate_and_print("The magnetic field at a distance of {r} meters from the wire is {result} T.", lambda I, r: (MU0 * I) / (2 * PI * r), I=I, r=r)

def sources_of_the_magnetic_field():
    """
    Calculate the magnetic field inside a coil.
    """
    N, I, A = [get_float_input(prompt, 0) for prompt in [
        "Enter the number of turns in the coil: ",
        "Enter the current in the coil (in amperes): ",
        "Enter the area of the coil (in square meters): "
    ]]
    calculate_and_print("The magnetic field inside the coil is {result} T.", lambda N, I, A: (MU0 * N * I) / A, N=N, I=I, A=A)

def faradays_law():
    """
    Calculate the induced emf in a coil.
    """
    N, B, A, t = [get_float_input(prompt, 0) for prompt in [
        "Enter the number of turns in the coil: ",
        "Enter the magnetic field (in teslas): ",
        "Enter the area of the coil (in square meters): ",
        "Enter the time interval (in seconds): "
    ]]
    calculate_and_print("The induced emf in the coil is {result} V.", lambda N, B, A, t: -N * B * A / t, N=N, B=B, A=A, t=t)

def inductance():
    """
    Calculate the inductance of a coil.
    """
    N, A, l, mu = [get_float_input(prompt, 0) for prompt in [
        "Enter the number of turns in the coil: ",
        "Enter the area of the coil (in square meters): ",
        "Enter the length of the coil (in meters): ",
        "Enter the permeability of the material: "
    ]]
    calculate_and_print("The inductance of the coil is {result} H.", lambda N, A, l, mu: (mu * N**2 * A) / l, N=N, A=A, l=l, mu=mu)

def electromagnetic_oscillations_and_alternating_current():
    """
    Calculate the resonant frequency of an LC circuit.
    """
    L, C = [get_float_input(prompt, 0) for prompt in [
        "Enter the inductance (in henrys): ",
        "Enter the capacitance (in farads): "
    ]]
    calculate_and_print("The resonant frequency of the circuit is {result} Hz.", lambda L, C: 1 / (2 * PI * (L * C)**0.5), L=L, C=C)

def maxwells_equations_and_electromagnetic_waves():
    """
    Calculate the magnetic field at a distance from a loop of wire.
    """
    I, A, r = [get_float_input(prompt, 0) for prompt in [
        "Enter the current (in amperes): ",
        "Enter the area of the loop (in square meters): ",
        "Enter the distance from the loop (in meters): "
    ]]
    calculate_and_print("The magnetic field at a distance of {r} meters from the loop is {result} T.", lambda I, A, r: (MU0 * I * A) / (2 * PI * r**3), I=I, A=A, r=r)

def main():
    """
    Main function for the program.
    """
    problem_functions = [
        electric_fields_and_forces,
        gauss_law_applications,
        electric_potential_and_potential_energy,
        capacitance_and_dielectrics,
        current_resistance_and_emf,
        direct_current_circuits,
        magnetic_fields_and_forces,
        sources_of_the_magnetic_field,
        faradays_law,
        inductance,
        electromagnetic_oscillations_and_alternating_current,
        maxwells_equations_and_electromagnetic_waves
    ]

    print("Welcome to the Physics 2 Problem Solver!")
    for i, func in enumerate(problem_functions, start=1):
        print(f"{i}. {func.__name__.replace('_', ' ').title()}")

    choice = get_float_input("Enter the number of the problem type you would like to solve: ", 1)
    if 1 <= choice <= len(problem_functions):
        problem_functions[int(choice) - 1]()
    else:
        print("Invalid choice. Please enter a number between 1 and", len(problem_functions))

if __name__ == "__main__":
    main()
