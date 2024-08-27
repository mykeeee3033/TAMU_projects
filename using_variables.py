# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Micheal Tidwell
# Section:      102 536
# Assignment:   Lab 2.9
# Date:         26/08/2024


from math import *

#problem 1
velocity = 9
diameter = 0.875
viscos = 0.0015
reynolds_number = (velocity * diameter) / viscos
print(f"Reynolds number is {reynolds_number}")


#problem 2
n = 1
distance = 0.028
scatter_angle = 35
scatter_angle_rad = radians(scatter_angle)
print(f"Wavelength is {(2 * distance)*(sin(scatter_angle_rad))} nm")


#problem 3
initial_rate = 100
decline_rate = 2
time_elapsed = 10
hyperbolic_constant = 0.8
print(f"Production rate is {(initial_rate)/((1+hyperbolic_constant*decline_rate*time_elapsed)**(1/hyperbolic_constant))} barrels/day")

#problem 4
exhaust_vel = 2028
initial_mass = 11000
final_mass = 8300
print(f"Change of velocity is {exhaust_vel * log(initial_mass / final_mass)} m/s")


""" Calculate the Reynolds number for a fluid with velocity 9 m/s, kinematic viscosity 0.0015 m^2/s, and a characteristic linear dimension of 0.875 m.
Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.028 nm, scattering angle of 35 degrees, and first order diffraction. Bragg’s Law describes the scattering of waves from a crystal using the equation nλ = 2d sin θ The standard unit of wavelength in the SI system is nanometers (nm).
Use the Arps equation to calculate the production rate of a well after 10 days, if it had an initial production rate of 100 barrels/day, an initial decline rate of 2/day, and a hyperbolic constant of 0.8.
Use the Tsiolkovsky rocket equation to calculate the change of velocity of a fighter jet for an initial mass of 11000 kg, final mass of 8300 kg, and exhaust velocity of 2028 m/s. """