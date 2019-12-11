with open('input.txt') as fh:
    module_mass = (int(l.rstrip()) for l in fh)

    fuel = ((mass // 3) - 2 for mass in module_mass)

    print(f'The final fuel requirement is {sum(fuel)}')
