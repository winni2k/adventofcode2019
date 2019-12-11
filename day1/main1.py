module_mass = [int(l.rstrip()) for l in open('input.txt').readlines()]
fuel = []
for mass in module_mass:
    mass //= 3
    mass -= 2
    fuel.append(mass)

print(f'The final fuel requirement is {sum(fuel)}')