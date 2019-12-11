def fuel_for_mass(mass):
    return (mass // 3) - 2


def fuel_fuel_calc(mass):
    fuel = 0
    mass_of_diff = fuel_for_mass(mass)
    while mass_of_diff > 0:
        fuel += mass_of_diff
        mass_of_diff = fuel_for_mass(mass_of_diff)
    return fuel

import io
# fh = io.StringIO('100756')
fh = open('input2.txt')

module_mass = (int(l.rstrip()) for l in fh)

fuel = (fuel_fuel_calc(mass) for mass in module_mass)

print(f'The final fuel requirement is {sum(fuel)}')
